## Context
目标：预测与评估城市交通状况（low/normal/high/heavy），并分析交通流量影响因素。数据包含时间、日期、星期、各类车辆计数（Car/Bike/Bus/Truck）、Total、Traffic Situation。痛点：交通呈现强不确定性与时段性，传统线性模型难以捕捉非线性与时序依赖。

## Key Insight
时间序列任务上，LSTM优于传统机器学习与浅层神经网络；非时序特征下，树模型与集成方法（RF、XGBoost）在准确率与稳定性上表现突出。CarCount、TruckCount是关键特征。

## Method
### Architecture
- 数据处理：数值化Traffic指标，剔除日期等与实验无关特征；归一化；训练/测试随机划分（示例7:3）；交叉验证不同训练集比例。
- 相关性分析：采用皮尔逊相关系数评估变量线性相关性，提示日期与交通呈非线性关系。
- 模型集合：
  - 线性回归（LR）用于连续目标回归
  - 逻辑回归（LogReg）用于分类（low/normal/high/heavy）
  - 随机森林（RF），基于树的集成
  - 极端梯度提升（XGBoost），多弱学习器提升
  - 神经网络：BP（反向传播）、RNN（循环）、LSTM（长短期记忆）
- 评价指标：Accuracy、MSE、Loss、R²；并对分类任务计算混淆矩阵。

### Key Equations
- LSTM/RNN 以序列建模实现时序依赖；
- 皮尔逊相关系数用于线性相关性度量；
- XGBoost/RF 通过树分裂学习非线性关系与交互项。

## Results
| 模型 | Test Accuracy | Test MSE | 备注 |
|------|---------------|----------|------|
| LSTM | 0.9882        | 0.0095   | 时间序列上表现最佳 |
| RNN  | 0.9843        | 0.0224   | MSE稳定 |
| BP   | 0.9787        | 0.0314   | 均衡但误差较高 |
| XGBoost | 0.9989     | 0.0011   | 非时序下准确率与误差俱优 |
| RF   | 0.9972        | 0.0062   | 稳定、较低误差 |
| LR   | R²≈0.65       | 0.2919   | 线性拟合力不足 |
| LogReg | 0.8891      | 1.8763   | 分类基线 |

- 交叉验证：随训练比例增大，XGBoost/RF准确率与MSE持续优化；LSTM在高比例时MSE下降明显。
- 特征重要性：CarCount、TruckCount影响显著；树模型对特征敏感度与稳定性较好。

## Takeaways
- 时序任务：优先使用LSTM；若数据量有限，可考虑RNN/BP作为备选。
- 非时序/特征工程充分：XGBoost与RF具有强鲁棒性与高精度。
- 指标选取：分类用Accuracy与混淆矩阵；回归用MSE，辅以R²衡量拟合解释力。
- 特征选择：优先关注CarCount、TruckCount；日期等可能与交通呈非线性，应避免直接线性建模。
- 过拟合提示：训练优于测试，需正则化、早停与交叉验证。

## Open Questions
- 外部因素融合：天气、节假日、事件对交通的交互影响如何建模（多源异构融合）？
- 空间相关性：路网拓扑与相邻路段流量的时空耦合（如图卷积、时空图网络）。
- 部署与实时性：在线更新与概念漂移的适配策略。

## Related Papers
- 时空数据分析关键技术（智能交通）
- 基于有向图卷积神经网络的交通预测与拥堵管控
- Traffic flow forecasting with deep learning
- 基于机器学习的交通流预测方法综述
- Congestion prediction for smart sustainable cities using IoT and ML
