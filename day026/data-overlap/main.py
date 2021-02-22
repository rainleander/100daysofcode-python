file1 = open("file1.txt", "r")
file1_list = file1.read().splitlines()

file2 = open("file2.txt", "r")
file2_list = file2.read().splitlines()

result = [int(x) for x in file1_list if x in file2_list]

# Write your code above 👆

print(result)
