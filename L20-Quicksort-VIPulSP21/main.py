def partition(listx,start,end):
  pivot=listx[end]
  i=start-1
  for j in range(start,end):
    if pivot>listx[j]:
      i=i+1
      listx[i],listx[j]=listx[j],listx[i]
  listx[i+1],listx[end]=listx[end],listx[i+1]
  return i+1

# def partition(listx,start,end):
#   pivot_index=start
#   # pivot_index=0
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
#   listx[end],listx[pivot_index]=listx[pivot_index],listx[end]
#   return end

def Quicksort(listx,start,end):
  if start<end:
    partindex=partition(listx,start,end)
    Quicksort(listx,start,partindex-1)
    Quicksort(listx,partindex+1,end)
    return listx

i=int(input())
listx=list(map(int,input().split(' ')))
abc=Quicksort(listx,0,len(listx)-1)
print(*abc)