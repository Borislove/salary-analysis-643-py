# -*- coding: utf-8 -*-
import pandas as pd

url = 'https://raw.githubusercontent.com/Borislove/files/main/data/poverty1.csv'
DATA3 = pd.read_csv(url, index_col=0)
print(DATA3)


