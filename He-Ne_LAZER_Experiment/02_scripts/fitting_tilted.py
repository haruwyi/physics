import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = '/home/haruk/physics/He-Ne_LAZER_Experiment/00_raw_data/20260417_V_tilted_copy.csv'
df = pd.read_csv(file_path)

results = []

x_log = np.log10(df['intensity'])

y = df['voltage']

a, b = np.polyfit(x_log, y, 1)

y_pred = a * x_log + b
r2 = 1 - (np.sum((y - y_pred)**2) / np.sum((y - np.mean(y))**2))


results.append({'Slope (a)': a, 'Intercept (b)': b, 'R2': r2})

print(results)