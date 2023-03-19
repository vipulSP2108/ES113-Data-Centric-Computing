class Node:
  def __init__(self,data=None,next=None):
    self.data=data
    self.next=next

class Linklist:
  def __init__(self):
    self.head=None
    
  def add(self,data):
    if self.head is None:
      self.head=Node(data,None)
      return
    itr=self.head
    while itr.next:
      itr=itr.next
    itr.next=Node(data)

  def delete(self,data):
    itr=self.head
    if itr.data==data:
      self.head=itr.next
      itr=None
      return
    while itr.next:
      if itr.data==data:
        break
      privious=itr
      itr=itr.next
    privious.next=itr.next
    itr=None

  def print(self):
    if self.head is None:
      return -1
    itr=self.head
    llstr=''
    while itr:
      llstr=llstr+str(itr.data)+' '
#      print(itr.data,end=' ')
      itr=itr.next
    print(llstr)

i=int(input())
count=0
ll=Linklist()
while count<i:
  fuc,num=input().split(' ')
  if fuc=='a':
    ll.add(int(num))
  elif fuc=='d':
    ll.delete(int(num))
  count=count+1

ll.print()