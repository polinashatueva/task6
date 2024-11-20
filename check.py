import alg1  # наш модуль
import time  # модуль для замера времени

N =int(input())
from random import randint

Massiv = [randint(1, 1000) for i in range(N)]
M =Massiv[:]

Start = time.time()
alg1.bubble_sort(M)
Finish = time.time()
Res_msec1 = (Finish - Start) * 1000
print (Res_msec1)

Start = time.time()
alg1.selection_sort(M)
Finish = time.time()
Res_msec2 = (Finish - Start) * 1000
print (Res_msec2)

Start = time.time()
alg1.insertion_sort(M)
Finish = time.time()
Res_msec3 = (Finish - Start) * 1000
print (Res_msec3)

high=max(M)
low = min(M)
Start = time.time()
alg1.quick_sort(M, high, low)
Finish = time.time()
Res_msec4 = (Finish - Start) * 1000
print (Res_msec4)

