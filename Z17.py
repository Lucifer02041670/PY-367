#"D:\Загрузки\lorum.txt"

def r():
    file = open(file="lorum.txt", mode="r")
    print(file.read())
    file.close()

def rP():
    file = open(file="lorum.txt", mode="r+")
    print(file.read())
    file.write("123")
    file.close()

def w():
    file = open(file="lorum.txt", mode="w")
    #print(file.read())
    file.close()

def wP():
    file = open(file="lorum.txt", mode="w+")
    print(file.read())
    file.close()

def a():
    file = open(file="lorum.txt", mode="a")
    #print(file.read())
    file.close()

def aP():
    file = open(file="lorum.txt", mode="a+")
    print(file.read())
    file.close()

def main():
    r()
    rP()
    w()
    wP()
    a()
    aP()

if __name__ == "__main__":
    main()