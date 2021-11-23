print("podaj dłogości boków trójkąta: ")
a = float(input())
b = float(input())
c = float(input())
p = (a+b+c)/2
P = (p*(p-a)*(p-b)*(p-c))**(1/2)
print("Pole trójkąta wynosi {}".format(P))

