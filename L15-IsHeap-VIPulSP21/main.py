n=int(input())
listx=list(map(int,input().split(' ')))

def isheap(len_list,listx):
  for i in range(len_list-1,0,-1):
    if listx[i]<listx[(i-1)//2]:
      return 0
  return 1

print(isheap(n,listx))