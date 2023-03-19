def merge_sort(listx):
  if len(listx)<=1:
    return

  mid=len(listx)//2
  left_list=listx[:mid]
  right_list=listx[mid:]

  merge_sort(left_list)
  merge_sort(right_list)
  return mearge_two_sorted_list(left_list,right_list,listx)
    
def mearge_two_sorted_list(a,b,listx):
  # sorted_list=[]
  len_a=len(a)
  len_b=len(b)
  counta=0
  countb=0
  k=0
  while counta<len(a) and countb<len(b):
    if a[counta]<=b[countb]:
      # sorted_list.append(a[counta])
      listx[k]=a[counta]
      counta=counta+1
    else:
      # sorted_list.append(b[countb])
      listx[k]=b[countb]
      countb=countb+1
    k=k+1
  while counta<len_a:
    listx[k]=a[counta]
    k=k+1
    counta=counta+1
  while countb<len_b:
    listx[k]=b[countb]
    k=k+1
    countb=countb+1
  # if counta<len_a:
  #   sorted_list=sorted_list+a[counta:]
  # if countb<len_b:
  #   sorted_list=sorted_list+b[countb:]
  # return sorted_list

i=int(input())
lst=list(map(int,input().split(' ')))
merge_sort(lst)

print(' '.join(str(i) for i in lst))
# a=[1,3,5]
# b=[2,4,6]
# mearge_two_sorted_list(a,b)