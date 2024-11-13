import alg1  # наш модуль
import time  # модуль для замера времени

N =10
from random import randint

Massiv = [randint(1, 1000) for i in range(N)]
M =Massiv[:]
Start = time.time()
alg1.bubble_sort(M)
Finish = time.time()
Res_msec = (Finish - Start) * 1000
print (Res_msec)
Start = time.time()
alg1.selection_sort(M)
Finish = time.time()
Res_msec = (Finish - Start) * 1000
print (Res_msec)
Start = time.time()
alg1.insertion_sort(M)
Finish = time.time()
Res_msec = (Finish - Start) * 1000
print (Res_msec)
Start = time.time()
alg1.selection_sort(M)
Finish = time.time()
Res_msec = (Finish - Start) * 1000
print (Res_msec)