import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# игнорируем перенос столбцов
#pd.options.display.expand_frame_repr = False

# работа в формате xlsx
# ----------inflation------------------
#infl_data = pd.read_excel('/content/sample_data/infl_rab.xlsx', index_col=0)

# образование
# ----------list 2---------------------------
# 2000-2016
DATA1 = pd.read_excel('/content/sample_data/tab3-zpl_2023 — копия.xlsx', skiprows=[0, 1], index_col=0,
                      sheet_name='2000-2016 гг.')


# ----------list 1---------------------------
#2017
DATA2 = pd.read_excel('/content/sample_data/tab3-zpl_2023 — копия.xlsx', index_col=0,
                      sheet_name='с 2017 г.')

# здравоохранение
#DATA3 = DATA1
#DATA4 = DATA2


#print('Лист 2')
DATA1 = DATA1.drop(DATA1.index[range(0, 32)])
DATA1 = DATA1.drop(DATA1.index[range(1, 5)])
#print(DATA1)
#print('--------------------------------')
#print('Лист 1')
DATA2 = DATA2.drop(DATA2.index[range(0, 50)])
DATA2 = DATA2.drop(DATA2.index[range(1, 6)])
#print(DATA2)
#print('--------------------------------')
# merge
#print('Слияние Лист 1, Лист 2')
#print('--------------------------------')
DATA_MERGE = DATA1.merge(DATA2, how='cross')
# print(DATA_MERGE.columns)
DATA_MERGE = DATA_MERGE.rename(index={0: 'ОБРАЗОВАНИЕ'})
#print(DATA_MERGE)
#print('--------------------------------')

plt.figure(figsize=(5, 5))
plt.plot(DATA_MERGE.columns, DATA_MERGE[DATA_MERGE.index == 'ОБРАЗОВАНИЕ'].values[0])
plt.title("График изменения зарплаты по годам: Образование ")
plt.show()

mask2 = infl_data.index == 'Всего'
plt.figure(figsize=(5, 5))
plt.plot(DATA_MERGE.columns, DATA_MERGE[DATA_MERGE.index == 'ОБРАЗОВАНИЕ'].values[0])
plt.plot(infl_data.columns,
         (infl_data[mask2].values[0] / 100 + 1) * DATA_MERGE[DATA_MERGE.index == 'ОБРАЗОВАНИЕ'].values[0])
plt.title("образование с инфляцией и без")
plt.show()

plt.figure(figsize=(5, 5))
plt.plot(infl_data.columns, infl_data[mask2].values[0])
plt.title("Инфляция")
plt.show()

# --------------------------------здравоохранение- -----------------
# деятельность в области здравоохранения и социальных услуг

print('Лист 2')
DATA3 = DATA3.drop(DATA3.index[range(0, 33)])
DATA3 = DATA3.drop(DATA3.index[range(1, 4)])
print(DATA3)
print('--------------------------------')
print('Лист 1')
DATA4 = DATA4.drop(DATA4.index[range(0, 51)])
DATA4 = DATA4.drop(DATA4.index[range(1, 5)])
print(DATA4)
print('--------------------------------')
# merge
print('Слияние Лист 1, Лист 2')
print('--------------------------------')
DATA_MERGE_2 = DATA3.merge(DATA4, how='cross')
print(DATA_MERGE_2.columns)
DATA_MERGE_2 = DATA_MERGE_2.rename(index={0: 'Здравоохранение и предоставление социальных услуг'})
print(DATA_MERGE_2)
print('--------------------------------')



# --------------------------------здравоохранение график -----------------
# до инфляции
plt.figure(figsize=(5, 5))
plt.plot(DATA_MERGE_2.columns,
         DATA_MERGE_2[DATA_MERGE_2.index == 'Здравоохранение и предоставление социальных услуг'].values[0])
plt.title("График изменения зарплаты по годам: Здравоохранение и предоставление социальных услуг до инфляции")
plt.show()


mask3 = infl_data.index == 'Всего'
plt.figure(figsize=(5, 5))
plt.plot(DATA_MERGE_2.columns,
         DATA_MERGE_2[DATA_MERGE_2.index == 'Здравоохранение и предоставление социальных услуг'].values[0])
plt.plot(infl_data.columns,
         (infl_data[mask3].values[0] / 100 + 1) *
         DATA_MERGE_2[DATA_MERGE_2.index == 'Здравоохранение и предоставление социальных услуг'].values[0])
plt.title("Здравоохранение и предоставление социальных услуг с инфляцией и без")
plt.show()

