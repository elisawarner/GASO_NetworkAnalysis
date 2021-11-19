#!/usr/bin/env python
# coding: utf-8

# # Download Wallet

# Note: Make sure to have a file called config.py. It should have this line:  
# `apiKeyETHERSCAN = "<API Key>"`  
# Get your apiKey from https://etherscan.io/apis

# Note: etherscan.io has a call limit of 5 calls/s on the free plan.

# In[1]:


import numpy as np
import pandas as pd
from datetime import datetime
from config import *
from wallet_functions import *


# In[2]:


# place wallet address here
origAddress = walletAddress


import tkinter as tk


def submit ():
	origAddress = e1.get() 
	tk.Label(master, text= "SUBMITTED", fg='green', font=('helvetica', 12, 'bold')).grid(row=3)
	
	df = pd.DataFrame()

	try:
		result = RequestWalletAddress(origAddress)

		appendDict = {}

		for row in result:
			appendDict = dict(row)
			appendDict['timeStamp'] = datetime.utcfromtimestamp(int(row['timeStamp'])).strftime('%Y-%m-%d %H:%M:%S')
			appendDict['value'] = int(row['value']) / 10**6
			df = df.append(appendDict, ignore_index = True)

		df.to_csv(origAddress + '.csv', index=False)
		t = GetTransactionInfo(df, origAddress)
		t.to_csv('TransInfo_' + origAddress[-4:] + '.csv', index = False)
		tk.Label(master, text= "     DONE     ", fg='green', font=('helvetica', 12, 'bold')).grid(row=3)
	except:
		tk.Label(master, text= "    ERROR    ", fg='red', font=('helvetica', 12, 'bold')).grid(row=3)


#################### CREATE INTERFACE
master = tk.Tk()

master.geometry("500x100")


tk.Label(master,text="Download USDT Info").grid(row=0,column=1)

tk.Label(master, 
         text="USDT Wallet Address").grid(row=1)

e1 = tk.Entry(master, width = 45)

e1.grid(row=1, column=1)

tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=2, column=0, sticky=tk.W, pady=4)
tk.Button(master, 
          text='Download', command=submit).grid(row=2, column=1, sticky=tk.W, pady=4)

master.mainloop()
