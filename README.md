# Metin Dosyasını Sese Dönüştürme Projesi

Bu Python projesi, bir `.txt` dosyasındaki metni **Google Text-to-Speech (gTTS)** kullanarak ses dosyasına dönüştürür ve oynatır

---

## Gereksinimler

Bu projeyi çalıştırabilmek için aşağıdaki araçlara ihtiyacınız var:
 
- **gTTS Kütüphanesi**  
- İşletim sistemi uyumlu bir medya oynatıcı:
  - **Windows:** `os.system("start ...")`
  - **Linux:** `os.system("xdg-open ...")`
  - **macOS:** `os.system("open ...")`

---

## Kurulum

Projenizi kolayca kurmak için şu adımları takip edin:

**Repoyu klonlayın veya indirin:**
   ```bash
   git clone https://github.com/MiracKayikci/Python-TTS-.txt-To-.mp3.git
   ```
**Gerekli kütüphaneyi yükleyin:**
  ```bash
  pip install gtts
  ```
**Metin dosyanızı hazırlayın:**

Projenin bulunduğu dizinde bir ```deneme.txt``` dosyası oluşturun ve seslendirmek istediğiniz metni bu dosyaya ekleyin.

**Dil Ayarı:**

Varsayılan dil Türkçeolarak ayarlanmıştır (lang="tr"). Eğer başka bir dil kullanmak istiyorsanız, kodun şu satırını değiştirin:



