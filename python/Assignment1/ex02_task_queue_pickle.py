import math
import pickle
import os
from sys import orig_argv


class ComputeTask:
    def __init__(self, task_id: int, operation: str, input_value: int):
        self.task_id = task_id
        self.operation = operation
        self.input_value = input_value
        self.result = None

    def execute(self) -> None:
        if self.operation == "square":
            self.result = self.input_value ** 2
        elif self.operation == "Cube":
            self.result = self.input_value ** 3
        elif self.operation == "Factorial":
            self.result = math.factorial(self.input_value)
        else:
            print("default")

    def __repr__(self) -> str:
        return (
              f"ComputeTask id = {self.task_id}, "
              f"op = { self.operation}, "
              f"result is = {self.result }" )


def main():
    filename="task_queue.pkl"
    tasks = [ ComputeTask(1, "square", 5),  ComputeTask(2, "Cube", 2),
              ComputeTask(3,"Factorial", 5), ComputeTask(4, "square", 133),
              ComputeTask(5,'Cube', 9)]

    for i in tasks[:2]:
        i.execute()

        print(i.result)

    with open('task_queue.pkl','wb') as f:
        pickle.dump(tasks,f)

    with open('task_queue.pkl', 'rb') as f:
        data  = pickle.load(f)

    print("unpickled data = ",data)

    for i in tasks[2:]:
        i.execute()
    print(tasks[2:])


if __name__ == "__main__":
    os.remove('task_queue.pkl')
    main()
