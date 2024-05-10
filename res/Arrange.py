def getSerialList(targerfile):
    """
    根据正文交叉引用返回参考文件顺序序列
    """
    serial_list = []
    targerfilec = open(targerfile, 'r')
    targerfile = targerfilec.read()
    in_square_bracket = False

    for i in targerfile:
        
        if in_square_bracket and i.isdigit(): 
            serial += i      # 扫描数字
        
        if i.isdigit() == False and i != ']':
            in_square_bracket = False      # 中断识别

        if i == '[':
            in_square_bracket = True      # 遇到方括号开始识别
            serial = ''

        elif i == ']' and in_square_bracket and serial != '':
            in_square_bracket = False          # 遇到反方括号终止识别
            serial_list.append(int(serial))     # 收纳引用序号
    targerfilec.close()


    return serial_list



def sortpaper(serialList, re_file):
    """
    根据序列修改参考文献顺序创造新文件
    """
    re_filec = open(re_file, 'r')       # 参考文献文件
    re_file = re_filec.readlines()
    compled_file = open('compled_file.txt', 'w')      # 排序后参考文件
    compled_text = ''
    for i in serialList:
        state = False       # 状态机
        for j in re_file[i-1]:
            if state:
                compled_text += j           # 采集字符
            if j == ']':
                state = True       # 遇到反方括号就开始采集字符
    
    print(compled_text)

    compled_file.write(compled_text)  # 写入文件



serialList = getSerialList('TargetFile.txt')
print([i+1 for i in range(len(serialList))])
print(serialList)
sortpaper(serialList, 're_file.txt')   # 启动启动，嘿嘿嘿!!!