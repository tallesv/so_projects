import os
import random
import threading
import time
import mmap
import signal
import posix_ipc
import sys
import struct


def generate_matrix(line=2, column=2):
    i, j = line, column
    return [[random.randint(0, 9) for x in range(i)] for y in range(j)]


def func(index, value_one, value_two):
    # print(f"Thread {index}: starting")
    global res
    res.append(value_one + value_two)
    # time.sleep(2)
    # print(f"Thread {index}: finishing")


def func_proc(value_one, value_two):
    # print(f"Thread {index}: starting")
    # print(value_one + value_two)
    return value_one + value_two


def unroll_with_thread(args, func):
    threads = []
    for index, arg in enumerate(args):
        # print(f"Main    : create and start thread {index}.")
        thread = threading.Thread(target=func, args=(index, *arg))
        threads.append(thread)
        thread.start()

    for index, thread in enumerate(threads):
        # print(f"Main    : before joining thread {index}.")
        thread.join()
        # print(f"Main    : thread {index} done.")


def create_mapped_memory():
    memory = posix_ipc.SharedMemory("test", flags=posix_ipc.O_CREAT, mode=0o777, size=50)
    mapped_memory = mmap.mmap(memory.fd, memory.size)
    memory.close_fd()
    return mapped_memory


def read_mapped_memory():
    memory_read = posix_ipc.SharedMemory("test")
    mapped_memory_read = mmap.mmap(memory_read.fd, memory_read.size)
    memory_read.close_fd()
    return mapped_memory_read


def unroll_with_process(args, func):
    pid = None
    mapped_memory = create_mapped_memory()
    mapped_memory.seek(0)
    for index, arg in enumerate(args):
        pid = os.fork()
        if pid == 0:
            result = func_proc(*arg)
            print(result)

            mapped_memory.write(struct.pack("i", result))
            os._exit(0)

    if pid and pid != 0:
        time.sleep(2)

        mapped_memory.seek(0)

        for i in range(4):
            val_bytes = mapped_memory.read(4)
            value = struct.unpack("i", val_bytes)[0]
            print(f"list[{i}]: {value}")
        mapped_memory.close()


def unroll(args, func, method, results):
    if method == "thre":
        unroll_with_thread(args, func)
    elif method == "proc":
        unroll_with_process(args, func)
    else:
        print("OPÇÃO NÃO INDISPONÍVEL!")


if __name__ == "__main__":
    res = []
    matrix_one = generate_matrix()
    matrix_two = generate_matrix()

    matrix_unroll = []
    for i in range(len(matrix_one)):
        for j in range(len(matrix_one[0])):
            matrix_unroll.append([matrix_one[i][j], matrix_two[i][j]])

    # for i in range(len(X)):
    #    for j in range(len(Y[0])):
    #        for k in range(len(Y)):
    #            result[i][j] += X[i][k] * Y[k][j]

    # multiply
    # 00  01
    # 10  11

    # A = [[1, 2],
    #      [3, 4]]

    # B = [[-1, 3],
    #      [4, 2]]

    # R[0,0] = (A[0,0] * B[0,0]) + (A[0,1] * B[1,0])

    # R[0,1] = (A[0,0] * B[0,1]) + (A[0,1] * B[1,1])

    # R[1,0] = (A[1,0] * B[0,0]) + (A[1,1] * B[1,0])

    # R[1,1] = (A[1,0] * B[0,1]) + (A[1,1] * B[1,1])

    # print(matrix_unroll)
    # unroll([[1, 3], [2, 4], [2, 4], [1, 3]], func, "thre", res)
    # unroll(matrix_unroll, func, "thre", res)
    print(matrix_unroll)
    unroll(matrix_unroll, func, "proc", res)
    # print(res)
