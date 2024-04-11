import pandas as pd
import streamlit as st

# ---------------------------------------
txt = 'Анализ зарплат в России'
st.markdown(f''':rainbow[{txt}]''')
# ---------------------------------------

# ---------------------------------------
xlsx = pd.ExcelFile('tab3-zpl_2023.xlsx')
# ---------------------------------------
# DATA = pd.read_excel(xlsx, sheet_name="Sheet1")
# print(xlsx.parse(DATA, sheet_name='Sheet1'))

# print(xlsx.sheet_names)  # показать название листа  ['с 2017 г.', '2000-2016 гг.']
# print(xlsx.parse(sheet_name='с 2017 г.'))  # парсинг
# print(xlsx.parse(sheet_name='2000-2016 гг.'))  # парсинг
# DATA = xlsx.parse(sheet_name='2000-2016 гг.')
#frame = pd.read_excel('../data/tab3-zpl_2023.xlsx', sheet_name='2000-2016 гг.')
#print(frame)

# ---------------------------------------
writer = pd.ExcelWriter(xlsx)
#frame.to_excel(writer, "'2000-2016 гг.'")
#frame.to_excel(xlsx)
