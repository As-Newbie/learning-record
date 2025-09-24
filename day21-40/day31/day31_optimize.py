import numpy as np
import matplotlib.pyplot as plt

# =============================
# 1. 构造信号
# =============================
fs = 200   # 采样率 200Hz
T = 2      # 时长 2秒
N = fs * T # 采样点数
t = np.linspace(0, T, N, endpoint=False)  # 时间轴 (endpoint=False 保证间隔严格为 1/fs)

# 混合信号：10Hz 正弦 + 40Hz 正弦(幅度1.5)
signal = np.sin(2*np.pi*10*t) + 1.5*np.sin(2*np.pi*40*t)

# =============================
# 2. FFT 变换
# =============================
fft_result = np.fft.fft(signal)
freqs = np.fft.fftfreq(N, d=1/fs)

# 归一化幅度
fft_magnitude = np.abs(fft_result) / N

# =============================
# 3. 可视化频谱
# =============================
plt.figure(figsize=(12,5))

# 折线图
plt.subplot(1,2,1)
plt.plot(freqs[:N//2], fft_magnitude[:N//2])
plt.title("FFT Frequency Spectrum (Line)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

# Stem 图（离散点更直观）
plt.subplot(1,2,2)
plt.stem(freqs[:N//2], fft_magnitude[:N//2])
plt.title("FFT Frequency Spectrum (Stem)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

plt.tight_layout()
plt.show()

# =============================
# 4. IFFT 验证还原
# =============================
restored_signal = np.fft.ifft(fft_result)
print("FFT->IFFT 是否成功还原原始信号？", np.allclose(signal, restored_signal))
