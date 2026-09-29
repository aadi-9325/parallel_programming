import threading
import os
import  time

import  random
from time import sleep

'''4. Create one thread per row (5 threads total) that each computes one row of the result matrix.
5. Start all threads, join them, and print the result matrix.

6. Verify correctness by computing the same result sequentially and comparing.'''


matrix_a  = [[ random.randint(1,10)  for _ in range(5)] for _ in range(5)]
matrix_b = [[ random.randint(10,20)for _ in range(5)] for _ in range(5) ]

result = [ [0]*5 for _ in range(5) ]

def add_row(a, b, result, row_index):
    sleep(1)
    result [row_index] = [a[row_index][i] + b[row_index][i] for i in range(len(a[row_index]))]


def main():
    print("Matrix A:", matrix_a)
    print("Matrix B:", matrix_b)
    def parallel():
        start = time.time()
        threads = [  threading.Thread(target=add_row, args=(matrix_a,matrix_b,result,i))
                     for i in range(len(matrix_a)) ]
        print("\nStarting threads...")
        for i in threads: i.start()
        for i in threads: i.join()
        print("Threaded Result Matrix:", result)
        print("parallel compute time = ", time.time() - start)

    def serial():
        start = time.time()
        for i in range(len(matrix_a)):
            add_row(matrix_a, matrix_b,result,i)
        print("Threaded Result Matrix:", result)
        print("serial compute time = ", time.time() - start)

    parallel()
    serial()



add_row(matrix_a,matrix_b,result,1)

if __name__ == "__main__":
    main()