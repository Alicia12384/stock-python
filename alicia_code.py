

import pandas as pd
import numpy as np
from plotly import __version__
print(__version__)
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


cf.go_offline() # allows us to use cufflinks offline

df=pd.DataFrame(np.random.randn(100,4), columns='A B C D'.split())
df.head()

df[['A','B']].iplot(kind='spread')
# this is useful for things like comparing stocks
# you get a plot which shows them against each other, and then a subplot underneath showing the spread of them against each other