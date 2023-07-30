import numpy as np
np.random.seed(1337)
import os
import pandas as pd
from keras import Sequential
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from keras.layers import Dense, Dropout, Conv1D, MaxPooling1D, Flatten, GRU
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution
#显示中文
# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示符号
plt.rcParams['axes.unicode_minus'] = False
#忽略警告
import warnings
warnings.filterwarnings("ignore")
#如果没有这个目录，则创建这个目录
if not os.path.isdir('result'):
    os.mkdir('result')
#本案例参数只是初步调节，仅用于学习，自己的数带入后训练过程需要不断调参才能获得较好的效果
#读取数据 datas.csv
df=pd.read_excel('train-new.xlsx')
#获取处理后的数据
data=df.values
####下面是 cnn-gru 模型预测部分
#显示原数据
# fig = plt.figure(figsize=(15, 8), dpi=80)
# plt.plot(data[:,6], label="origin data", color='b',lw=2.5) #若不需要日期或者数据没有日期可改成
# plt.plot(data[:,0], label=" ", color='b',lw=2.5),ata[:,0]表示取 close 列
# plt.title("origin data")
# plt.xticks(range(1,len(data),50),rotation=45) #为了横坐标显示清楚，通过间隔 50个显示一个值
# plt.legend()
# plt.savefig('result/origin_data.png')#图片保存路径
# plt.show()
#划分训练集和测试集长度
X=data[:,0:6]#取数据的其他特征部分,[行或行区间(:),列或列区间(:)],这里取open,high,low,vol 列
Y=data[:,6].reshape(-1,1)#取需要预测的特征 close 列并转置
data_len=len(data)#获取数据长度
train_len=int(data_len*0.70)#取 80%作为训练数据
test_len=data_len-train_len #测试集数据长度
#显示预测的特征 Y 的训练数据
fig = plt.figure(figsize=(15, 8), dpi=80)
plt.plot(Y[:train_len], label="train data", color='b',lw=2.5) #若不需要日期或者数据没有日期可改成
# plt.plot(Y[:train_len], label=" ", color='b',lw=2.5)
plt.title("origin train data")
21lt.xticks(range(1,len(Y[:train_len]),50),rotation=45) #为了横坐标显示清楚，通过间隔 50 个显示一个值
plt.legend()
plt.savefig('result/origin_train_data.png')#图片保存路径
plt.show()
