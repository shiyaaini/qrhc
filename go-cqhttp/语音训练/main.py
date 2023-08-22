import os
import librosa
import numpy as np
import tensorflow as tf
from tensorflow import keras

# 加载音频数据函数
def load_data(path):
    audio, sr = librosa.load(path, sr=None)
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
    return mfccs.T

# 构建声音生成器模型函数
def build_model(input_shape):
    model = keras.Sequential([
        keras.layers.Input(shape=input_shape),
        keras.layers.Dense(256, activation='relu'),
        keras.layers.Dense(512, activation='relu'),
        keras.layers.Dense(1024, activation='relu'),
        keras.layers.Dense(2000, activation='sigmoid')
    ])
    return model

# 训练模型函数
def train(model, data_path, epochs=100):
    # 获取数据列表
    files = os.listdir(data_path)
    # 编译模型
    model.compile(optimizer='adam', loss='binary_crossentropy')
    for epoch in range(epochs):
        print('Epoch %d/%d:' % (epoch+1, epochs))
        for file in files:
            # 读取音频文件
            audio = load_data(os.path.join(data_path, file))
            # 用前一半数据来训练
            x = audio[:len(audio)//2]
            y = audio[len(audio)//2:]
            # 将输入数据归一化为[-1,1]之间
            x = np.interp(x, (x.min(), x.max()), (-1, +1))
            y = np.interp(y, (y.min(), y.max()), (-1, +1))
            # 将x和y作为模型的输入和输出，进行单步训练
            model.train_on_batch(x.reshape(1,x.shape[0],x.shape[1]), y.reshape(1,y.shape[0],y.shape[1]))
    return model

# 加载数据路径
data_path = './audio_data'

# 获取样本的MFCC特征向量长度并构建模型
sample_file = os.path.join(data_path, os.listdir(data_path)[0])
sample_mfccs = load_data(sample_file)
input_shape = sample_mfccs.shape
model = build_model(input_shape)

# 训练模型
trained_model = train(model, data_path, epochs=100)

# 保存模型
trained_model.save('sound_generator.h5')
