i=int(input())
listx=[]
for j in range(i):
  lists=list(map(int,input()[1:-1].split(',')))
  listx.append(lists)

# for x in listx[0][0]:
#   listx.sort(x)

listx.sort(key=lambda x:x[0])
mearged=[]
for lists in listx:
  if not mearged or mearged[-1][1]<lists[0]:
    mearged.append(lists)
  else:
    mearged[-1][1]=max(mearged[-1][1],lists[1])
    
for lists in mearged:
  print(f'[{lists[0]}, {lists[1]}]',end=',')

# i=int(input())
# listx=[]
# for j in range(i):
#   b=input()
#   listx.append(b[1])
#   listx.append(b[3])
  
# list=list(map(int,listx))
# list_old=list

# list.sort()
# list_new=list
# print(list_old,list_new)

# def OverlapInterval(list1,list2):
#   len_list1=len(list1)
#   len_list2=len(list2)
  