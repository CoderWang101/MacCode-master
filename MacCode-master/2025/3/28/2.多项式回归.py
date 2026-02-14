### 1.数据准备
import numpy as np
import matplotlib.pyplot as plt

x= np.random.uniform(-3, 3, size=100)
X=x.reshape(-1, 1)
y=0.5*x**2+x+2+np.random.normal(0, 1, size=100)
#数据中加入噪声
plt.scatter(x, y)
plt.show()

### 2.线性回归
from sklearn.linear_model import LinearRegression

lin_reg=LinearRegression()
lin_reg.fit(X, y)
y_pred=lin_reg.predict(X)
plt.rcParams['font.family']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.title('LinearRegression')
plt.scatter(x, y)
plt.plot(x, y_pred, color='red')
plt.show()

### 3.多项式回归
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

poly=PolynomialFeatures(degree=2)
#设置最多添加几次幂的特征
poly.fit(X)
x2=poly.transform(X)
lin_reg2=LinearRegression()
lin_reg2.fit(x2, y)
y_pred2=lin_reg2.predict(x2)
plt.scatter(x, y)
plt.plot(np.sort(x), y_pred2[np.argsort(x)], color='red')
plt.title('PolynomialRegression')