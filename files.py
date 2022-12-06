# with open('data.txt') as f:
#     lines = f.readline()
#     f.close()

# print(lines)
# with open('data.txt', 'w') as f:
#     # lines = f.readlines()
#     f.close()

# with open('data.txt', 'w+') as f:
#     f.write("Test")
#     f.close()

# with open('data.txt', 'a') as f:
#     f.write("4. Adam Slodowy")
#     f.close()

# with open('data_new.txt', 'a') as f:
#     f.write("4. Adam Slodowy")
#     f.close()


# for line in lines:
#     print(line)


# try:
#     print(6/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

try:
    with open('adata.txt') as f:
        lines = f.readline()
        
except FileNotFoundError:
    print("adata.txt does not exist!")

finally:
    print("Finally block!")




