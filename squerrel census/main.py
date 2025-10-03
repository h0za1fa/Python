import pandas as pd

sqrl_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251002.csv')

# colors = sqrl_data['Primary Fur Color']
# print(colors)

sqrl_colors = sqrl_data.value_counts('Primary Fur Color')

sqrl_colors.to_csv('sqrl_color_data.csv')