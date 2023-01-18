def yazdir():
    print("Yazıyorum")

yazdir()




def topla(a, b):
    return a+b

print(topla(3, 5))


def topla_carp(a, b):
    return a + b, a * b

toplam, carpim = topla_carp(3, 5)
print(topla_carp(3, 5))
print(toplam, carpim)




def topla_ne_varsa_git(*a):
    toplam = 0
    for deger in a:
        toplam += deger
    return toplam

print(topla_ne_varsa_git(3, 5, 9, 15.2, 36))




