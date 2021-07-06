#Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.

#Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

#Примеры матриц вы найдете в методичке.

#Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

#Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

#Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
  def __init__(self,data):
   self.data = data
  
  def __str__(self):
    return "\n".join("\t".join([f"{i:03}" for i in line]) for line in self.data)
    
  def __add__(self, other):
    try:
      j = [[int(self.data[line][i]) + int(other.data[line][i]) for i in range(len(self.data[line]))] for line in range(len(self.data[line]))] for line in range(len(self.data))]
        return Matrix[j]
      except IndexError:
        return f"Не верная размерность матриц"
        
m_1 = [[4, 5, 29],[18,2, 3],[14, -25, 75]]
m_2 = [["2", "67", "82"], ["24", "72", "-13"],["8", "-19", "33"]]

mx_1 = Matrix(m_1)
mx_2 = Matrix(m_2)
sum_m = mx_1 + mx_2