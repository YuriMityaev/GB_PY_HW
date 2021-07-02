class Worker:
    def __init__(self, name, surname, position, salary, bonus):
      self.name = name
      self.surname = surname
      self.position = position
      self._income = {"salary": salary, "bonus": bonus}


class Position(Worker):
    def get_name(self):
        return f"{self.name} {self.surname}"

    def get_base(self):
        return f"{sum(self._income.values())}"


worker = Position("Yuri", "Mityaev", "Specialist", 100000, 20000)
print(worker.get_name())
print(worker.position)
print(worker.get_base())
