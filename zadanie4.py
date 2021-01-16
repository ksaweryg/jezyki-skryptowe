
from random import randint
long_list = [randint(0, 3000) for element in range(1000000)]

import time
start_time = time.time()
for num in long_list:
    if num == -1:
        print(num)
print(time.time()-start_time)

start_time2 = time.time()
counter = len(long_list)-1
while counter>0:
    if long_list[counter]==-1:
        print(long_list[counter])
    counter -=counter
print(time.time()-start_time2)

start_time3 = time.time()
if -1 in long_list:
    print('found')
print(time.time() - start_time3)

start_time4 = time.time()
if -1 not in long_list:
    pass
else:
    print('found')
print(time.time() - start_time4)