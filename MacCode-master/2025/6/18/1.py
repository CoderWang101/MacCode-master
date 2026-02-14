from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

#加载葡萄酒数据集
wine = load_wine()

#将wine对象的data和target属性分别作为前两个参数值进行划分
Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data, wine.target, test_size=0.3)

rfc = RandomForestClassifier(random_state=0)
rfc.fit(Xtrain, Ytrain)

accuracy_r = rfc.score(Xtest, Ytest)

print("Random Forest: {}".format(accuracy_r))