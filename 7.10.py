file = open("me.txt", "w")
file.write("Lukasz Checiak\nUniwersytet ekonomiczny w Krakowie\nInformatyka stosowana")
file.close()

file = open("me.txt", "r")
print(file.read())