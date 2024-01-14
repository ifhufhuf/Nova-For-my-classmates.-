import os
from colorama import Back, Fore, Style, init
import colorama  
import func
  
# 初始化colorama，这将使得ANSI转义序列在Windows上也能工作  
init(autoreset=True)  # 设置为True，以便在每次使用后自动重置颜色 
  
# 设置背景颜色为淡蓝色（如果colorama支持的话）  
# 注意：colorama可能不直接支持淡蓝色，你可能需要选择一个接近的颜色  
# print(Back.LIGHTBLUE_EX + "This text has a light blue background!")  
# 如果LIGHTBLUE_EX不可用，你可以尝试使用其他颜色或者自定义RGB值（如果colorama支持的话）
o = open(".\\src\\hello.txt",'r',encoding="utf-8")
print(Fore.LIGHTGREEN_EX + o.read())
o.close()
while True:
    zl = input(Fore.LIGHTBLUE_EX + "✨ ~>")
    x = zl.split()
    if x[0] == "help":
        o = open(".\\src\\help.help",'r',encoding="utf-8")
        print(Fore.LIGHTGREEN_EX + o.read())
        o.close()
    elif x[0] == "run":
        文件后缀 = x[1].split('.')[1]
        print(f"💠File extension: {文件后缀}")
        if 文件后缀 == "java":
            os.system(f"java {x[1]}")
        elif 文件后缀 == "py":
            os.system(f"python {x[1]}")
        elif 文件后缀 == "lua":
            os.system(f"lua {x[1]}")
    elif x[0] == "out":
        o = open(".\\src\\b.txt",'r',encoding="utf-8")
        print(Fore.LIGHTCYAN_EX + o.read())
        exit()
    elif x[0] == "d-run":
        文件后缀 = x[1].split('.')[1]
        print(f"💠File extension: {文件后缀}")
        if 文件后缀 == "java":
            func.find_main(x[1],'java')
        elif 文件后缀 == "py":
            func.find_main(x[1],'py')
        elif 文件后缀 == "lua":
            func.find_main(x[1],'lua')
    elif x[0] == "app":
        app_name = x[1]
        os.system(f".\\src\\python12\\python.exe .\\app\\{app_name}.py")
    elif x[0] == "using":
        key = input("key:")
        print(Fore.BLACK + "ing...") 
        if key == "114514":
            os.system(f".\\src\\python12\\python.exe .\\src\\using\\{x[1]}.py")
        else:
            print(f"ERROR:" + Fore.LIGHTRED_EX + f"{zl}")
    else:
        print(f"unknown instruction:" + Fore.LIGHTRED_EX + f"{zl}")
         