import pandas as pd

# 读取 Excel 文件
excel_file = r'D:\科研--海洋数据分析\STGCN-main\STGCN-main\data\water_data\vel.xls'
df = pd.read_excel(excel_file)

# 将数据保存为 CSV 文件
csv_file = r'D:\科研--海洋数据分析\STGCN-main\STGCN-main\data\water_data\vel.csv'
df.to_csv(csv_file, index=False)

