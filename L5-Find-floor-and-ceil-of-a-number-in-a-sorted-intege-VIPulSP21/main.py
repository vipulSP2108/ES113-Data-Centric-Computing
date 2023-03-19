def binary(listx,find):
  left=0
  right=len(listx)-1
  while right>=left:
    midindex=(left+right)//2
    if listx[midindex]==find:
      return 1, 1
    if listx[midindex]>find:
      right=midindex-1
    else:
      left=midindex+1
  listm=[]
  
  if right==-1:
    listm.append(right)
    listm.append(listx[left])

  if left==len(listx):
    listm.append(listx[right])
    listm.append(-1)

  else:
    listm.append(listx[right])
    listm.append(listx[left])
    
  return ' '.join(str(i) for i in listm)

i=int(input())
listx=list(map(int,input().split(' ')))
find=int(input())
print(binary(listx,find))