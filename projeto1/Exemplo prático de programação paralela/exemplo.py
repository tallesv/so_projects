def func(var1, var2):
	print (str(var1) + ", " + str(var2))
#programa principal
#sem usar loop unrolling
for i in range(5):
	func(i, i+1)