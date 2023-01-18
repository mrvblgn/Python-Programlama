liste = ["Elma", "Armut", "Ayva"]

liste.sort()
print(liste)

liste.reverse()
print(liste)

def fonksiyon(n):
  return abs(n - 50)

sayi_listesi = [50, 350, 43, 68, 21]
sayi_listesi.sort(key=fonksiyon)
print(sayi_listesi)