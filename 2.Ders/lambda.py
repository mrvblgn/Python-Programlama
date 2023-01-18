lambda_fonksiyonu = lambda a: a + 10

print(lambda_fonksiyonu(5))




topla = lambda a, b: a + b

def toplama(a, b):
    return a + b

print(topla(3, 5))
print(toplama(3, 5))
print(type(topla))
print(type(toplama))




def benim_fonksiyonum(n):
  return lambda a: a * n

katini_al = benim_fonksiyonum(2)
print(katini_al(5))

katini_al = benim_fonksiyonum(5)
print(katini_al(5))