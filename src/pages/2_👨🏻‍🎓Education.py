# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import streamlit as st

# Образование
# ------------Option---------
pd.options.display.expand_frame_repr = False
#matplotlib.use('Qt5Agg')
# ---------DATA-------------
url = 'https://raw.githubusercontent.com/Borislove/files/main/data/data.csv'
DATA = pd.read_csv(url, index_col=0)
inflation = DATA.values[3]
# print(inflation)

# DATA.head(1)
DATA = DATA.drop(index=('Здравоохранение и предоставление социальных услуг'))
DATA = DATA.drop(index=('Государственное управление и обеспечение военной безопасности; социальное страхование'))
# print(DATA.index)
# print(DATA.columns)
st.dataframe(data=DATA, width=1500, height=110)

education = DATA.values[0]
print(education)
columns = DATA.columns

# txt = 'Средняя заработная плата в сфере: '
txt_education = 'Образование'
txt_inflation = 'Инфляция'

# CHECKBOX
checkbox = st.checkbox('Инфляция', True)
flag = False
if checkbox:
    flag = True

if flag:  # тут идет подсчет с инфляцией
    st.write('''Динамика номинальных и реальных заработных плат: Образование''')
    plt.title(txt_education + "С учетом инфляции")
    fig = plt.figure(figsize=(13, 10))
    plt.plot(columns, education)  # исключаем столбцы
    plt.plot(columns, (1 - inflation / 100) * education)
    plt.legend(['номинальные', 'реальные'])
    st.write(plt.figure(fig))
else:
    st.write('''Динамика номинальных заработных плат: Образование''')
    fig = plt.figure(figsize=(13, 10))
    plt.plot(columns, education)  # исключаем столбцы
    plt.legend(['номинальные'], loc='best')
    st.write(plt.figure(fig))

# --------------------------------------------------------------------
# # пирог


# image = Image.open('education.jpg')
st.image(image='\salary-analysis-643-py\src\pages\education.jpg', caption='education')


st.write('''
Заработная плата в отрасли образования значительно увеличилась с течением времени. Этот факт является свидетельством изменений, происходящих в обществе и признания важности образования в современном мире. Стремительное развитие технологий и повышение квалификации специалистов привели к повышению требований к уровню образования и, как следствие, к увеличению заработной платы. Важность образования в нашей жизни не может быть переоценена, и продвижение в этой сфере должно вознаграждаться соответствующим образом.  
  
Одной из главных причин роста заработной платы в образовании является повышение статуса учителей и преподавателей в обществе. Учительство ранее считалось менее престижной профессией, но сегодня образование приобретает все большее значение, и теперь учителя и педагоги получают заслуженное признание и доступ к более высоким возможностям карьерного роста. В свою очередь, повышение статуса учителей влечет за собой улучшение их материального положения, поскольку общество понимает, что процесс образования играет решающую роль в формировании будущего.  
  
Также нельзя не упомянуть о реформах, осуществляемых в сфере образования. Постоянные изменения и улучшения программ обучения, внедрение новых методик и подходов к обучению — все это требует большего участия и вложения ресурсов со стороны преподавателей. Осознавая важность их роли, общество и государство всесторонне поддерживают развитие и рост профессионалов в образовании. Увеличение заработной платы является одним из механизмов стимулирования и поддержания качественного преподавания, что в конечном итоге способствует развитию образования в целом.  
  
В целом, увеличение заработной платы в отрасли образования — это положительное явление, которое отражает признание важности образования в обществе. Оно позволяет привлекать талантливых людей в сферу образования, улучшает статус учителей и преподавателей, а также способствует развитию образовательных программ и методик. Это свидетельство прогресса на пути к более качественному и эффективному образованию.
''')
