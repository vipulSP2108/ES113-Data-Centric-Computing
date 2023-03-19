def TwickQuick(listx,find):
  if not listx:
    return None
  pivot=listx[0]
  left=[]
  right=[]
  for x in listx:
    if x<pivot:
      left.append(x)
    if x>pivot:
      right.append(x)
  i=len(left)
  if find-1==i:
    return pivot
  elif find-1<i:
    return TwickQuick(left,find)
  else:
    return TwickQuick(right,find-i-1)
  
i=int(input())
listx=list(map(int,input().split(' ')))
k=int(input())

print(TwickQuick(listx,k))