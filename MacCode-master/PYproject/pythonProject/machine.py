import tensorflow as tf
from keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from keras.utils import to_categorical
from keras.callbacks import EarlyStopping, ReduceLROnPlateau

# 1. 加载数据（以 MNIST 为例）
(x_train, y_train), (x_val, y_val) = tf.keras.datasets.mnist.load_data()

# 2. 预处理：展平图像（28x28 → 784）
x_train = x_train.reshape(-1, 784).astype('float32') / 255.0
x_val = x_val.reshape(-1, 784).astype('float32') / 255.0

# 3. 标签转 one-hot 编码
y_train = to_categorical(y_train, num_classes=10)
y_val = to_categorical(y_val, num_classes=10)

# 4. 构建模型
model = Sequential([
    Dense(128, activation='relu', input_shape=(784,)),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dropout(0.3),
    Dense(10, activation='softmax')
])

# 5. 编译
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 6. 回调
callbacks = [
    EarlyStopping(patience=5, restore_best_weights=True),
    ReduceLROnPlateau(factor=0.5, patience=3)
]

# 7. 训练
model.fit(x_train, y_train,
          validation_data=(x_val, y_val),
          epochs=50,
          batch_size=32,
          callbacks=callbacks)