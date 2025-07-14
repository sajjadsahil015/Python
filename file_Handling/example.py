with open("example.txt","w") as file:
    file.write("First line\n")
    file.write("second line\n")
    file.writelines(["Third line\n","Fourth line"])

with open("example.txt","r") as file:
    content=file.read()
    print(content)
with open("example.txt","r") as file:
    for line in file:
        print(line,end="")
    file.seek(0)
    print(file.readline())
with open("my_file.txt","r") as file:
    contnt= file.readlines()
    for lines in contnt:
        print(lines,end="")
with open("new_file.txt","a") as file:
    file.write("this is appended line")

