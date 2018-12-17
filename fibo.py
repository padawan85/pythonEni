import os

def fibo(limit):
    res = 0
    x   = 0
    y   = 1
    while y <= limit:
        res = x + y
        print str(x) + " + " + str(y) + " = " + str(res)
        x   = y 
        y   = res

def main():
    os.system('cls')
    print """
    +--------------------------------------------+
    |   ____  __  ____   __     ____     __      |
    |  (  __)(  )(  _ \\ /  \\   (___ \\   /  \\     |
    |   ) _)  )(  ) _ ((  O )   / __/ _(  0 )    |
    |  (__)  (__)(____/ \\__/   (____)(_)\\__/     |
    |                                            |
    |  > Author:  Glenn Le Gac                   |
    +--------------------------------------------+
    """
    fibo(int(raw_input("Limit: ")))

main()
