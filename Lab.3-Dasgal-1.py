ovog = input("Таны овог: ")
ner = input("Таны нэр: ")
nernii_urt = len(ner)
try:
    nas = int(input("Нас: "))
except ValueError:
    print("Алдаа: Насаа зөв оруулна уу.")
    nas = 0

uguulber = "Сайн байна уу. Таны овог нэр: " + ovog + " " + ner + ", таны нас: " + str(nas)

print(uguulber)
print("Тантай танилцахад таатай байна.")
print("Таны нэрийн урт: " + str(nernii_urt))
print("Таны нэрийн текст өгөгдлийн төрөл: ", type(ner))
print("Таны нас өгөгдлийн төрөл: ", type(nas))
