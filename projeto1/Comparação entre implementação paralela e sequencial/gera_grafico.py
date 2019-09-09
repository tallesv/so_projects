# Make sure to import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np

# Prepare your data
x_seq_soma = []
y_seq_soma = []
f = open("tempo_soma_sequencial.txt","r")
for l in f:
	row = l.split()
	x_seq_soma.append(row[0])
	y_seq_soma.append(row[1])

f.close()

x_seq_mult = []
y_seq_mult = []
f = open("tempo_mult_sequencial.txt","r")
for l in f:
	row = l.split()
	x_seq_mult.append(row[0])
	y_seq_mult.append(row[1])

f.close()

x_thread_soma = []
y_thread_soma = []
f = open("tempo_soma_threads.txt","r")
for l in f:
	row = l.split()
	x_thread_soma.append(row[0])
	y_thread_soma.append(row[1])

f.close()


# Plotting the data
plt.plot(x_seq_soma, y_seq_soma, label='soma sequencial')
plt.plot(x_seq_mult, y_seq_mult, label='multiplicacao sequencial')
plt.plot(x_thread_soma, y_thread_soma, label='soma por threads')
plt.ylim(bottom=1)
# Adding a legend
plt.legend()
plt.ylabel('tempo')
plt.xlabel('tamanho da matriz')
# Result
plt.show()