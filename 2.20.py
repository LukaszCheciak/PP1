print("Podaj swoją wagę w kg: ")
w = float(input())
print("podaj swój wzrost w cm: ")
x = float(input())
b = w/(x/100)**2
print("Twoje BMI wynosi {}".format(b))
