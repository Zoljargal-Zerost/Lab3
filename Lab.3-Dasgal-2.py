ner = input("Таны бүтэн нэр: ")
nershil = input("Таны нэршил: ")

index = int(input("Таны бүтэн нэрэнд таны товчилсон нэрийн ямар дугаарт байгаа үсгийг хайх вэ?: "))

if index <= len(nershil):
    letter = nershil[index - 1]
    position = ner.find(letter)
    print(f"{index} дугаар дахь үсэг {position + 1} дугаар дээр олдлоо")
else:
    print("Товчилсон нэрийн дугаар хэтрээд байна.")
