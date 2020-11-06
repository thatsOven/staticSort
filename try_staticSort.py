from thatsOvens_staticSort import thatsOvens_staticSort
from random import randrange
from time import time
inputa = []
number_quantity = 1000
maximum_number = 1000
for i in range(number_quantity):
    inputa.append(randrange(0, int(maximum_number), 1))
print(inputa)
startime = time()
thatsOvens_staticSort(inputa)
fin = str(time() - startime)
print(inputa)
print("thatsOven's staticSort, Elapsed time: " + fin + ' s (' + str(float(fin) * 1000) + ' ms)')
print('Quantity of numbers: ' + str(len(inputa)) + ' , Maximum number: ' + str(max(inputa)))
input()
