#矩阵初始化函数
def genMatrix(rows,cols):
    #用二维数组来代表矩阵
    matrix = [[0 for col in range(cols)] for row in range(rows)]
    for i in range(rows):
        for j in range(cols):
            matrix[i][j]
    return matrix

#构造蛇形填数函数
def testSnake():
    #调用genMatrix函数
    matrix = genMatrix(number, number)
    i = j = 0
    total = matrix[i][j] = 1
    while(total < number * number):
        #向右填数
        while(j + 1 < number and matrix[i][j + 1] == 0):
            total += 1
            j += 1
            matrix[i][j] = total
        #向下填数
        while(i + 1 < number and matrix[i + 1][j] == 0):
            total += 1
            i += 1
            matrix[i][j] = total
        #向左填数
        while(j > 0 and matrix[i][j - 1] == 0):
            total += 1
            j -= 1
            matrix[i][j] = total
        #向上填数i
        while(i + 1 > 0 and matrix[i - 1][j] == 0):
            total += 1
            i -= 1
            matrix[i][j] = total
    #打印显示
    for i in range(number):
            for j in range(number):
                print ('\t%d ' % matrix[i][j], end=''),
                #python2.X版本用print()后面加上逗号来不换行
                #python3.X版本的打印不换行可用print ('\t%d ' % matrix[i][j], end='')
            print('\n')

#主流程控制
while True:
    number = int(input("Please Input your number:"))
    if(number <= 0):
        print("请输入大于0的整数")
        continue
    testSnake()
    flag = input("Do you want to continue? Y/N").strip()
    #字符串的strip()是为了去除命令行输入前后的空格
    if(flag.__eq__("Y")):
        continue
    break
