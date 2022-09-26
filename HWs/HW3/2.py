file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

file1lines = file1.readlines()
file2lines = file2.readlines()

print(file2lines)

with open("file3.txt", "x") as f:
    for i in range(max(len(file1lines), len(file2lines))):
        if i < len(file1lines): f.write(file1lines[i]) 
        if i < len(file2lines): f.write(file2lines[i]) 



file1.close()
file2.close()