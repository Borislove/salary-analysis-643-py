import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.display.expand_frame_repr = False
# DATA3 = DATA3.drop(DATA3.index[range(1, 4)])

# infl_data = pd.read_excel('infl_rab.xlsx', skiprows=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], index_col=0)
infl_data = pd.read_excel('infl_rab.xlsx', index_col=0)
# print(infl_data.columns)
zp_data = pd.read_excel('zp_srmes_rab.xlsx', index_col=0)
# infl_data = pd.read_excel('infl_rab.xlsx', index_col=0)


# DATA1 = DATA1.drop(DATA1.index[range(0, 32)])
# zp_data = zp_data.drop(zp_data.index[range(2, 3)])
# zp_data = zp_data.drop(zp_data.index[range(1, 2)])
print(zp_data)
# print(infl_data)

mask1 = zp_data.index == 'рыболовство и рыбоводство'
mask2 = infl_data.index == 'Всего'

# plt.figure(figsize=(5, 5))
# plt.plot(zp_data.columns, zp_data[mask1].values[0])
# plt.title("рыболовство и рыбоводство зп до инфляции")
# plt.show()

plt.figure(figsize=(5, 5))
plt.plot(zp_data.columns, zp_data[mask1].values[0])
#plt.plot(infl_data.columns, (infl_data[mask2].values[0] / 100 + 1) * zp_data[mask1].values[0])
plt.plot(infl_data.columns, (1- infl_data[mask2].values[0] / 100 ) * zp_data[mask1].values[0])
plt.title("рыболовство и рыбоводство за с инфляцией и без")
plt.show()

# plt.figure(figsize=(5, 5))
# plt.plot(infl_data.columns, infl_data[mask2].values[0])
# plt.title("Инфляция")
# plt.show()
