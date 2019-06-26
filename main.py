import pandas as pd
from pandas_datareader import data as web
import numpy as np
from plotly import __version__
print(__version__)
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import datetime

# We will look at stock prices over the past year, starting at January 1, 2016
start = datetime.datetime(2016,1,1)
end = datetime.date.today()

# Populate the variables "apple", "microsoft" and "google" with real stock market data (using pandas datareader, which reads stocks from the web)
apple = web.DataReader("AAPL", "yahoo", start,  end)
microsoft = web.DataReader("MSFT", "yahoo", start, end)
google = web.DataReader("GOOG", "yahoo", start, end)

# Define a pandas dataframe containing stocks from Apple, Google and Microsoft
df = pd.DataFrame({"AAPL": apple["Adj Close"],
                      "MSFT": microsoft["Adj Close"],
                      "GOOG": google["Adj Close"]})

# This returns the first value of the dataframe define above, just to check it's got some values in it.
df.head()

# This plots the dataframe into plotly, assuming that ~/.plotly api key exists, otherwise it will say you're not logged in.
df[['AAPL','MSFT', 'GOOG']].iplot(kind='spread')