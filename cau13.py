a=int(input("nhap gia tri:"))
b=int(input("nhap gia tri:"))
c=int(input("nhap gia tri:"))
d=b*b-(4*a*c)
if d>0:
    x1=(-b-sqrt(d))/2*a
    print("gia tri x1:",x1)
    x2=(-b+sqrt(d))/2*a
    print("gia tri x2:",x2)
if d==0:
    x1=x2=-b/2*a
    print("gia tri x1,x2:",x1,x2)
if d<0:
    print("vo nghiem")


