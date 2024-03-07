import os

print(" ____ ___ ____  ______   __")
print("|  _ \_ _|  _ \|  _ \ \ / /")
print("| |_) | || |_) | |_) \ V / ")
print("|  __/| ||  __/|  __/ | | ")
print("|_|  |___|_|   |_|    |_|  ")

def upgrade():
    os.system("pip install --upgrade pip")
    
def install():
    install = input("What do you want to install?")
    os.system("pip install " + install)
    
def uninstall():
    uninstall = input("What do you want to uninstall?")
    os.system("pip uninstall "+ uninstall)
    
    
def start():
    start = input("Welcome to pippy!\nWhat do you want to do?\n1 - upgrade pip\n2 - install package\n3 - uninstall package\n4 - change lang\n5 - Quit\n")    
    if(start == "1"):
        upgrade()        
    if(start == "2"):
        install()
    if(start == "3"):
        uninstall()
    if(start == "4"):
        os.system("python pippyru.py")
    if(start == "5"):
        quit()
    

start()



