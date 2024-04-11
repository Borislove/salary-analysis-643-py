# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.core import records

# ---- OPTION------------------------------------------
# Сброс ограничений на количество выводимых рядов
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_rows', 8)

# Сброс ограничений на число столбцов
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_columns', 7)

# Сброс ограничений на количество символов в записи
# pd.set_option('display.max_colwidth', None)
# ------------------------------------------------------
# игнорируем перенос столбцов
pd.options.display.expand_frame_repr = False

# -------------DATA----------------


# ----------inflation------------------
#infl_data = pd.read_excel('infl_rab.xlsx', index_col=0)
# ----------------------------------------

# --- test---
# DATA = pd.read_excel('../data/tab3-zpl_2023 — копия.xlsx', index_col=0, sheet_name='с 2017 г.')  # , sheet_name=''

# 2000-2016
DATA1 = pd.read_excel('tab3-zpl_2023.xlsx', skiprows=[0, 1], index_col=0,
                      sheet_name='2000-2016 гг.')  # , sheet_name=''
# 2017
# DATA = pd.read_excel('../data/tab3-zpl_2023.xlsx', index_col=0, sheet_name='с 2017 г.')  # , sheet_name=''

# ----------list 1---------------------------
# игнорирование строк  0 по 4
# DATA2 = pd.read_excel('../data/tab3-zpl_2023.xlsx', skiprows=[0, 1, 2, 3], index_col=0,
#                       sheet_name='с 2017 г.')

# редактирование таблицы - года
DATA2 = pd.read_excel('tab3-zpl_2023 — копия.xlsx', index_col=0,
                      sheet_name='с 2017 г.')

DATA3 = DATA1
DATA4 = DATA2

# print(DATA)

# tables = pd.read_html('../data/Таблицы уровня инфляции.html')
# print(len(tables))
# failures = tables[0]
# print(failures.head())
# print(failures)


# mask1 = DATA.index == 'образование'
# plt.figure(figsize=(5, 5))
# plt.plot(DATA.columns, DATA[mask1].values[0])
# plt.plot(DATA.columns, DATA[mask1].values[0])

# print(DATA[mask1].values)  # [[30257.6 34361.0 37071.9 39563.0 43390.5 48400.2 54262.7]]
##plt.plot(DATA.columns, DATA[mask1].columns)
##plt.plot(DATA.columns, DATA[mask1].columns)

# plt.title("Образование")
# plt.show()
# DATA = DATA.set_index(DATA.loc[:3])
# print(DATA.head())
# print(DATA)


# mask1 = DATA.index == 'образование'
# print(mask1)

# print((DATA.loc['Образование']))  # вывести строку

# колонки
# print(DATA.columns)
# # вытаскиваем года
# print(data.loc[0]['Name'].split('.')[0].split(',')[1].strip())
# срез
# DATA.columns = DATA.columns.str[:4]
# print(DATA1.columns)
# print((DATA1.loc['Образование']))  # вывести строку


# mask2 = DATA2.index == 'образование'

# -------- 2000-2016 --------------- работает
# plt.figure(figsize=(5, 5))
# plt.plot(DATA1.columns, DATA1[DATA1.index == 'Образование'].values[0])
# plt.show()
#
# # -------- с 2017 г. ---------------
# print(DATA2)
# DATA2.columns = DATA2.columns.str[:4]
# plt.figure(figsize=(5, 5))
# plt.plot(DATA2.columns, DATA2[DATA2.index == 'образование'].values[0])
# plt.show()


# --------------------------------------образование- -----------------
education = 'ОБРАЗОВАНИЕ'
print('Лист 2')
DATA1 = DATA1.drop(DATA1.index[range(0, 32)])
DATA1 = DATA1.drop(DATA1.index[range(1, 5)])
print(DATA1)
print('--------------------------------')
print('Лист 1')
DATA2 = DATA2.drop(DATA2.index[range(0, 50)])
DATA2 = DATA2.drop(DATA2.index[range(1, 6)])
print(DATA2)
print('--------------------------------')
# merge
print('Слияние Лист 1, Лист 2')
print('--------------------------------')
DATA_MERGE_1 = DATA1.merge(DATA2, how='cross')
# print(DATA_MERGE.columns)
DATA_MERGE_1 = DATA_MERGE_1.rename(index={0: education})
print(DATA_MERGE_1)
print('--------------------------------')
# --------------------------------график образование- -----------------
# до инфляции
# plt.figure(figsize=(5, 5))
# plt.plot(DATA_MERGE_1.columns, DATA_MERGE_1[DATA_MERGE_1.index == education].values[0])
# plt.title("График изменения зарплаты по годам: Образование до инфляции ")
# plt.show()

# после инфляции
mask2 = infl_data.index == 'Всего'
plt.figure(figsize=(5, 5))
plt.plot(DATA_MERGE_1.columns, DATA_MERGE_1[DATA_MERGE_1.index == education].values[0])
plt.plot(infl_data.columns,
         (1 - infl_data[mask2].values[0] / 100) * DATA_MERGE_1[DATA_MERGE_1.index == education].values[0])

plt.title("образование с инфляцией и без")
plt.legend([education, 'Инфляция'])

plt.show()

# инфляция
# plt.figure(figsize=(5, 5))
# plt.plot(infl_data.columns, infl_data[mask2].values[0])
# plt.title("Инфляция")
# plt.show()

# --------------------------------здравоохранение- -----------------
# деятельность в области здравоохранения и социальных услуг

# healthcare = 'Здравоохранение и предоставление социальных услуг'
# print('Лист 2')
# DATA3 = DATA3.drop(DATA3.index[range(0, 33)])
# DATA3 = DATA3.drop(DATA3.index[range(1, 4)])
# print(DATA3)
# print('--------------------------------')
# print('Лист 1')
# DATA4 = DATA4.drop(DATA4.index[range(0, 51)])
# DATA4 = DATA4.drop(DATA4.index[range(1, 5)])
# print(DATA4)
# print('--------------------------------')
# # merge
# print('Слияние Лист 1, Лист 2')
# print('--------------------------------')
# DATA_MERGE_2 = DATA3.merge(DATA4, how='cross')
# print(DATA_MERGE_2.columns)
# DATA_MERGE_2 = DATA_MERGE_2.rename(index={0: healthcare})
# print(DATA_MERGE_2)
# print('--------------------------------')
# # --------------------------------здравоохранение график -----------------
# # до инфляции
# plt.figure(figsize=(5, 5))
# plt.plot(DATA_MERGE_2.columns,
#          DATA_MERGE_2[DATA_MERGE_2.index == healthcare].values[0])
# plt.title(f"График изменения зарплаты по годам: {healthcare} до инфляции")
# plt.show()
#
# mask3 = infl_data.index == 'Всего'
# plt.figure(figsize=(5, 5))
# plt.plot(DATA_MERGE_2.columns,
#          DATA_MERGE_2[DATA_MERGE_2.index == healthcare].values[0])
# plt.plot(infl_data.columns,
#          (1 -infl_data[mask3].values[0] / 100 ) *
#          DATA_MERGE_2[DATA_MERGE_2.index == healthcare].values[0])
#
# plt.title(f"{healthcare} с инфляцией и без")
# plt.show()
