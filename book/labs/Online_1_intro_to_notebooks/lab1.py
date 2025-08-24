
def pyramid(x):
    y = 0
    for i in range(0, x):
        for j in range(0, i + 1):
            print("#", end="")
            y += 1
        print()
    return y
 
def mysteryCont1():
    print("/|              (\  |( ")
    print("^ \\    /____\\    /\\ |")
    print("  \\|__|      |__|  --")
    
def mysteryCont2():
    print("  '         (    . .    )")
    print(" /           \\__     __/")
    
def mystery(y):
    print("              __     __")
    print("   ________  /  \\~~~/  \\")
    mysteryCont2()
    mysteryCont1()
    return y ** 2
    
