with open('716.txt', 'r') as firstfile, open('copylines.txt', 'a') as secondfile:
    for line in firstfile:
        secondfile.write(line)