import threading


def cpu_task(n=5_000_000):
    total = 0
    for i in range(n):
