# data overloading

class Person:
  def __init__(self,name,date):
    self.date=list(map(int,date.split('/')))
    self.name=name
  def __gt__(self1,self2):
    if self1.date[2]<self2.date[2]:
      return True
    elif self1.date[2]>self2.date[2]:
      return False
      
    elif self1.date[1]<self2.date[1]:
      return True
    elif self1.date[1]>self2.date[1]:
      return False
      
    elif self1.date[0]>self2.date[0]:
      return True
    elif self1.date[0]<self2.date[0]:
      return False
      
    else:
      return False
      
i1,i2=input().split(',')
j1,j2=input().split(',')
per1=Person(i1,i2)
per2=Person(j1,j2)
print(per1>per2)

# id,im,iy=i2.split('/')
# jd,jm,jy=j2.split('/')

# if iy>jy:
#   print('False')
# elif jy>iy:
#   print('True')

# elif im>jm and iy==jy:
#   print('False')
# elif jm>im and jy==iy:
#   print('True')

# elif id>jd and im==jm and iy==jy:
#   print('False')
# elif jd>id and jm==im and jy==iy:
#   print('True')

# else:
#   print('False')