# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import streamlit as st

# ------------Option---------
pd.options.display.expand_frame_repr = False
matplotlib.use('Qt5Agg')
# ---------DATA-------------
url = 'https://raw.githubusercontent.com/Borislove/files/main/data/data.csv'
DATA = pd.read_csv(url, index_col=0)
inflation = DATA.values[3]
# print(inflation)

# DATA.head(1)
DATA = DATA.drop(index=('Образование'))
DATA = DATA.drop(index=('Здравоохранение и предоставление социальных услуг'))
# print(DATA.index)
# print(DATA.columns)
st.dataframe(data=DATA, width=1500, height=110)

security = DATA.values[0]
print(security)
columns = DATA.columns

# txt = 'Средняя заработная плата в сфере: '
txt_education = 'Гос.управление'
txt_inflation = 'Инфляция'

# CHECKBOX
checkbox = st.checkbox('Инфляция', True)
flag = False
if checkbox:
    flag = True

if flag:  # тут идет подсчет с инфляцией
    st.write('''Динамика номинальных и реальных заработных плат: Государственное управление и обеспечение военной безопасности; социальное страхование''')
    plt.title(txt_education + "С учетом инфляции")
    fig = plt.figure(figsize=(13, 10))
    plt.plot(columns, security)  # исключаем столбцы
    plt.plot(columns, (1 - inflation / 100) * security)
    plt.legend(['номинальные', 'реальные'])
    st.write(plt.figure(fig))
else:
    st.write('''Динамика номинальных заработных плат: Государственное управление и обеспечение военной безопасности; социальное страхование''')
    fig = plt.figure(figsize=(13, 10))
    plt.plot(columns, security)  # исключаем столбцы
    plt.legend(['номинальные'], loc='best')
    st.write(plt.figure(fig))

st.image(image='\salary-analysis-643-py\src\pages\security.jpg', caption='security')


st.write('''
Заработная плата в отрасли:  Государственное управление и обеспечение военной безопасности значительно увеличилась с течением времени. 
Это обусловлено рядом факторов, включая инфляцию, повышение квалификации сотрудников, увеличение ответственности и сложности выполняемых задач, а также изменениями в законодательстве. Государственные служащие и работники военно-промышленной отрасли обычно имеют стабильные и высокие заработные платы, что делает эти профессии привлекательными для многих людей. Кроме того, в связи с повышением требований к безопасности и защите государства, спрос на профессионалов в этой отрасли постоянно растет, что также влияет на уровень заработной платы.

''')