i=int(input())
listx=list(map(int,input().split(' ')))

def StrangePairs(listx):
  count=0
  for i in range(len(listx)):
    for j in range(i+1,len(listx)):
      numi=listx[i]
      numj=listx[j]
      if numi>2*numj:
        count=count+1
  return count

print(StrangePairs(listx))

# def mearge_lists(list1,list2,lst):
#   # listx=[]
#   len_list1=len(list1)
#   len_list2=len(list2)
#   count1=0
#   count2=0
#   k=0
#   while count1<len_list1 and count2<len_list2:
#     if list1[count1]>=list2[count2]:
#       # listx.append(list1[count1])
#       lst[k]=list1[count1]
#       count1=count1+1
#     elif list1[count1]<=list2[count2]:
#       # listx.append(list2[count2])
#       lst[k]=list2[count2]
#       count2=count2+1
#     k=k+1
#   if count1>len_list1:
#     listx.append(list2[count2:])
#   if count2>len_list2:
#     listx.append(list1[count1:])

# def mearge(listx):
#   if len(listx)<=1:
#     return
    
#   mid=len(listx)//2
#   left=listx[:mid]
#   right=listx[mid:]
#   mearge(left)
#   mearge(right)
#   return mearge_lists(left,right,listx)
 