
import pandas as pd

def Read_data(file):
 dt=pd.read_excel('201404070532-20230716-213836(1).xlsx')
 dt.columns=['time']
 data=dt
 pd.set_option('display.max_rows', None)
 pd.set_option('display.max_columns', None)
 pd.set_option('display.width', None)
 pd.set_option('display.unicode.ambiguous_as_wide', True)
 pd.set_option('display.unicode.east_asian_width', True)
 print(data.head())
 return data
def data_clean(data):
 print('存在'if any(data.duplicated()) else'不存在',data.drop_duplicates())
 print(data.isnull())
 print(data.isnull().sum())
 print(data.isnull().T.sum())
 print('不存在'if any(data.isnull())else'cunzai','缺失值')
 data.dropna()
 data.fillna(method='ffill')
 data.fillna(method='bfill')
 data.fillna(value=2)
 data.fillna(value={'':data[''].mean()})
 data1=data['']
 xmean=data1.mean()
 xstd=data1.std()
 print('cunzai'if any(data1>xmean+2*xstd)else'不存在','上限异常值')
 print('cunzai' if any(data1 > xmean + 2 * xstd) else '不存在', '下限异常值')
 q1=data1.quantile(0.25)
 q3=data1.quantile(0.75)
 up=q3+1.5*(q3-q1)
 dw= q1 - 1.5 * (q3 - q1)
 print('存在'if any(data1>up)else'不存在','上限异常值')
 print('存在'if any(data1<dw)else'不存在','下限异常值')
 data1[data1>up]=data1[data1<up].max()
 data1[data1<dw]=data1[data1>dw].min()
 print(data1)