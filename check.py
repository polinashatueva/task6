import Libsort # наш модуль
import time # модуль для замера времени
Massiv = [random.randint(1,10) for i in range(N)]
Start = time.time()
Libsort.insertion_sort(Massiv)
Finish = time.time()
Res_msec = (Finish – Start)*1000

print(len(Massiv))
print()