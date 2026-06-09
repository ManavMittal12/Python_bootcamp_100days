with open("file1.txt") as file1:
    file1_list = [int(n.strip("\n")) for n in file1.readlines()]

with open("file2.txt") as file2:
    file2_list = [int(n.strip("\n")) for n in file2.readlines()]


result = [num for num in file1_list if num in file2_list]
print(result)
