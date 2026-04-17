import pandas as pd
import matplotlib.pyplot as plt
import os

# パスの設定
file_path = '/home/haruk/physics/He-Ne_LAZER_Experiment/00_raw_data/20260417_all.csv'
df = pd.read_csv(file_path)

# データの読み込み
df = pd.read_csv(file_path)

# グラフの設定
plt.rcParams['font.size'] = 12
plt.figure(figsize=(8, 6))

# 3つのデータをそれぞれプロット
plt.semilogx(df['intensity'], df['V_ref'], 'o-', label='Standard')
plt.semilogx(df['intensity'], df['V_tilted'], 's--', label='Tilted (Angle Dep.)')
plt.semilogx(df['intensity'], df['V_dark'], '^-', label='Darkened (BG Reduced)')

# グラフの装飾
plt.xlabel('Relative Light Intensity $I$ (Log Scale)')
plt.ylabel('Photovoltaic Output $V$ (V)')
plt.title('Comparison of Solar Cell Output Characteristics')
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.legend() # 凡例を表示

# 保存と表示
plt.savefig('/home/haruk/physics/He-Ne_LAZER_Experiment/00_raw_data/comparison_plot.png')
plt.show()