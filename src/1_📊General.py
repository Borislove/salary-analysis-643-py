# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import streamlit as st

txt = ('Реальные и номинальные зарплаты по видам экономической деятельности в Российской Федерации за 2000-2023 гг.')
# st.write(txt)
st.header(txt)

url = 'https://raw.githubusercontent.com/Borislove/files/main/data/data.csv'
DATA = pd.read_csv(url, index_col=0)

st.dataframe(data=DATA, width=1500, height=185)

education = DATA.values[0]
healthcare = DATA.values[1]
security = DATA.values[2]
inflation = DATA.values[3]
columns = DATA.columns

txt = 'Средняя заработная плата в сфере: '
txt_education = 'Образование'
txt_healthcare = 'Здравоохранение и предоставление социальных услуг'
txt_security = 'Государственное управление и обеспечение военной безопасности; социальное страхование'
txt_inflation = 'Инфляция'

fig = plt.figure(figsize=(13, 5))
plt.title('Номинальные заработные платы')
plt.plot(columns, education, color='blue')
plt.plot(columns, healthcare, color='orange')
plt.plot(columns, security, color='green')
plt.legend([txt_education, txt_healthcare, txt_security])
st.write(plt.figure(fig))

st.write('------------------------------------------------------------------------------------------------')
fig2 = plt.figure(figsize=(13, 5))
plt.title('Реальные заработные платы')
plt.plot(columns, (1 - inflation / 100) * education, color='blue')
plt.plot(columns, (1 - inflation / 100) * healthcare, color='orange')
plt.plot(columns, (1 - inflation / 100) * security, color='green')
plt.legend([txt_education, txt_healthcare, txt_security])
st.write(plt.figure(fig2))


st.write('------------------------------------------------------------------------------------------------')
st.image(image='\salary-analysis-643-py\src\pages\gr999.png', caption='rate of increase')
st.write('------------------------------------------------------------------------------------------------')
st.image(image='\salary-analysis-643-py\src\pages\pokazatel.png', caption='pie')
st.write('------------------------------------------------------------------------------------------------')
st.write('Важные экономические показатели')
# ВВП
url = 'https://raw.githubusercontent.com/Borislove/files/main/data/VVP.csv'
DATA1 = pd.read_csv(url, index_col=0)

url = 'https://raw.githubusercontent.com/Borislove/files/main/data/joblessness.csv'
DATA2 = pd.read_csv(url, index_col=0)
# бедность
url = 'https://raw.githubusercontent.com/Borislove/files/main/data/poverty1.csv'
DATA3 = pd.read_csv(url, index_col=0)

DATA_DOP = pd.concat([DATA1, DATA2, DATA3])
st.dataframe(data=DATA_DOP, width=1500, height=150)

st.write('------------------------------------------------------------------------------------------------')
st.image(image='\salary-analysis-643-py\src\pages\corr.png', caption='Pearson correlation coefficient')

st.write('------------------------------------------------------------------------------------------------')
st.image(image='\salary-analysis-643-py\src\pages\corr_s.png', caption='Spearman correlation coefficient')

st.write('------------------------------------------------------------------------------------------------')
st.image(image='\salary-analysis-643-py\src\pages\corr_k.png', caption='Kendall correlation coefficient')
st.write('------------------------------------------------------------------------------------------------')

# ------------------------------------

st.write('''
При анализе представленных данных было установлено снижение инфляции и рост среднемесячных зарплат.
Это говорит о положительных тенденциях в экономике, так как уменьшение инфляции обычно означает стабильность цен на товары и услуги,
что в свою очередь способствует увеличению покупательной способности населения.
Рост среднемесячных зарплат также свидетельствует о росте экономики и улучшении благосостояния работников. 
Эти факторы могут способствовать повышению уровня жизни и увеличению потребительского спроса в стране.
''')