import xlwt

# workbook = xlwt.Workbook(encoding='utf-8')
# worksheet = workbook.add_sheet('sheet1')
# worksheet.write(0,0,'hello')
# workbook.save('student.xls')

# for i in range(9):
#     for j in range(i+1):
#         res=(i+1)*(j+1)
#         print('{}*{}={}'.format(i+1,j+1,res),end=" ")
#     print()

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet1')
for i in range(9):
    for j in range(i+1):
        res=(i+1)*(j+1)
        worksheet.write(i,j,'{}*{}={}'.format(i+1,j+1,res))
workbook.save('final.xls')





