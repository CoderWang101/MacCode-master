from sklearn.datasets import load_iris

X=load_iris().data
y=load_iris().target
print('前8条数据:\n',X[:8])
print('前8条数据的标签(类型):\n',y[:8])

#划分数据集并进行归一化
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)   
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)
print('训练集前8条数据:\n',X_train[:5])

#训练模型并对测试集进行预测
from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression(random_state=0)
classifier.fit(X_train,y_train)
y_pred=classifier.predict(X_test)
#用逻辑回归自带的评估score()函数进行评估准确性
print('逻辑回归模型的准确率:%3f'%(classifier.score(X_test,y_test)))