import pandas as pd

iowa_file_path = 'train.csv'
home_data = pd.read_csv(iowa_file_path)

print(home_data.describe())

avg_lot_size = round(home_data.LotArea.mean())
newest_home_age = 2026 - home_data.YearBuilt.max()

print(f'Tamaño medio del lote: {avg_lot_size}')
print(f'Antigüedad de la vivienda más nueva: {newest_home_age} años')
