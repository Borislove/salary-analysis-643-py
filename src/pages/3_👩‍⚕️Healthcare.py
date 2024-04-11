# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import streamlit as st

# Здравоохранение

# ------------Option---------
pd.options.display.expand_frame_repr = False
matplotlib.use('Qt5Agg')
# ---------DATA-------------
url = 'https://raw.githubusercontent.com/Borislove/files/main/data/data.csv'
DATA = pd.read_csv(url, index_col=0)
inflation = DATA.values[3]

# print(DATA.index)
DATA = DATA.drop(index=('Образование'))
DATA = DATA.drop(index=('Государственное управление и обеспечение военной безопасности; социальное страхование'))

print(DATA.values[0])
print(DATA)

print(DATA.index)
st.dataframe(data=DATA, width=1500, height=110)

healthcare = DATA.values[0]
columns = DATA.columns

txt_education = 'Здравоохранение'
txt_inflation = 'Инфляция'

# CHECKBOX
checkbox = st.checkbox('Инфляция', True)
flag = False
if checkbox:
    flag = True

if flag:  # тут идет подсчет с инфляцией
    st.write('''Динамика номинальных и реальных заработных плат: Здравоохранение и предоставление социальных услуг''')
    plt.title(txt_education + "С учетом инфляции")
    fig = plt.figure(figsize=(13, 10))
    plt.plot(columns, healthcare)  # исключаем столбцы
    plt.plot(columns, (1 - inflation / 100) * healthcare)
    plt.legend(['номинальные', 'реальные'])
    st.write(plt.figure(fig))
else:
    st.write('''Динамика номинальных заработных плат: Здравоохранение и предоставление социальных услуг''')
    fig = plt.figure(figsize=(13, 10))
    plt.plot(columns, healthcare)  # исключаем столбцы
    plt.legend(['номинальные'], loc='best')
    st.write(plt.figure(fig))

# --------------------------------------------------------------------
# # пирог


# image = Image.open('education.jpg')
st.image(image='\salary-analysis-643-py\src\pages\healthcare.jpg', caption='healthcare')

st.write('''Врачи, медсестры и другие специалисты здравоохранения получают сейчас гораздо больше, чем раньше, за свою работу.
Это связано с увеличением спроса на медицинские услуги, ростом медицинских технологий и 
увеличением финансирования здравоохранения со стороны правительства и частных компаний. Кроме того, 
медицинская профессия требует специального обучения и опыта, что также влияет на уровень заработной платы в этой сфере. 
К концу 2023 года заработные платы значительно выросли.
''')
