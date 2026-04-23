import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. データの準備
file_path = '/home/haruk/physics/He-Ne_LAZER_Experiment/00_raw_data/20260417_all.csv'
df = pd.read_csv(file_path)

# 独立変数（強度）を対数に変換
x_log = np.log10(df['intensity'])

# フィッティング結果を格納するリスト
results = []

# 2. グラフの設定
plt.figure(figsize=(10, 7))
colors = {'V_ref': 'blue', 'V_tilted': 'orange', 'V_dark': 'green', 'V_dark_re':'red'}
labels = {'V_ref': 'Reference', 'V_tilted': 'Tilted', 'V_dark': 'Reduced BG', 'V_dark_re': 'Re:Reduced BG'}

# 3. 各カラムに対してループ処理
for col in ['V_ref', 'V_tilted', 'V_dark', 'V_dark_re']:
    y = df[col]
    
    # 最小二乗法による1次式フィッティング: V = a*log10(I) + b
    a, b = np.polyfit(x_log, y, 1)
    
    # 決定係数 R^2 の計算（適合度の指標）
    y_pred = a * x_log + b
    r2 = 1 - (np.sum((y - y_pred)**2) / np.sum((y - np.mean(y))**2))
    
    # 結果を保存
    results.append({'Condition': col, 'Slope (a)': a, 'Intercept (b)': b, 'R2': r2})
    
    # プロット（実測値は点、フィッティングは線）
    plt.scatter(df['intensity'], y, color=colors[col], alpha=0.6)
    plt.plot(df['intensity'], y_pred, color=colors[col], 
             linestyle='--', label=f'{labels[col]} (a={a:.3f}, R2={r2:.4f})')

# 4. グラフの装飾
plt.xscale('log')
plt.xlabel('Relative Light Intensity $I$')
plt.ylabel('Photovoltaic Output $V$ (V)')
plt.title('Fitting of Solar Cell Characteristics')
plt.grid(True, which="both", ls="-", alpha=0.3)
plt.legend()
plt.savefig('/home/haruk/physics/He-Ne_LAZER_Experiment/03_outputs/fitting_re.png')
plt.show()

# 5. パラメータをテーブルで表示
results_df = pd.DataFrame(results)
print(results_df)