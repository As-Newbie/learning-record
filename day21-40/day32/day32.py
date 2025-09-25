from signal import signal

import numpy as np
import matplotlib.pyplot as plt

print("∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目1开始∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
# 题目1：多项式基础
# (a) 定义一个多项式 p(x) = 3x^3 - 2x^2 + x - 5，计算在 x=0,1,2 时的值
# (b) 求这个多项式的导数和积分
# (c) 求这个多项式的全部根
a1=np.poly1d([3,-2,1,-5])
a1_0=np.polyval(a1,0)
a1_1=np.polyval(a1,1)
a1_2=np.polyval(a1,2)
# a1(0), a1(1), a1(2) 直接调用 poly1d 对象就能算值，不必再 np.polyval。
# 示例：
# print(a1(0), a1(1), a1(2))
print(f"多项式为\n{a1}\n其在x=0,1,2 时的值为{a1_0}，{a1_1}，{a1_2}")
a1_differential=np.polyder(a1)
a1_integration=np.polyint(a1)
print(f"多项式为\n{a1}\n其导数为\n{a1_differential}\n积分为\n{a1_integration}")
a1_root=np.roots(a1)
print(f"多项式为\n{a1}\n其所有的根为{a1_root}")
print("∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目2开始∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
# 题目2：多项式构造
# 已知根 [1, -2, 3]，请用 numpy 构造对应的多项式，并写出展开式
a2=np.poly([1,-2,3])
b2=np.poly1d(a2)
print(f"多项式为\n{a2}\n其展开式为\n{b2}\n其根为{np.roots(b2)}")
print("∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目3开始∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
# 题目3：FFT 滤波实验
# (a) 构造一个复合信号：50Hz 正弦波 + 120Hz 正弦波 + 200Hz 正弦波
# (b) 用 FFT 分析并画出频谱图
# (c) 设计一个低通滤波器，只保留 0~100Hz，去掉高频分量
# (d) 用 IFFT 重建信号，并与原始信号对比（画时域波形 + 频域对比）
# 1. 构造复合信号 (50Hz + 120Hz + 200Hz)
fs=500 #采样率100
# 你用了 fs=100，但是信号里有 200Hz 成分。根据采样定理（Nyquist），采样率必须 ≥ 2倍最高频率，否则会混叠。
# 👉 建议改成 fs=500 或更大
T=1
t=np.linspace(0,T,fs*T,endpoint=False)
signal=np.sin(2*np.pi*50*t)+0.5*np.sin(2*np.pi*120*t)+0.3*np.sin(2*np.pi*200*t)
# 2.FFT
fft_result=np.fft.fft(signal)
freqs=np.fft.fftfreq(len(signal),1/fs)
# 3. 低通滤波器: 保留 0~100Hz
fft_filtered = fft_result.copy()
fft_filtered[np.abs(freqs) > 100] = 0
# 4. IFFT
filtered_signal = np.fft.ifft(fft_filtered)
# 画图

plt.figure(figsize=(12,6))

plt.subplot(2,2,1)
plt.plot(t, signal)
plt.title("Original Signal (Time Domain)")
plt.xlabel("Time (s)"); plt.ylabel("Amplitude")

plt.subplot(2,2,2)
plt.plot(freqs[:500], np.abs(fft_result)[:500])
plt.title("Original Signal (Frequency Domain)")
plt.xlabel("Frequency (Hz)"); plt.ylabel("Amplitude")

plt.subplot(2,2,3)
plt.plot(t, filtered_signal.real)
plt.title("Filtered Signal (Time Domain)")
plt.xlabel("Time (s)"); plt.ylabel("Amplitude")

plt.subplot(2,2,4)
plt.plot(freqs[:500], np.abs(fft_filtered)[:500])
plt.title("Filtered Signal (Frequency Domain)")
plt.xlabel("Frequency (Hz)"); plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()


