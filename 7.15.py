file = open(input("File name: "),"r")
line_count = 0
for i in file:
    if i != "\n":
        line_count += 1
file.close()
print(f"Number of lines:{line_count}")