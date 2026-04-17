import pandas as pd
import matplotlib.pyplot as plt
import os

# パスの設定（実行スクリプトと同じ場所にCSVがある場合）
file_path = '/home/haruk/physics/He-Ne_LAZER_Experiment/00_raw_data/20260417_all.csv'
df = pd.read_csv(file_path)

# データの読み込み
df = pd.read_csv(file_path)

# グラフの設定
plt.figure(figsize=(10, 7))

# 3つのデータをそれぞれプロット（マーカーや線種を変えると見やすいです）
plt.semilogx(df['intensity'], df['voltage_default'], marker='o', label='Trial 1 (Original)')
plt.semilogx(df['intensity'], df['voltage_tilt'], marker='s', linestyle='--', label='Trial 2 (Repositioned)')
plt.semilogx(df['intensity'], df['voltage_indark'], marker='^', linestyle=':', label='Trial 3 (Readjusted)')

# グラフの装飾
plt.xlabel('Relative Light Intensity $I$ (Log Scale)')
plt.ylabel('Electromotive Force $V$ (V)')
plt.title('Comparison of Solar Cell Output Characteristics')
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.legend() # 凡例を表示

# 保存と表示
plt.savefig('comparison_plot.png')
plt.show()