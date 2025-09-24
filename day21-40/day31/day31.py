import numpy as np
import matplotlib.pyplot as plt
# # 构造信号：两个频率叠加
# t = np.linspace(0, 1, 500)   # 时间轴（0~1秒，500个点）
# signal = np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*120*t)
#
# # 傅里叶变换
# fft_result = np.fft.fft(signal)
# freqs = np.fft.fftfreq(len(t), d=1/500)  # 采样频率500Hz
#
# # 可视化
# plt.figure(figsize=(10,4))
# plt.plot(freqs[:250], np.abs(fft_result)[:250])  # 只看正频率部分
# plt.title("FFT 频谱")
# plt.xlabel("频率 (Hz)")
# plt.ylabel("幅度")
# plt.show()

print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目1开始∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
# ✍️ 今日练习题
# 生成一个混合信号：包含 10Hz 正弦波 和 40Hz 正弦波，采样率为 200Hz，总时长 2 秒。
# 用 np.fft.fft 分析它，并画出频谱图。
# （提示：np.linspace 建立时间序列，注意采样率与 np.fft.fftfreq 配合）
# 用 np.fft.ifft 验证：对信号做 fft 后再做 ifft，能否还原回原始信号？
# （提示：可以对比 np.allclose(original, restored)）

# 生成一个混合信号：包含 10Hz 正弦波 和 40Hz 正弦波，采样率为 200Hz，总时长 2 秒
t=np.linspace(0,2,400)
# t = np.linspace(0, 2, 400, endpoint=False)
# 这样能保证时间间隔严格是 1/200 秒，否则最后一个点会稍微偏差。
# 时间轴2s，400个点
signal_1=np.sin(2*np.pi*10*t)+1.5*np.sin(2*np.pi*40*t)
# 傅里叶变换
fft_result1=np.fft.fft(signal_1)
# 采样频率200Hz
freqs1=np.fft.fftfreq(len(t),d=1/200)
# 可视化
plt.figure(figsize=(10,4))
plt.plot(freqs1[:250], np.abs(fft_result1)[:250])  # 只看正频率部分
plt.title("FFT frequency spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()
# 用 plt.stem 可视化频谱
# FFT 结果本质是离散点，用 stem 更直观：

# plt.stem(freqs1[:200], np.abs(fft_result1)[:200], use_line_collection=True)
# plt.title("FFT frequency spectrum (stem)")
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Magnitude")
# plt.show()
# 验证频谱还原
restored_signal=np.fft.ifft(fft_result1)
print("Is the restored signal identical to the original?", np.allclose(signal_1, restored_signal))




