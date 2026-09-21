import threading
import os
import time

num = int(input("Enter a number:"))
print(f"\n{threading.current_thread().name}")
def check_even(n):
    if n%2 == 0:
        print(f"{n} is even")
        time.sleep(10)
        print(f"\n{threading.current_thread().name}")
    else:
        print(f"{n} is odd")

def rename_func():
    print(f"\n{threading.current_thread().name}")
    os.rename("D:/my_pic.PNG","D:/pic.PNG")
    
t1 = threading.Thread(target = check_even, args=(num,))
t2 = threading.Thread(target = rename_func)

t1.start()
t2.start()

t1.join()
t2.join()
