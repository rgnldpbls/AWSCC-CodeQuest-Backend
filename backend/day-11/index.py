with open('names.txt', 'r') as file:
    lines = file.readlines()
    names = []
    for line in lines:
        names.append(line)
        names.sort()
file.close()
with open('names.txt', 'w') as file:
    file.writelines(names)
file.close()