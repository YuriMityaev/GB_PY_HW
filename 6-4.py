class Car:
  """Автомобиль"""
  
  def __init__(self, name, color, speed, is_police=False):
    self.name = name
    self.color = color
    self.speed = speed
    self.is_police = is_police
    print(f"Новая машина: {self.name} (Цвет {self.color}) машина полицейская - {self.is_police}")
    
  def go(self):
    print(f"{self.name}: Машина поехала.")
    
  def stop(self):
    print(f"{self.name}: Машина остановилась.")
  
  def turn(self.direction):
    print(f"{self.name}: Машина повернула {"налево" if derection ==0 else "направо"}."}
    
  def show_speed(self):
    return f"{self.name}: Скорость автомобиля: {self.speed}."
    
  class TownCar(Car):
      #Городской автомобиль
      
      def show_speed(self):
        return f"{self.name}: Скорость автомобиля: {Self.speed}. Превышение скорости!"
            if self.speed > 60 else f"{self.name}: Скорость автомобиля {self.speed}"
            
            
     class WorkingCar(Car):
      #Грузовой Автомобиль
      
      def show_speed(self):
        return f"{self.name}: Скорость автомобиля: {Self.speed}. Превышение скорости!"
            if self.speed > 40 else f"{self.name}: Скорость автомобиля {self.speed}"
            
     class SportCar(Car):
     #Спорткар
     pass
     
     class PoliceCar(Car):
      #Полиция
      
      def __init__(self, name, color, speed, is_police=True):
        return f"{self.name}: Скорость автомобиля: {Self.speed}. Превышение скорости!"
            super().__init__(name,color,speed, is_police)
            
       police_car = PoliceCar("Бобик", "Синиего", 80)
       police_car.go()
       print(police_car.show_speed())
       police_car.turn(0)
       police_car.stop()
       print()
       
       work_car = WorkCar("Буханка", "Зеленого", 40)
       work_car.go()
       work_car.turn(1)
       print(work_car.show_speed())
       work_car.turn(0)
       work_car.stop()
       print()
       
       sport_car = SportCar("Ферари", "красного", 120)
       sport_car.go()
       sport_car.turn(0)
       print(sport_car.show_speed())
       sport_car.turn(0)
       sport_car.stop()
       print()
       
       town_car = TownCar("Дайхатсу", "белого", 50)
       town_car.go()
       town_car.turn(1)
       print(town_car.show_speed())
       town_car.turn(0)
       town_car.stop()
       print()
       
       print (f" Авто {town_car.name} ({town_car.color} цвета)")
       print (f" Авто {police_car.name} ({police_car.color} цвета)")
