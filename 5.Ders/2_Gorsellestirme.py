
"""
1 - veri isimli bir klasör oluşturun
2 - zip dsosyasını veri klasörüne çıkartın
3 - zip dosyası içindeki csv dosyalarının tüm içeriğini
    tek bir csv dosyasında birleştirin
    volume olmasın
4 - bu kayıtların tamamını sqlite veritabanına bir tablo
    oluşturarak yükleyin
5 - kullanıcının belirlediği paritenin
    kullanıcının belirlediği aralığının
    kullanıcının belirlediği değerin
    grafiğini çizdirin (veriler sqlite tan çekilecek).
"""

import sqlite3
import matplotlib.pyplot as plt

bag = sqlite3.connect("kripto.vt")
cursor = bag.cursor()

parite = "AVAXUSDT"
bas_tarih = "2022-02-04"
bitis_tarih = "2023-01-01"

sorgu = "SELECT * FROM parite WHERE " \
        "(otime BETWEEN '"+bas_tarih+"' " \
        "AND '"+bitis_tarih+"') " \
        "AND parite='"+parite+"'"
cursor.execute(sorgu)
sonuc = cursor.fetchall()
liste_x = []
liste_y = []
for mum in sonuc:
    liste_y.append(mum[6])
    liste_x.append(mum[2])

plt.plot(liste_x, liste_y)
plt.show()
bag.close()

