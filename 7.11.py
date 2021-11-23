array = ["Troja","Kevin sam w domu","Pasja","Patriota","Dzien swira"]
file = open("films.txt", "w")
for i in range(0,len(array)):
    file.write(array[i]+"\n")
file.close()
file = open("films.txt", "r")
print(file.read())