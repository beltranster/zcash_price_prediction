# zcash_price_prediction
In this repo, you will find the code developed to create an ML model that predicts shifts in price of cyptocurrency Zcash based on market news
Please read 01_ file to understand the flow. 
I use a .plist script to run the .py files and get daily data for news and prices which I store individually
Then, I use an .ipynb to read all the stored files and consolidate into two .csv files: all_zec.csv for price and sample_news.csv (last one is a sample because the actual file was too large to upload)
I explored extracting the data from different sites, such as CoinLore and Google, and ended up using the Coingecko API because it provided the most granular price information (price every 5 min), which is what I was trying to get
