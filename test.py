import time
from _thread import *

l = []
previous_time = time.time()
count = 0

while count < 1000:
	current_time = time.time()
	l.append((current_time-previous_time)*10**3)
	previous_time = current_time
	count += 1

print(sum(l)/len(l))

def func():
	i = 1
	return

l = []
count = 0
while count < 1000:
	start_time = time.time()
	start_new_thread(func, ())
	end_time = time.time()
	l.append((end_time-start_time)*10**3)
	count += 1

print(sum(l)/len(l))
	