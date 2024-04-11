import pandas as pd

# игнорируем перенос столбцов
pd.options.display.expand_frame_repr = False

infl_data = pd.read_excel('infl_rab.xlsx', skiprows=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], index_col=0)
print(infl_data.values)
