i=int(input())
listx=list(map(int,input().split(' ')))


for i in range(1,len(listx)):
  var=listx[i]
  j=i-1
  while j>=0 and var<listx[j]:
    listx[j+1]=listx[j]
    j=j-1
  listx[j+1]=var
  print(' '.join(str(i) for i in listx))


# listm=[]
# def insertion(listx):
#   for i in range(1,len(listx)):
#     var=listx[i]
#     j=i-1
#     while j>=0 and var<listx[j]:
#       listx[j+1]=listx[j]
#       j=j-1
#     listx[j+1]=var
#     listm.append(listx)
#     for i in range(len(listm)-1):
#       print(' '.join(str(j) for j in listm[i]))

# print(insertion(listx))


      