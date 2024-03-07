import os

print(" ____ ___ ____  ______   __")
print("|  _ \_ _|  _ \|  _ \ \ / /")
print("| |_) | || |_) | |_) \ V / ")
print("|  __/| ||  __/|  __/ | | ")
print("|_|  |___|_|   |_|    |_|  ")

def upgrade():
    os.system("pip install --upgrade pip")
    
def install():
    install = input("Что вы хотите установить?")
    os.system("pip install " + install)
    
def uninstall():
    uninstall = input("Что вы хотите удалить?")
    os.system("pip uninstall "+ uninstall)
    
    
def start():
    start = input("Добро пожаловать в pippy!\nЧто вы хотите сделать?\n1 - Обновить pip\n2 - Установить пакет\n3 - удалить пакет\n4 - Поменять язык\n5 - Выйти\n")    
    if(start == "1"):
        upgrade()        
    if(start == "2"):
        install()
    if(start == "3"):
        uninstall()
    if(start == "4"):
        os.system("python pippy.py")
    if(start == "5"):
        quit()
    

start()
