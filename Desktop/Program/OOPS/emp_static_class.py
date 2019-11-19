from datetime import date as dt
class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age
   @staticmethod
   def isAdult(age):
      if age > 18:
         return True
      else:
         return False
   @classmethod
   def p_from_year(p_cls, name, year):
      return p_cls(name, dt.today().year - year)
   def __str__(self):
      return 'Person Name: {} and Age: {}'.format(self.name, self.age)
p1 = Person('Utkarsh', 25)
print(p1)
p2 = Person.p_from_year('Ajinkya', 1996)
print(p2)
print(Person.isAdult(12))
print(Person.isAdult(18))

