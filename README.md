# GASO_NetworkAnalysis

## Description:
**Author:** EW  
**Last Update:** 11/12/2021  
**Description:** This network analysis contains information about IP addresses, looking up publicly-available Internet data.  

1. `GetIPs.ipynb` : This code makes a DNS server request for every domain name within the ScamWebsites.csv file. It extracts IP addresses. It then uses an IP-search API to get the lat-long coordinates, ISP, org name, AS, etc. information from the IP address and merges this with the scam websites. Results in some intermediate files due to reasons explained in the notebook.  
2. `Analyze_My_Data.ipynb` : This code analyzes ScamWebsites.csv, which came from a batch search on ScamAdviser. It creates graphs based on interesting data pulled from the results.  
3. `IPDataAnlysis.ipynb` : This code analyzes my own IP code from program #1. It creates similar charts to #2.  