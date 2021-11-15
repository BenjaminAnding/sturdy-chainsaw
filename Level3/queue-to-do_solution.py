from functools import reduce
from queue import Queue
def solution(s, l):
	q = Queue(maxsize = l)
	workers = [x for x in range(s, s + (l ** 2))]
	xs = []
	i = 0
	j = l
	while i < len(workers):
		while not q.full():
			q.put(workers[i])
			i += 1
		for k in range(j):
			xs.append(q.get())
		while not q.empty():
			q.get()
		j -= 1
	return reduce(lambda x, y: x ^ y, xs)
