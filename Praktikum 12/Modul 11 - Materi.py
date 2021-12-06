"""
@Materi: Object Oriented Programming
@Judul: Praktikum 11 Materi
@Hari/Tanggal: Senin, 20210920
@NIM: 065001900001
@author: Azhar Rizky Zulma
"""

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name: ", self.name,  ", Salary: ", self.salary)


#This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
#This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)


#Versi Mamalia

class Mamalia:
    mamalCount = 0
    
    def __init__(self, nama_mamalia, kaki_mamalia):
        self.nama_mamalia = nama_mamalia
        self.kaki_mamalia = kaki_mamalia
        Mamalia.mamalCount += 1
        
    def printMamal(self):
        print("Nama Mamalia ini Adalah: " + self.nama_mamalia + "\nKakinya Berjumlah " + str(self.kaki_mamalia))
                
mamal1 = Mamalia("Kucing", 4)
mamal1.printMamal()

mamal2 = Mamalia("Hamster", 4)
mamal2.printMamal()

print("Jumlah Mamalia yang dimasukkan ke dalam objek adalah: ", Mamalia.mamalCount)
