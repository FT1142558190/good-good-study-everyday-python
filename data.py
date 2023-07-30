import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('data1.xlsx')

# 获取所有列名称
column_names = df.columns.tolist()

# 遍历列，每列输出一个图形
for column_name in column_names:
    # 统计值出现的次数
    value_counts = df[column_name].value_counts()

    # 创建图形对象
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(value_counts.index.astype(str), value_counts.values, marker='o', linestyle='-')
    ax.set_xlabel(column_name)
    ax.set_ylabel('Count')

    # 间隔显示X轴标签
    num_labels = 10  # 设置要显示的标签数量
    interval = max(len(value_counts.index) // num_labels, 1)  # 计算间隔值
    x_ticks = range(0, len(value_counts.index), interval)
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(value_counts.index.astype(str)[x_ticks], rotation=45, ha='right')

    # 调整子图布局
    plt.tight_layout()

    # 显示图形
    plt.show()