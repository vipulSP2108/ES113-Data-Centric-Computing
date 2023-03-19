def binary(listx,find):
  left=0
  right=len(listx)-1
  mid=0
  while left <= right:
    mid=(left+right)//2
    mid_num=listx[mid]
    if mid_num==find:
      return mid
    if mid_num<find:
      left=mid+1
    else:
      right=mid-1
  return -1

x=int(input())
listx1=list(map(int,input().split(" ")))
findx=int(input())
print(binary(listx1,findx))

# import numpy as np

# a=int(input())
# lis=list(map(int,input().split(" ")))
# arr=np.array(lis)
# find=int(input())
# min=0
# max=a-1

# if len(lis)==a:
#   while True:
#     mid=min+(max-min)//2
#     if find in arr:
#       if arr[mid]==find:
#         print(mid)
#         break
#       elif arr[mid]<find:
#         min=mid+1
#       else:
#         max=max-1
#     else:
#       print(-1)
#       break
# else:
#   print('error') 