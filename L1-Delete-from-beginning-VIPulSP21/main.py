class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

#class Linked List
class LinkedList:
  def __init__(self):
    self.head = None

  def push_front(self, newElement):
    newNode = Node(newElement)
    newNode.next = self.head 
    self.head = newNode   
  
  def delete_beginning(self,i):
#    itr=self.head
#    count=0
#    while itr and count<i:
#      itr=self.head
#      self.head=itr.next
#      count=count+1

    itr=self.head
    count=0
    while itr and count<i:
      itr=itr.next
      count=count+1
      
    if self.head is None:
      return -1

    elif count<i:
      return -1

    else:
      self.head=itr
      itr=self.head
      llstr=''
      while itr:
        llstr=llstr+str(itr.data)+' '
        itr=itr.next
      return llstr
    
MyList = LinkedList()

MyList.push_front(10)
MyList.push_front(20)
MyList.push_front(30)
MyList.push_front(40)
MyList.push_front(50)
MyList.push_front(60)
MyList.push_front(70)
MyList.push_front(80)
MyList.push_front(90)

n=int(input())
#Write your delete code 
print(MyList.delete_beginning(n))

# listx=[90,80,70,60,50,40,30,20,10]