file = open("shoplist.txt","a")
file2 = open("MeatAndFish.txt","r")
file3 = open("GrainsAndBread.txt","r")
file = file2 + file3
print(file)
file.close()
file2.close()
file3.close()