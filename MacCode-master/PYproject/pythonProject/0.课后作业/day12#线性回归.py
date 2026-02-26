import numpy as np
from typing import Tuple, List, Union

# 线性回归之正规方程与梯度下降的对照示例
# 为便于理解，示例使用可控的随机数据，并打印关键结果与解释


def add_bias(X: np.ndarray) -> np.ndarray:
    """在特征矩阵左侧添加常数项(截距)列"""
    ones = np.ones((X.shape[0], 1))
    return np.hstack([ones, X])


def normal_equation(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    """
    正规方程法（闭式解）：
      β̂ = (XᵀX)⁻¹ Xᵀ y
    为增强稳定性，示例使用伪逆 pinv，当 XᵀX 不可逆或病态时仍可求解近似解。
    """
    XtX = X.T @ X
    XtY = X.T @ y
    beta = np.linalg.pinv(XtX) @ XtY
    return beta


def gradient_descent(
    X: np.ndarray,
    y: np.ndarray,
    lr: float = 0.05,
    epochs: int = 1000,
    return_history: bool = False,
) -> Union[np.ndarray, Tuple[np.ndarray, List[float]]]:
    """
    梯度下降（全梯度）最小化均方误差：
      L(β) = (1/n) ∑ (y_i - x_i^T β)^2
    梯度：
      ∇β L = (2/n) Xᵀ (Xβ - y)
    参数更新：
      β ← β - lr * ∇β L
    """
    n = X.shape[0]
    beta = np.zeros(X.shape[1])
    losses = []
    for _ in range(epochs):
        pred = X @ beta
        grad = (2.0 / n) * (X.T @ (pred - y))
        beta -= lr * grad
        if return_history:
            loss = np.mean((y - pred) ** 2)
            losses.append(loss)
    return (beta, losses) if return_history else beta


def metrics(y_true: np.ndarray, y_pred: np.ndarray) -> dict:
    """计算 MSE 与 R²（拟合优度）"""
    mse = float(np.mean((y_true - y_pred) ** 2))
    var = float(np.var(y_true))
    r2 = 1.0 - (mse / var) if var > 0 else float("nan")
    return {"MSE": mse, "R2": r2}


def make_synthetic(n: int = 300, p: int = 3, seed: int = 42) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    构造可控的线性数据：
      y = β0 + β1 x1 + ... + βp xp + ε
    """
    rng = np.random.default_rng(seed)
    X = rng.normal(0, 1, size=(n, p))
    true_beta = np.array([2.0, 1.5, -0.7, 0.8])[: p + 1]  # 含截距β0
    Xb = add_bias(X)
    noise = rng.normal(0, 0.5, size=n)
    y = Xb @ true_beta + noise
    return Xb, y, true_beta


def main():
    # 1) 造数据：含截距列
    Xb, y, true_beta = make_synthetic(n=400, p=3, seed=1)

    print("【数据与目标】")
    print("- 目标：用线性模型拟合 y 与 X 的关系，学习参数 β")
    print("- 真值 β（含截距）:", true_beta)
    print()

    # 2) 正规方程（闭式解）
    beta_ne = normal_equation(Xb, y)
    y_pred_ne = Xb @ beta_ne
    m_ne = metrics(y, y_pred_ne)

    print("【正规方程法（了解）】")
    print("- 原理：直接解正规方程 (XᵀX)β = Xᵀy，得到闭式解 β̂")
    print("- 直观：一次“算出来”，不需要学习率与迭代")
    print("- 局限：高维/大样本下计算与内存开销大；XᵀX 可能病态")
    print("  学到的 β̂:", beta_ne)
    print("  评估:", m_ne)
    print()

    # 3) 梯度下降（迭代优化）
    beta_gd, losses = gradient_descent(Xb, y, lr=0.05, epochs=1500, return_history=True)
    y_pred_gd = Xb @ beta_gd
    m_gd = metrics(y, y_pred_gd)

    print("【梯度下降法（重要）】")
    print("- 原理：沿损失函数的负梯度方向迭代更新 β，以逐步逼近最优解")
    print("- 关键：学习率 lr（步长）、迭代次数 epochs、初始化与收敛判据")
    print("- 优势：可扩展到大数据/在线学习；可与正则化、批量策略结合")
    print("  学到的 β̂:", beta_gd)
    print("  评估:", m_gd)
    print(f"  迭代首尾损失: {losses[0]:.4f} -> {losses[-1]:.4f}")
    print()

    # 4) 对照总结
    diff = np.linalg.norm(beta_ne - beta_gd)
    print("【对照总结】")
    print("- 两种方法在该线性可解问题上应得到非常接近的参数与指标")
    print("- 正规方程：一步到位，但在大规模/奇异矩阵上不稳定或成本高")
    print("- 梯度下降：可迭代逼近，需选择合适学习率，可用于更复杂场景")
    print(f"- 参数差异的二范数 ||β_ne - β_gd|| = {diff:.6f}")
    print()

    # 5) 学习提示
    print("【学习提示】")
    print("- 建议先理解均方误差与梯度的推导，再动手实现更新公式")
    print("- 习惯在特征矩阵中加入截距列；实战中常对特征进行标准化")
    print("- 逐步调试：先用较小数据、较大 lr 观察发散，再减小 lr 看收敛")


if __name__ == "__main__":
    main()
