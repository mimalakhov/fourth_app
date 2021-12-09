#First_______________________________________________________________
'''Реализовать сортировку списка методом пузырька;
'''
list = [] # Для введённого пользователем

while True: # Стандартный цикл для пользовательского ввода
    print("Enter new element? 0/1")
    answer = int(input())
    if(answer != 1):
        break
    else:
        print("Enter the value:")
        list.append(int(input()))
print("List: {}".format(list)) 

# Алгоритм для сортировки пузырьком
for i in range(len(list) - 1):
    for j in range(len(list) - i - 1):
        if(list[j] > list[j+1]):
            list[j], list[j+1] = list[j+1], list[j]
print("Sorted list: {}".format(list))
print()

#Second__________________________________________________________
'''Создать словарь цветов, в котором ключ - название или кодировка цвета; значение - кортеж из rgb этого цвета
'''
dict = {}

while True:
    print("Enter new element? 0/1")
    answer = int(input())
    if(answer != 1):
        break
    else:
        # Вводится название цвета, а затем его представление в rgb-формате
        print("Enter the name of color:")
        name = input()
        print("Enter the rgb-turple:")
        list = []
        for i in range(3):
            rgb = int(input())
            if(rgb >= 0 and rgb <= 255):
                list.append(rgb)
            else: 
                print("Wrong!!!")
                break
        dict[name] = list
print(dict)
print()

#Third_______________________________________________________________
'''Заполнить два случайных набора чисел. Вывести оба набора. Указать какие элементы:
         входят одновременно в оба;
         входят только в первое, но не входят во второе;
         входят только во второе, но не входят в первое;
         входят в первое или во второе, но не в оба из них одновременно.
'''
import random

# Первичное объявление множеств
set1 = {random.randint(0, 20)}
set2 = {random.randint(0, 20)}

while (len(set1) != 10): # Заполнение множества 1 до тех пор, пока его размер не станет равным 10
    set1.add(random.randint(0, 20))
while (len(set2) != 10): # Заполнение множества 2 до тех пор, пока его размер не станет равным 10
    set2.add(random.randint(0, 20))
print(set1)
print(set2)

print("First group:")
print(set1 & set2)
print("Second group:")
print(set1 - set2)
print(set2 - set1)
print("Fourth group:")
print((set1|set2) - (set1&set2))
print()

#Fourth___________________________________________________________________
'''Создать игровой инвентарь. 
   Должна быть возможность добавлять в него предметы и удалять предметы из него. 
   Инвентарь должен быть ограничен по весу, каждый предмет имеет свой вес. 
   Вывод предметов должен быть с названием предмета и его весом.
'''
invent = {}
MAX_WEIGHT = 30 # Константа для максимального веса инвентаря
while True:
    # Меню для добавления/удаления/остановки
    print("Enter a new element: press 1")
    print("Delete a element: press 2")
    print("For stop: press 0")
    answer = int(input())
    if(answer == 1):
        if(sum(invent.values()) >= MAX_WEIGHT):
            print("The inventory is full!")
        else:
            print("Enter the name:")
            name = input()
            print("Enter the weight:")
            weight = int(input())
            invent[name] = weight
    elif(answer==2):
        print("Enter the name")
        name = input()
        if(name in invent):
            invent.pop(name)
        else: print("No such element!")
    else: break
    print(invent)