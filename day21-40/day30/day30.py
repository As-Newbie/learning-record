# ✏️ 今日练习题
# 题目1：矩阵基础
# 创建矩阵 A = [[2, 1], [1, 3]] 和向量 b = [1, 2]。
# 计算 A @ b 的结果。
# 用 np.linalg.solve 解方程组 Ax = b。
# 题目2：矩阵性质
# 计算 A 的行列式。
# 求 A 的逆矩阵，并验证 A @ A_inv 是否接近单位矩阵。
# 题目3：特征分解
# 计算 A 的特征值和特征向量。
# 验证：A @ v ≈ λ * v 是否成立（选一个特征向量）。
# 题目4（进阶）：奇异值分解
# 对 A 做 SVD 分解。
# 验证 U @ np.diag(S) @ Vt ≈ A 是否成立。
import numpy as np
print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目1开始∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
A=np.array([[2,1],[1,3]])
b=np.array([1,2])
# 计算A@b
a1=A@b
print(f"计算A@b的结果是\n{a1}")
x1=np.linalg.solve(A,b)
# 用 np.linalg.solve 解方程组 Ax = b。
print(f"解方程组 Ax = b的结果是x={x1}")
print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目1结束∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目2开始∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
# 计算 A 的行列式
det_A=np.linalg.det(A)
print(f"计算 A 的行列式的结果是\n{det_A}")
# 求 A 的逆矩阵，并验证 A @ A_inv 是否接近单位矩阵
A_inv=np.linalg.inv(A)
print(f"计算 A 的逆矩阵的结果是\n{A_inv}")
# 验证A @ A_inv是否接近单位矩阵
identity_check = A @ A_inv
print("A @ A_inv的结果:\n", identity_check)
# 检查是否接近单位矩阵（考虑浮点误差）
is_identity = np.allclose(identity_check, np.eye(2))
print("A @ A_inv是否接近单位矩阵:", is_identity)
print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目2结束∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目3开始∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
# 计算 A 的特征值和特征向量
vals, vecs = np.linalg.eig(A)
# 设置全局浮点数显示精度（例如保留 4 位小数）
np.set_printoptions(precision=4, suppress=True, floatmode="fixed")
# suppress=True 防止科学计数法
# floatmode="fixed" 强制显示固定位数（包括末尾的 0）
print(f"矩阵 A 的特征是是\n{vals}\n特征向量是\n{vecs}")
# 验证：A @ v ≈ λ * v 是否成立（选一个特征向量）
# 选择第一个特征值和特征向量进行验证
lambda1 = vals[0]
v1 = vecs[:, 0]
# 计算 A @ v1 和 λ1 * v1
Av1 = A @ v1
lambda_v1 = lambda1 * v1
print(f"\n选择第一个特征值 λ1 = {lambda1:.4f} 和对应特征向量:")
print("v1 =", v1)
print("A @ v1 =", Av1)
print("λ1 * v1 =", lambda_v1)
print("误差 A @ v1 - λ1 * v1 =", Av1 - lambda_v1)
print("验证是否接近零向量:", np.allclose(Av1, lambda_v1))
print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目3结束∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目4开始∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
U, S, Vt = np.linalg.svd(A)
print("U 矩阵:\n", U)
print("奇异值 S:", S)
print("Vt 矩阵:\n", Vt)
# 验证 U @ np.diag(S) @ Vt ≈ A
A_reconstructed = U @ np.diag(S) @ Vt
# 如果矩阵是非方阵，np.diag(S) 维度可能对不上。
# 更通用的写法是：
# Sigma = np.zeros_like(A, dtype=float)
# np.fill_diagonal(Sigma, S)
# A_reconstructed = U @ Sigma @ Vt
print("\n重构的矩阵 U @ diag(S) @ Vt:\n", A_reconstructed)
print("原始矩阵 A:\n", A)
print("误差矩阵 A_reconstructed - A:\n", A_reconstructed - A)
print("验证是否接近原始矩阵:", np.allclose(A_reconstructed, A))
# 验证了第一个特征值和特征向量，也可以加个循环批量验证所有：
# for i in range(len(vals)):
#     v = vecs[:, i]
#     print(f"验证特征值 {vals[i]:.4f}")
#     print("误差 =", np.linalg.norm(A @ v - vals[i] * v))
print(f"∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷题目4结束∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
