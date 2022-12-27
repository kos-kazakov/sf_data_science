from collections import Counter

#cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
#cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']
#counter_moscow=Counter(cars_moscow)
#counter_spb=Counter(cars_spb)
#c['red']+=1
#print(counter_moscow+counter_spb)
#counter_moscow.subtract(counter_spb)
#print(*counter_moscow.elements())
#print(counter_moscow.most_common(1))
#counter_moscow.clear()
#print(counter_moscow)

from collections import defaultdict
#groups=defaultdict(list)

#students = [('Ivanov',1),('Smirnov',4),('Petrov',3),('Kuznetsova',1),
#            ('Nikitina',2),('Markov',3),('Pavlov',2)]

#for student,group in students:
#    groups[group].append(student)
    
#print(groups[2121])
#print(groups)    

from collections import OrderedDict

#data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]
#client_ages = dict(data)
#print(client_ages)
#ord_client_ages = OrderedDict(sorted(data, key=lambda x: x[1]))
#print(ord_client_ages)


#clients = deque()
#clients.append('Ivanov')
#clients.append('Petrov')
#clients.append('Smirnov')
#clients.append('Tikhonova')

#first_client = clients.popleft()
#second_client = clients.popleft()
 
#print("First client:", first_client)
#print("Second client:", second_client)
#clients.appendleft('Vip-client')
#tired_client = clients.pop()
#print(tired_client, "left the queue")
#del clients[2]
#print(clients)

#shop = deque([1, 2, 3, 4, 5], maxlen=3)
#print(shop)
#shop.extendleft([11, 12, 13, 14, 15, 16, 17])
#print(shop)
"""
temps = [20.6, 19.4, 19.0, 19.0, 22.1,
        22.5, 22.8, 24.1, 25.6, 27.0,
        27.0, 25.6, 26.8, 27.3, 22.5,
        25.4, 24.4, 23.7, 23.6, 22.6,
        20.4, 17.9, 17.3, 17.3, 18.1,
        20.1, 22.2, 19.8, 21.3, 21.3,
        21.9]

days = deque(maxlen=7)
 
for temp in temps:
    # Добавляем температуру в очередь
    days.append(temp)
    # Если длина очереди оказалась равной максимальной длине очереди (7),
    # печатаем среднюю температуру за последние 7 дней
    if len(days) == days.maxlen:
        print(round(sum(days) / len(days), 2), end='; ')
# Напечатаем пустую строку, чтобы завершить действие параметра
# end. Иначе следующая строка окажется напечатанной на предыдущей
print("")
"""
"""
temps =  [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]

ordered_temps_dict = OrderedDict(sorted(temps, key=lambda x: x[1], reverse=True))
print(ordered_temps_dict)

temps =  [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]

def check(temps):
    ordered_temps_dict = OrderedDict(sorted(temps, key=lambda x: x[1], reverse=True))
    return ordered_temps_dict
    
print(check(temps))
"""
"""
from collections import deque

def brackets(line):
    dq=deque()
    for el in line:
        if el == '(':
            dq.append(el)
        else:
            if len(dq) == 0:
                return False
            dq.pop()
    if len(dq) != 0:
        return False
    else:
         return True
     
print(brackets("(()())"))
# True
print(brackets(""))
# True
print(brackets("(()()))"))
# False                
"""
"""
ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
           ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
           ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]

#ratings.sort()
cafes = OrderedDict(sorted(ratings, key=lambda x: (-x[1], x[0])))
print(cafes)

"""
"""
from collections import defaultdict, deque

tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', True)]

def task_manager(tasks):
    tasks_by_server = defaultdict(deque)
    for task, server, task_priority in tasks:
        if task_priority:
            tasks_by_server[server].appendleft(task)
        else:
             tasks_by_server[server].append(task)
    return tasks_by_server          
 
print(task_manager(tasks))
# defaultdict(, {'voltage': deque([41667, 35364]),
# 'office': deque([36871, 40690, 33850])})

import numpy as np

"""
import numpy as np

simplelist = [19, 242, 14, 152, 142, 1000]
mean_value = np.array(simplelist).mean()
print(mean_value)
