a=int(input("inter mark eng"))
b=int(input("inter mark it"))
c=int(input("inter mark bk"))
d=int(input("inter mark oc"))
f=int(input("inter mark sp"))
percentage=(a+b+c+d+f)*100/500
if (percentage>90):
    print("f.c")
elif((percentage>80) and(percentage<89)):
    print("s.c")
elif((percentage>70) and(percentage<79)):
    print("t.c")
elif((percentage>60) and(percentage<69)):
    print("fail")
else:
    print("fail")

     

