# 1 :
print("Python {0[0]} is {0[1]}".format(('Object', 'Oriented')))



# 2 :
for i in range(5):
    for j in range(i):
        print("A", end=" ")
    print()



# 3 :
metin = "Metin"
try:
    metin += 3
except:
    print("Hatalı işlem")



# 4 :
class a:
   a = b = None
   def __init__(self, a, b):
       self.a = a
       self.b = b
   def __str__(self):
      return self.a+self.b

b = a("3", "5")
print(b)





