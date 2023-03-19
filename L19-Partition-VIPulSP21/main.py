# def partition(listx,start,end):
#   count=0
#   pivot=listx[end]
#   i=start-1
#   for j in range(start,end):
#     if listx[j]<pivot:
#       i=i+1
#       listx[i],listx[j]=listx[j],list[i]
#   listx[i+1],listx[end]=listx[end],listx[i+1]
  
#   return count

# i=int(input())
# listx=list(map(int,input().split(' ')))
# print(partition(listx,0,len(listx)-1))

def partition(listx,start,end):
  count=0
  pivot=listx[start]
  i=start
  for j in range(start+1,end):
    if listx[j]<pivot:
      i=i+1
      listx[i],listx[j]=listx[j],list[i]
      count=count+1
  listx[0],listx[i]=listx[i],listx[0]
  
  return count
  
i=int(input())
listx=list(map(int,input().split(' ')))
print(partition(listx,0,len(listx)))

# def partition(listx,start,end,count):
#   # pivot_index=0
#   pivot_index=start
#   pivot=listx[pivot_index]
#   # start=pivot_index+1
#   # end=len(listx)-1

#   while start<end:
#     while start<len(listx) and pivot>=listx[start]:
#       start=start+1
#     while pivot<listx[end]:
#       end=end-1

#     if start<end:
#       listx[start],listx[end]=listx[end],listx[start]
#   listx[pivot_index],listx[end]=listx[end],listx[pivot_index]
#   count=count+1
#   return end

# def Quicksort(listx,start,end,count):
#   if start<end:
#     partindex=partition(listx,start,end,count)
#     Quicksort(listx,start,partindex-1,count)
#     Quicksort(listx,partindex+1,end,count)
#   return count,listx

# i=int(input())
# listx=list(map(int,input().split(' ')))
# print(partition(listx,0,len(listx)-1))
# abc=Quicksort(listx,0,len(listx)-1,0)
# print(abc)