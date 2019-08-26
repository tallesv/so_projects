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
				print("processo filho: " + str(os.getpid()) + " do pai :" + str(os.getppid()))
				func(args[i][0], args[i][1])
				if(operation == 'sum'):
					results.append([ args[i][0] + args[i][0], args[i][1] + args[i][1] ])
					exit()		
	elif(method == 'thre'):
		
		#for i in range(0, 5):
		#	global var
		#	global lock
		#	if(operation == 'sum'):
		#		x = threading.Thread(target=func, args=(args[i]))
		#		x.start()
		#		lock.acquire()	
		#		results.append([ args[i][0] + args[i][0], args[i][1] + args[i][1] ])	
		#		lock.release()
		global var
		global lock
		if(operation == 'sum'):
			t1 = threading.Thread(target=func, args=(args[0]))
			t2 = threading.Thread(target=func, args=(args[1]))
			t3 = threading.Thread(target=func, args=(args[2]))
			t4 = threading.Thread(target=func, args=(args[3]))
			t5 = threading.Thread(target=func, args=(args[4]))
			t1.start()
			lock.acquire()	
			results.append([ args[0][0] + args[0][0], args[0][1] + args[0][1] ])	
			lock.release()
			t2.start()
			lock.acquire()	
			results.append([ args[1][0] + args[1][0], args[1][1] + args[1][1] ])	
			lock.release()
			t3.start()
			lock.acquire()	
			results.append([ args[2][0] + args[2][0], args[2][1] + args[2][1] ])	
			lock.release()
			t4.start()
			lock.acquire()	
			results.append([ args[3][0] + args[3][0], args[3][1] + args[3][1] ])	
			lock.release()
			t5.start()
			lock.acquire()	
			results.append([ args[4][0] + args[4][0], args[4][1] + args[4][1] ])	
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