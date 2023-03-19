# M1
class Matrix:
  def __init__(self,matx):
    self.matxa=matx[0]
    self.matxb=matx[1]
    self.matxc=matx[2]
    self.matxd=matx[3]
  def __add__(matx1,matx2):
    matxsum=[]
    matxsum.append(matx1.matxa+matx2.matxa)
    matxsum.append(matx1.matxb+matx2.matxb)
    matxsum.append(matx1.matxc+matx2.matxc)
    matxsum.append(matx1.matxd+matx2.matxd)
    return matxsum

# M2
# class Matrix:
#   def __init__(self,matx):
#     self.mat=[matx[0],matx[1],matx[2],matx[3]]
#   def __add__(self1,self2):
#     matsum=[]
#     matsum.append(self1.mat[0]+self2.mat[0])
#     matsum.append(self1.mat[1]+self2.mat[1])
#     matsum.append(self1.mat[2]+self2.mat[2])
#     matsum.append(self1.mat[3]+self2.mat[3])
#     return matsum
    
matx1=Matrix(list(map(int,input().split(' '))))
matx2=Matrix(list(map(int,input().split(' '))))
matxsum=matx1+matx2
print(' '.join(str(i) for i in matxsum))

# def __add__(matx1,matx2):
#   matxsum=matx1 + matx2
#   return ' '.join(str(i) for i in matxsum)

# matx1=np.array(list(map(int,input().split(' '))))
# matx2=np.array(list(map(int,input().split(' '))))

# print(__add__(matx1,matx2))

# def __add__(matx1,matx2):
#   matxsum=[]
#   for i in range(len(matx1)):
#     matxsum.append(matx1[i]+matx2[i])
#   return ' '.join(str() for i in matxsum)

# matx1=list(map(int,input().split(' ')))
# matx2=list(map(int,input().split(' ')))
# print(__add__(matx1,matx2))