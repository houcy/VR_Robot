y=int(input("请输入"))
if(y%400==0):print("Y")
else:
    if(y%4==0):
        if(y%100==0):
            print("N")
        else:
            print("Y")
    else:
        print("N")
input()