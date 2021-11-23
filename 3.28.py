first_number = 0
second_number = 1
i = 15
print(first_number)
print(second_number)
for z in range(i):
    print(first_number+second_number)
    first_number +=second_number
    print(second_number+first_number)
    second_number +=first_number