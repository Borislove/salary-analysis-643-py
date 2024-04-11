# -*- coding: utf-8 -*-
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# -------OPTION--------------------
pd.options.display.expand_frame_repr = False

# ---------DATA-------------
url = 'https://raw.githubusercontent.com/Borislove/files/main/data/data.csv'
DATA = pd.read_excel(url)

print(DATA)  # без инфляции

# st.title(' ')


# print(DATA.values[0])  # столбцы  0
# # print(DATA.values[3]) # инфляция 3
#
# education = 'Образование'
#
# plt.figure(figsize=(5, 5))
#
# plt.title(education)
# # plt.show(DATA.index(education))
# plt.figure(figsize=(5, 5))
# plt.plot(DATA.columns, DATA.values[0])
# plt.show()
