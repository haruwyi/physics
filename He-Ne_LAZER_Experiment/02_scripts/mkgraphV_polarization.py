import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 1. データの読み込み
# csv を読み込む
file_path = '/home/haruk/physics/He-Ne_LAZER_Experiment/00_raw_data/20260424_polarization.csv'
df = pd.read_csv(file_path)

a_calib = 0.081980  # 傾き
b_calib = 0.436  # 切片

# 電圧V を 相対強度I に変換 (I = 10^((V-b)/a))
df['intensity'] = 10**((df['voltage'] - b_calib) / a_calib)



# マルスの法則でフィッティング: I = I_max * cos^2(theta - phi) + I_offset
def malus_law(theta, I_max, phi, I_offset):
    return I_max * (np.cos(np.radians(theta - phi)))**2 + I_offset

# 初期値の自動推定
I_max_init = df['intensity'].max() - df['intensity'].min()
phi_init = df['degree'][df['intensity'].idxmax()]
offset_init = df['intensity'].min()

# フィッティングの実行
popt, _ = curve_fit(malus_law, df['degree'], df['intensity'], 
                    p0=[I_max_init, phi_init, offset_init],
                    bounds=([0, -180, 0], [np.inf, 180, np.inf]))

# 結果の展開
I_max_fit, phi_fit, I_offset_fit = popt

# --- 適合結果の数値を出力 ---
print("【マルスの法則 適合結果】")
print(f"最大強度 (I_max)    : {I_max_fit:.4f}")
print(f"偏光面の角度 (phi)  : {phi_fit:.2f} 度")
print(f"補正値 (I_offset)   : {I_offset_fit:.4f}")
print("--------------------------")

# プロット
plt.figure(figsize=(10, 6))
plt.scatter(df['degree'], df['intensity'], label='Calculated Intensity $I$')
theta_line = np.linspace(0, 360, 500)
plt.plot(theta_line, malus_law(theta_line, *popt), 'r--', 
         label=f'Malus Law Fit ($\phi={phi_fit:.1f}^\circ$)')

plt.xlabel('Angle $\\theta$ (deg)')
plt.ylabel('Relative Intensity $I$')
plt.title('Verification of Malus\'s Law')
plt.legend()
plt.grid(True)
plt.savefig('/home/haruk/physics/He-Ne_LAZER_Experiment/03_outputs/polarization_fit.png')
plt.show()