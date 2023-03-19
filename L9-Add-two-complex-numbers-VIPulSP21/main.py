class Complex:
  def __init__(self,real,imagi):
    self.real=real
    self.imagi=imagi
  def __add__(self1,self2):
    final_real=self1.real+self2.real
    final_imagi=self1.imagi+self2.imagi 
    if final_imagi==0:
      return final_real
    elif final_real==0:
      if final_imagi>0:
        return f'i{final_imagi}'
      elif final_imagi>0:
        return f'-i{abs(final_imagi)}'
    elif final_imagi>0:
      return f'{final_real}+i{final_imagi}'
    elif final_imagi<0:
      return f'{final_real}-i{abs(final_imagi)}'

r1,i1=input().split(' ')
r2,i2=input().split(' ')
comp1=Complex(int(r1),int(i1))
comp2=Complex(int(r2),int(i2))
print(comp1+comp2)