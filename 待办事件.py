import os
import json

def check_file_exists_in_folder(folder_path, file_name):
    full_path = os.path.join(folder_path, file_name)
    return os.path.isfile(full_path)

# 使用示例
target_folder = os.path.abspath('.').replace('/', '\\')
file_to_check = "op.txt"
opp = target_folder + "\\" + "op.txt"

if check_file_exists_in_folder(target_folder, file_to_check):
    with open(opp,'r',encoding='utf-8') as file:
        try:
            op = json.load(file)
        except:
            op = []
else:
    op = []
    with open(opp,'w',encoding='utf-8') as file:
        json.dump(op,file)

while True:
    x = str(input('请选择你的操作(1.添加待办事项 2.查看待办事项 3.删除待办事项 4.退出)'))
    if x == '4':
        exit()
    elif x == '2':
        if len(op) == 0:
            print('没有待办事项')
        else:
            for i in range(len(op)):
                print(op[i])
    elif x == '1':
        jop = str(input('请输入待办事项(什么都不输取消)'))
        if jop == '' or jop.isspace():
            print('已取消')
        else:
            op.append(jop)
            with open(opp,'w',encoding='utf-8') as file:
                json.dump(op,file)
            print('添加成功')
    elif x == '3':
        if len(op) == 0:
            print('没有待办事项')
        else:
            while True:
                for i in range(len(op)):
                    print(op[i],i + 1,sep='   ')
                print('全部删除   a')
                print('取消   其他')
                dela = str(input('请输入待办事项序号'))
                l = str(len(op))
                if dela.isdigit() and dela > '0' and dela <= l:
                    dela = int(dela)
                    op.pop(dela - 1)
                    with open(opp,'w',encoding='utf-8') as file:
                        json.dump(op,file)
                    print('删除成功')
                    break
                elif dela == 'a':
                    xx = str(input('你确定要删除全部待办事项吗?(y/n)'))
                    if xx == 'y':
                        op = []
                        with open(opp,'w',encoding='utf-8') as file:
                            json.dump(op,file)
                        print('删除成功')
                        break
                    else:
                        print('已取消')
                else:
                    print('已取消')
                    break
    else:
        print('输入错误')
