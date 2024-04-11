import numpy as np

import pandas as pd

# df = pd.read_excel('../data/tab3-zpl.xlsx')
# df = pd.read_excel('tab3-zpl_2023.xlsx') //работает


url = 'https://raw.githubusercontent.com/Borislove/files/main/data/infl_rab.xlsx'
df = pd.read_excel(url)
print(df)


