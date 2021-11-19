
# README

**Author:** Elisa Warner  
**Date:** 11/19/2021  
**Description:** The code in this folder pertains to a simple user interface to utilize the etherscan.io API. The interface allows you to simply input the wallet address, then download: 1) a CSV of the entire history of the wallet, and 2) a transaction summary of all transactions in this wallet.  

## Contents
1. `downloadWallet.ipynb`: This Python Notebook allows a user to input the Source address and obtain the transaction and summary data.  
2. `downloadWallet.py`: This executable script is an interface version of the Python Notebook. It requests users to input the wallet address.  

3. `wallet_functions.py`: Helper functions for #1/#2.  

## How to run
First, make sure you have a config file set up. The config file should look like below:  

```
############### ADD ADDRESS HERE ##########################
walletAddress = "<WALLET ADDRESS HERE>"


############## DO NOT CHANGE BELOW LINE ###################
apiKeyETHERSCAN = "<APIKEY HERE>"
```

Title this file `config.py`.  

You can obtain an API key by creating an etherscan API account here:
https://etherscan.io/apis  

Simply find the API key and add here.  

To run #1, simply open a Jupyter Notebook and run each cell. To run #2, go to your terminal or command prompt, and type: `python downloadWallet.py`. Wait for the interactive GUI to appear.  

## Dependencies
This code was tested on a PC with Windows 11 and Anaconda, Python=3.8. If you have Anaconda, all packages should already be installed for you. If you do not know how to install, contact `elisawa@umich.edu` for an executable version. You can choose to attempt to run this as a python executable. If so, look at "Creating the Environment" below.  

## Creating the Environment
If you decide to create an environment to run the code from a python script, install python=3.8. Then, download dependencies by typing `pip install -r requirements.txt` into the terminal. Then run the code command `python downloadWallet.py` and look for a GUI window to pop up.  