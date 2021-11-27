#First
list = []
while True:
    print("Enter new element? 0/1")
    answer=int(input())
    if(answer!=1):
        break
    else:
        print("Enter the value:")
        list.append(int(input()))
print("List: {}".format(list))
for i in range(len(list)-1):
    for j in range(len(list)-i-1):
        if(list[j]>list[j+1]):
            list[j], list[j+1] = list[j+1], list[j]
print("Sorted list: {}".format(list))
print()

#Second
dict = {}
while True:
    print("Enter new element? 0/1")
    answer=int(input())
    if(answer!=1):
        break
    else:
        print("Enter the name of color:")
        name = input()
        print("Enter the rgb-turple:")
        list = []
        for i in range(3):
            rgb = int(input())
            if(rgb>=0 and rgb<=255):
                list.append(rgb)
            else: 
                print("Wrong!!!")
                break
        dict[name] = list
print(dict)
print()

#Third
import random
set1 = {random.randint(0, 20)}
set2 = {random.randint(0, 20)}
while (len(set1) != 10):
    set1.add(random.randint(0, 20))
while (len(set2) != 10):
    set2.add(random.randint(0, 20))
print(set1)
print(set2)
print("First group:")
print(set1 & set2)
print("Second group:")
print(set1 - set2)
print("Third group:")
print(set2 - set1)
print("Fourth group:")
print((set1|set2) - (set1&set2))
print()

#Fourth
invent = {}
MAX_WEIGHT = 30
while True:
    print("Enter a new element: press 1")
    print("Delete a element: press 2")
    print("For stop: press 0")
    answer = int(input())
    if(answer==1):
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