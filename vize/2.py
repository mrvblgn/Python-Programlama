# 1 :
class a:
   a = b = None
   def __init__(self, a, b):
       self.a = a
       self.b = b
   def __str__(self):
      return self.a+self.b

class b(a):
    pass




# 2 :
p=5/2
q=p*4
r=p+q
p+=p+q+r
q-=p+q*r
print(p,q,r)




# 3 :
def create_multipliers():
    return [lambda x: i * x for i in range(5)]

for multiplier in create_multipliers():
    print(multiplier(2))


