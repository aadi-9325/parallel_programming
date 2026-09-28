"""All thread share the same PID (process ID)
Each thead has a unique TID ()
"""
import threading
import time
from time import sleep


def do(name):
    for i in range(100_00):
        print(name, end = " ")
        print(i, end ="\t")
        sleep(.25)

def main():
    # do("aditya")
    # do("sohel")
    t1 = threading.Thread(target=do, args=["aditya"])
    t2 = threading.Thread(target=do, args=["sohel"])
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()