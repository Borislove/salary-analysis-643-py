# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import streamlit as st
import seaborn as sns

url = 'https://raw.githubusercontent.com/Borislove/files/main/data/data.csv'
DATA = pd.read_csv(url, index_col=0)
DATA.head()


inflation = DATA.values[3]
columns = DATA.columns

txt_inflation = 'Инфляция'

fig = plt.figure(figsize=(13, 5))
plt.title(txt_inflation)
plt.bar(columns, inflation)
st.write(plt.figure(fig))

