import requests
import json
import numpy as np
import pandas as pd
from datetime import datetime
from config import *

################ CACHING & DATA RETRIEVAL ###################
# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------
CACHE_FNAME = 'cache_file.json'
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
DEBUG = False
apiKey = apiKeyETHERSCAN

# -----------------------------------------------------------------------------
# Load cache file
# -----------------------------------------------------------------------------
try:
    with open(CACHE_FNAME, 'r') as cache_file:
        cache_json = cache_file.read()
        CACHE_DICTION = json.loads(cache_json)
except:
    CACHE_DICTION = {}


def has_cache_expired(timestamp_str, expire_in_days): # BUG 1
    """Check if cache timestamp is over expire_in_days old"""
    # gives current datetime
    now = datetime.now()

    # datetime.strptime converts a formatted string into datetime object
    cache_timestamp = datetime.strptime(timestamp_str, DATETIME_FORMAT)

    # subtracting two datetime objects gives you a timedelta object
    delta = now - cache_timestamp
    delta_in_days = delta.days

    # now that we have days as integers, we can just use comparison
    # and decide if cache has expired or not
    if delta_in_days < expire_in_days: #BUG 2
        return False
    else:
        return True

def params_unique_combination(baseurl, params_d, private_keys=["api_key"]):
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)

def get_from_cache(url, params_d):
    """If URL exists in cache and has not expired, return the html, else return None"""
    cache_key = params_unique_combination(url, params_d)
    if cache_key in CACHE_DICTION:
        url_dict = CACHE_DICTION[cache_key]
 #       html = CACHE_DICTION[url]['html']
        if has_cache_expired(url_dict['timestamp'], url_dict['expire_in_days']):
            # also remove old copy from cache
            del CACHE_DICTION[cache_key]
            html = None
        else:
            html = CACHE_DICTION[cache_key]['html']
    else:
        html = None

    return html

def set_in_cache(url, params_d, html, expire_in_days):
    """Add URL and html to the cache dictionary, and save the whole dictionary to a file as json"""
    cache_key = params_unique_combination(url, params_d)
    
    CACHE_DICTION[cache_key] = {
        'html': html,
        'timestamp': datetime.now().strftime(DATETIME_FORMAT),
        'expire_in_days': expire_in_days
    }

    with open(CACHE_FNAME, 'w') as cache_file:
        cache_json = json.dumps(CACHE_DICTION)
        cache_file.write(cache_json)

def get_html_from_url(url, params_d, expire_in_days=7): #Added params_d
    """Check in cache, if not found, load html, save in cache and then return that html"""
    # check in cache
    html = get_from_cache(url, params_d)
 #   print(html)
    if html is not None:
        if DEBUG:
            print('Loading from cache: {0}'.format(url))
    else:
 #       if DEBUG:
        print('Fetching a fresh copy: {0}'.format(url))
 #       print()

        # fetch fresh
        response = requests.get(url, params=params_d)

        # Deleted line about encoding because it was messing up my shit

        html = response.text

        # cache it
        set_in_cache(url, params_d, html, expire_in_days)

    return html


######################## END CACHING #############################################

def RequestWalletAddress(address):
    #contractAddress = '0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2'
    params_d = {}
    baseurl = "https://api.etherscan.io/api"
    params_d['module'] = "account"
    params_d['action'] = "tokentx"
    params_d['contractaddress'] = '0xdac17f958d2ee523a2206206994597c13d831ec7' # tether
    params_d['address'] = address
    #params_d['offset'] = 100
    params_d['sort'] = "asc"
    params_d['apikey'] = apiKey
    
    google_results = get_html_from_url(baseurl, params_d, expire_in_days=1)
    #print(google_results)
    results = json.loads(google_results)['result']
    
    return results

def ResultScan(results, address):
    outAddress = {} # who are they submitting to
    inAddress = {} # who is sending to them
    
    for transaction in results:
        if transaction['from'].upper() == address.upper(): # outgoing transactions
            if transaction['to'] not in outAddress:
                outAddress[transaction['to']] = 0
            outAddress[transaction['to']] = outAddress[transaction['to']] + 1
        if transaction['to'].upper () == address.upper(): # incoming transactions
            if transaction['from'] not in inAddress:
                inAddress[transaction['from']] = 0
            inAddress[transaction['from']] = inAddress[transaction['from']] + 1
    
    return outAddress, inAddress

def GetTransactionInfo(df, origAddress):

    ###Transaction Info: Receivers

    # create new transactions doc
    transactions = pd.DataFrame()

    addresses = pd.unique(df['to'])

    for address in addresses:
        if address.upper() == origAddress.upper():
            continue

        # grab data
        sub = df[df['to'] == address]
    
        # collect data
        rowDict = {}
        rowDict["address"] = address
        rowDict["numTransactions"] = int(sub.shape[0]) # number of rows
        rowDict["sumMoney"] = np.sum(sub['value'])
        rowDict["type"] = "OUT"
    
        transactions = transactions.append(rowDict, ignore_index = True)

    ### Transaction Info: Sources
    addresses = pd.unique(df['from'])

    for address in addresses:

        if address.upper() == origAddress.upper():
            continue

        # grab data
        sub = df[df['from'] == address]
    
        # collect data
        rowDict = {}
        rowDict["address"] = address
        rowDict["numTransactions"] = int(sub.shape[0]) # number of rows
        rowDict["sumMoney"] = np.sum(sub['value'])
        rowDict["type"] = "IN"
    
        transactions = transactions.append(rowDict, ignore_index = True)
    
    return transactions