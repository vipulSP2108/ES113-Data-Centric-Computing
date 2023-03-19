def heapify(N,listx,i):
  largest=i
  left=(i*2)+1
  right=(i*2)+2
  if left<N and listx[largest]<listx[left]:
    largest=left
  if right<N and listx[largest]<listx[right]:
    largest=right
  if largest!=i:
    listx[i],listx[largest]=listx[largest],listx[i]
    heapify(N,listx,largest)

def HeapSort(listx):
  N=len(listx)
  for i in range(N-1//2,-1,-1):
    heapify(N,listx,i)

  for i in range(N-1,0,-1):
    listx[0],listx[i]=listx[i],listx[0]
    heapify(i,listx,0)
  return listx
  
i=int(input())
listx=list(map(int,input().split(' ')))
newlist=HeapSort(listx)
for i in newlist:
  print(i,end=' ')