import os
import random
import threading
import time
import multiprocessing

from pip import __main__

words = ["python", "parallel", "computing" ,"process", "thread", "memory", "data", "algorithm", "performance",
         "speedup"]


file_list = [ f"file_{i}.txt" for i in range(1,6)]


def worker():
    for file_name in file_list:
        with open(f'{file_name}','w') as file:
            content = " ".join(random.choices(words, k=random.randint(5000, 10000)))
            file.write(content)

def count_words(filepath)->tuple:
    time.sleep(0.5)
    word_count = 0
    with open(filepath, 'r') as file:
        word_count = len(file.read().split())
    return filepath, word_count
# sequential run of word count


def main():
    t1 = threading.Thread(target=worker)
    t1.start()
    t2 = threading.Thread(target=worker)
    t2.start()

    t1.join()
    t2.join()

    seq_start_time = time.time()

    for file in file_list:
        print(count_words(file))

    seq_end_time = time.time()

    parr_start_time = time.time()
    with multiprocessing.Pool() as pool:
        par_results = pool.map(count_words, file_list)
    parr_end_time = time.time()

    for name, count in par_results:
        print(f"  {name}: {count} words")

    print(f"sequential time = ", (seq_end_time - seq_start_time))
    print(f"parallel time = ", (parr_end_time - parr_start_time))

if __name__ == "__main__":
    for f in file_list:
        if os.path.exists(f):
            os.remove(f)
    print("Test files deleted.")

    main()



