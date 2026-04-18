import pandas as pd
import matplotlib.pyplot as plt

# 1. データの読み込み
# csv を読み込む
file_path = '/home/haruk/physics/He-Ne_LAZER_Experiment/00_raw_data/20260417_V_dark.csv'
df = pd.read_csv(file_path)

# 読み込んだデータの中身を確認（最初の数行を表示）
print(df.head())

# 2. データの抽出
# ヘッダー名（intensity, voltage）を指定してデータを取り出す
x = df['intensity']
y = df['voltage']

# 3. グラフの作成
plt.figure(figsize=(8, 6))

# 光の強度（x軸）を対数軸にする 
plt.semilogx(x, y, marker='o', linestyle='-', label='Experimental Data')

# 軸ラベルとタイトルの設定
plt.xlabel('Relative Intensity $I$ (Log Scale)')
plt.ylabel('Photovoltaic Output $V$ (V)')
plt.title('Solar Cell Characteristics - Semi-log Plot')
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.legend()

plt.savefig("/home/haruk/physics/He-Ne_LAZER_Experiment/03_outputs/V_dark.png") # PNG形式で保存

plt.show()