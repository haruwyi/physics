import matplotlib.pyplot as plt
import numpy as np

# データの読み込み
data = np.loadtxt("data.txt")
t = data[:, 0]
x = data[:, 1]

# グラフの作成
plt.figure(figsize=(8, 4))
plt.plot(t, x, label="Position x(t)")
plt.title("Simple Harmonic Motion (Euler Method)")
plt.xlabel("Time [s]")
plt.ylabel("Position [m]")
plt.grid(True)
plt.legend()

# 画像として保存
plt.savefig("result.png")
print("画像保存完了: result.png を作成しました。")
plt.show()