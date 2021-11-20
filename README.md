# GASO_NetworkAnalysis

## Description:
**Author:** EW  
**Last Update:** 11/12/2021  
**Description:** This network analysis contains information about IP addresses, looking up publicly-available Internet data.  

1. `GetIPs.ipynb` : This code makes a DNS server request for every domain name within the ScamWebsites.csv file. It extracts IP addresses. It then uses an IP-search API to get the lat-long coordinates, ISP, org name, AS, etc. information from the IP address and merges this with the scam websites. Results in some intermediate files due to reasons explained in the notebook.  
2. `Analyze_My_Data.ipynb` : This code analyzes ScamWebsites.csv, which came from a batch search on ScamAdviser. It creates graphs based on interesting data pulled from the results.  
3. `IPDataAnlysis.ipynb` : This code analyzes my own IP code from program #1. It creates similar charts to #2.  
4. `DownloadRepository.ipynb` : This code enables you to enter an open s3 bucket or other reposity and download all the listed images. Requires the link which contains the XML file of folder contents.  
5. `walletTrace.ipynb` : This code allows a user to enter the wallet address of a USDT crypto account. It will trace 10 levels back, looking at the top 5 senders and receivers to each wallet in the link, and then their top 5 senders and receivers (next level).  
6. `WHOIS_Import.ipynb` : This code uses an API to extract WHOIS data for both existing and defunct sites, compiling them all in a csv document.  
7. `downloadWallet/downloadWallet.ipynb` : This code enables a user to input a USDT wallet account, and will output a CSV of the wallet transactions using the ethernet.io API and a CSV summary of the transactions.  
8. `downloadWallet/py` : This code provides a GUI user interface for a user to download wallet transactions and an account summary for USDT wallet accounts.  
9. `wallet_functions.py` : helper functions for #7/#8  
10. `SiteCompare.py` : This code goes through all known scam websites and classifies them based on their landing page. Like HTML templates are grouped together.  