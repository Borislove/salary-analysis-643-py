import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.options.display.expand_frame_repr = False
url = 'https://raw.githubusercontent.com/Borislove/files/main/data/research.csv'
DATA1 = pd.read_csv(url, index_col=0)
print(DATA1)