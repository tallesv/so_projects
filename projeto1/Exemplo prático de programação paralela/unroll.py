import time
import os
import threading

lock = threading.Lock()

def func(var1, var2):
	print (str(var1) + ", " + str(var2))

def unroll(args, func, method, results, operation):
	if(method == 'proc'):
		print("")

		linhas = len(args)
		for i in range(0, 5):
			time.sleep(1)
			if(os.fork() == 0):
				##print("processo filho: " + str(os.getpid()) + " do pai :" + str(os.getppid()))
				func(args[i][0], args[i][1])
				if(operation == 'sum'):
					results.append([ args[i][0] + args[i][0], args[i][1] + args[i][1] ])
					exit()		
	elif(method == 'thre'):
		
		for i in range(0, 5):
			global var
			global lock
			if(operation == 'sum'):
				x = threading.Thread(target=func, args=(args[i]))
				x.start()
				lock.acquire()	
				results.append([ args[i][0] + args[i][0], args[i][1] + args[i][1] ])	
				lock.release()

	else:
		print("metodo invalido!")
#programa principal
#usando loop unrolling
res = []
unroll([[0, 1],[1, 2], [2, 3], [3, 4],[4, 5]], func, 'proc',res, 'sum')
#unroll([[0, 1],[1, 2], [2, 3], [3, 4],[4, 5]], func, 'thre',res, 'sum')

mat = [[0, 1],[1, 2], [2, 3], [3, 4],[4, 5]]

print(res)