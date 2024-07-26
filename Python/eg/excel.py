#pip install openpyxl

import openpyxl

# 创建一个新的 Excel 工作簿
wb = openpyxl.Workbook()

# 选择默认的工作表（第一个工作表）
sheet = wb.active

# 在单元格中写入数据
sheet['A1'] = '姓名'
sheet['B1'] = '年龄'

# 写入一些示例数据
data = [
    ('Alice', 30),
    ('Bob', 25),
    ('Charlie', 35)
]

# 将数据写入多个行
for row_idx, row_data in enumerate(data, start=2):
    sheet[f'A{row_idx}'] = row_data[0]
    sheet[f'B{row_idx}'] = row_data[1]

# 保存 Excel 文件
wb.save('example.xlsx')
print("Excel 文件已成功创建。")

