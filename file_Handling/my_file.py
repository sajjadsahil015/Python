file = open("new_file.txt","w")

file.write("new line\n")
file.write("another line\n")
file.close()

lines = ["first_line:karachi\n","second line:skardu\n"]
file = open("new_file.txt","a")
file.writelines(lines)
print(file.tell())
file.close()

file = open("new_file.txt","r")
content = file.read()
# print(content)

file.seek(0)

lines = file.readlines()
for line in lines:
    print(line)
for line in lines:
    print(line.strip())
file.close()

try:
    file = open("my_file.txt","x")
    file.write("hello world\n")
    print("file successfully created!")
except FileExistsError:
    print("file already exists")

with open("my_file.txt","r") as file:
    print(file.tell())
    while True:
        content = file.read(10)
        if not content:
            print("end of content")
            break
        print(content)
    print(file.tell())
    file.seek(0)
    print(file.tell())

with open("new_file.txt","rb") as file:
    print("Tell",file.tell())
    file.seek(4)
    print("Tell",file.tell())

    file.seek(2,1)
    print("Tell",file.tell())

    file.seek(-4,2)
    print("Tell",file.tell())

def copy_file(source_path,destination_path):
    try:
        with open(source_path,"r") as source_file,open(destination_path,"w") as dest_file:
            for line in source_file:
                dest_file.write(line)
        print(f"{source_path} successfully copied to {destination_path}")
    except FileNotFoundError:
        print(f"Error: {source_path} not found")
    except Exception as e:
        print(f"Error: found error during copying.{e}")

copy_file("my_file.txt","unique_file.txt")