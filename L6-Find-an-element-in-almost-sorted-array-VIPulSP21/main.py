i=int(input())
listx=list(map(int,input().split(' ')))
find=int(input())

# listx=[10, 20, 30, 40, 50, 45, 35, 25, 15]
# find=43

def binary(listx):
  val=len(listx)//2
  leftmin=0
  leftmax=val # here val 4, ie. 40
  rightmin=val # here val 4, ie. 50
  rightmax=len(listx)-1
  new=''
  while True:
    while leftmax>leftmin:
      leftmid=(leftmin+leftmax)//2
      findp=listx[leftmid]
      if find==findp:
        new=leftmid
        break
      elif find>findp:
        leftmin=leftmid + 1
      elif find<findp:
        leftmax=leftmid-1
    
    while rightmax>=rightmin:
      rightmid=(rightmin+rightmax)//2
      findp=listx[rightmid]
      if find==findp:
        new=rightmid
        break
      elif find<findp:
        rightmin=rightmid+1
      elif find>findp:
        rightmax=rightmid-1
    if type(new)==int:
      return new
      break
    else:
      return -1
      break

print(binary(listx))