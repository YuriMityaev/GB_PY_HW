from itertools import zip_longest

class Matrix:
  def __init__(self,data):
      self.data = data
  
  def __str__(self):
      return str("\n".join(["\t".join([str(i) for i in j]) for j in self.data]))
    
  def __add__(self, other):
      return Matrix([map(sum, zip_longest(*t, fillvalue=0))
                     for t in zip_longest(self.data, other.data, fillvalue=[])])
        
m_1 = [[4, 5, 29], [18,2, 3], [14, -25]]
m_2 = [[4, 5, 1], [33,21, 86]]

mx_1 = Matrix(m_1)
mx_2 = Matrix(m_2)
print(mx_1)
print(mx_1 + mx_2)
