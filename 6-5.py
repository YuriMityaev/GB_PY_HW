class Stationery:
  def __init__(self, title="Ты всегда можешь что-нибудь нарисовать"):
    self.title = title
    
    def draw (self):
      print(f"Просто начни с {self.title}!")
      
class Pen(Stationery):
  def draw(self):
    print(f"Или можешь использовать {self.title} ручку!")
    
class Pencil(Stationery):
  def draw(self):
    print(f"Разрисуй все {self.title} карандашами!")
    
class Marker(Stationery):
  def draw(self):
    print(f"На обоях хорошо пишет {self.title} маркер!")

    
    stat=Stationery()
    stat.draw()
    pen = Pen ("Гелевую")
    pen.draw()
    Pencil = Pencil("Разноцветными")
    pencil.draw()
    marker = Marker("самый толстый")
    marker.draw()
