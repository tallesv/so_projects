import os
import random
import threading
import time
import mmap
import signal
import posix_ipc
import sys
import struct


def generate_matrix(line, column):
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
    aux = []
    global res
    mapped_memory = create_mapped_memory()
    mapped_memory.seek(0)
    mapped_memory_read = read_mapped_memory();
    for index, arg in enumerate(args):
        pid = os.fork()
        if pid == 0:
            result = func_proc(*arg)
            #print(result)

            mapped_memory.write(struct.pack("i", result))
            os._exit(0)

        if pid and pid != 0:
            time.sleep(2)

            mapped_memory_read.seek(0)

            val_bytes = mapped_memory_read.read(4)
            value = struct.unpack("i", val_bytes)[0]
                #print("list[%d]: %d" %(i, value))
            res.append(value)
        
    mapped_memory_read.close()
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
    matrix_one = generate_matrix(3,3)
    matrix_two = generate_matrix(3,3)

    matrix_unroll = []
    for i in range(len(matrix_one)):
        for j in range(len(matrix_one[0])):
            matrix_unroll.append([matrix_one[i][j], matrix_two[i][j]])


    start_time = time.time()
    unroll(matrix_unroll, func, "thre", res)
    tempo = time.time() - start_time      
    print('tempo : %d' %tempo)

    for i in matrix_one:
        print(i)
    print("")
    for i in matrix_two:
        print(i)        
    print("")
    print(res)
    


    '''
    res = []
    tamanho = [2, 3, 4, 5, 6, 8, 10, 20, 30, 40, 50, 75, 100]

    tempo_soma = []
    tempo_mult = []

    for k in range(len(tamanho)):

        matrix_one = generate_matrix(tamanho[k],tamanho[k])
        matrix_two = generate_matrix(tamanho[k],tamanho[k])

        matrix_unroll = []
        for i in range(len(matrix_one)):
            for j in range(len(matrix_one[0])):
                matrix_unroll.append([matrix_one[i][j], matrix_two[i][j]])

        start_time = time.time()
        unroll(matrix_unroll, func, "thre", res)
        tempo = time.time() - start_time
        tempo_soma.append(tempo)

    f = open("projeto1/Comparação entre implementação paralela e sequencial/tempo_soma_threads.txt","w+")


    for i in range(len(tamanho)):
        print(tempo_soma[i])
        f.write("%d %f \n" %(tamanho[i], tempo_soma[i]))

    f.close()

    '''


    '''
    res = []
    tamanho = [2, 3, 4, 5, 6, 8, 10, 20, 30, 40, 50, 75, 100]

    tempo_soma = []
    tempo_mult = []

    for k in range(len(tamanho)):

        matrix_one = generate_matrix(tamanho[k],tamanho[k])
        matrix_two = generate_matrix(tamanho[k],tamanho[k])

        matrix_unroll = []
        for i in range(len(matrix_one)):
            for j in range(len(matrix_one[0])):
                matrix_unroll.append([matrix_one[i][j], matrix_two[i][j]])

        start_time = time.time()
        unroll(matrix_unroll, func, "proc", res)
        tempo = time.time() - start_time
        tempo_soma.append(tempo)

    f = open("/projeto1/Comparação entre implementação paralela e sequencial/tempo_soma_processo.txt","w+")


    for i in range(len(tamanho)):
        print(tempo_soma[i])
        f.write("%d %f \n" %(tamanho[i], tempo_soma[i]))

    f.close()

    '''






