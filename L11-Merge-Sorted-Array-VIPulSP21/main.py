i1=int(input())
listx1=list(map(int,input().split(' ')))
i2=int(input())
listx2=list(map(int,input().split(' ')))
# listx=listx1+listx2

# def mergesorting(listfinal):
#   for i in range(1,len(listfinal)):
#     var=listfinal[i]
#     j=i-1
#     while j>=0 and listfinal[j]>var:
#       listfinal[j+1]=listfinal[j]
#       j=j-1
#     listfinal[j+1]=var
    
#   return " ".join(str(i) for i in listfinal)

# print(mergesorting(listx))

def merge_sorted_array(a,b):
  len_a=len(a)
  len_b=len(b)
  counta=0
  countb=0
  sorted_list=[]
  while counta<len_a and countb<len_b:
    if a[counta]<=b[countb]:
      sorted_list.append(a[counta])
      counta=counta+1
    else:
      sorted_list.append(b[countb])
      countb=countb+1
  if counta<len_a:
    sorted_list=sorted_list+a[counta:]
  if countb<len_b:
    sorted_list=sorted_list+b[countb:]
  return sorted_list

lst=merge_sorted_array(listx1,listx2)
print(' '.join(str(i) for i in lst))