class Node:
  def __init__(self,data=None,next=None):
    self.data=data
    self.next=next

class Linklist:
  def __init__(self):
    self.head=None

  def insert_at_end(self,data):
    if self.head is None:
      self.head=Node(data,None)
      return
      
    itr = self.head
    while itr.next:
      itr=itr.next
    itr.next=Node(data)

  def print(self):
    if self.head is None:
      return -1

    itr=self.head
#    llstr=''
    while itr:
#      llstr=llstr+str(itr.data)+' '
      print(itr.data,end=' ')
      itr=itr.next
#    print(llstr)
    
i=int(input())
ll=Linklist()
count=1
while i>=count:
  j=int(input())
  ll.insert_at_end(j)
  count=count+1

ll.print()

# listx=[]
# i=int(input())
# count=0
# while count<i:
#   new=int(input())
#   listx.append(new)
#   count=count+1
# print(' '.join(str(i) for i in listx))