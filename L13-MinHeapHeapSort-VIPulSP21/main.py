def heapify(N,listx,i):
  minimum=i
  left=i*2+1
  right=i*2+2
  if left<N and listx[minimum]>listx[left]:
    minimum=left
  if right<N and listx[minimum]>listx[right]:
    minimum=right
  if minimum != i:
    listx[i],listx[minimum]=listx[minimum],listx[i]

    heapify(N,listx,minimum)

def MinSort(listx):
  N=len(listx)
  for i in range(N//2-1,-1,-1):
    heapify(N,listx,i)

  for i in range(N-1,0,-1):
    listx[i],listx[0]=listx[0],listx[i]
    heapify(i,listx,0)
  return listx
  
i=int(input())
listx=list(map(int,input().split(' ')))
newlist=MinSort(listx)
# print(newlist)

for i in range(len(newlist)-1,-1,-1):
  print(newlist[i],end=' ')