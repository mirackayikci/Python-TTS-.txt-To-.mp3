from gtts import gTTS
import os
from os import path

def dosyaVarmi(dosya):
    return path.exists(dosya)

# Buradaki "tr" ifadesini istediğiniz dilin koduyla değiştirin
dosya = open("deneme.txt", "r", encoding="utf-8")
yazi = dosya.read()
cikti = gTTS(text=yazi, lang="tr", slow=False)

if dosyaVarmi("deneme.mp3"):
    print("Önceki ses dosyası siliniyor...")
    os.remove("deneme.mp3")

print("Yeni ses dosyası oluşturuluyor...")
cikti.save("deneme.mp3")
print("Seslendiriliyor...")
os.system("start deneme.mp3")


dosya.close()