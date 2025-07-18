import os
import  shutil
from datetime import datetime
uzantilar = {".jpg":"Resimler",".txt":"Metinler",".py":"Python",".pdf":"Belgeler",".zip":"Zip Dosyaları",".rar":"Rar Dosyaları"}

def klasor_dosyalarini_listele(klasor):
        if not os.path.exists(klasor):
            raise FileNotFoundError("Girmiş olduğunuz klasör bulunmuyor.")
        else:       
            return [f for f in os.listdir(klasor) if os.path.isfile(os.path.join(klasor,f))]
        
def klasor_olustur(alt_klasor):
    if not os.path.exists(alt_klasor):
        os.mkdir(alt_klasor)
        return alt_klasor

def klasor_gruplama(klasor):
    dosyalar = klasor_dosyalarini_listele(klasor)
    with open("islemler.log","a",encoding="utf-8") as yazilacak:
        for uzanti in uzantilar:
            dosyalar_uzanti = [dosya for dosya in dosyalar if os.path.splitext(dosya)[1] == uzanti]
            if not dosyalar_uzanti:
                continue
            print(f"{len(dosyalar_uzanti)} tane {uzanti} dosyası bulundu. {uzantilar[uzanti]} dosyasına taşınacak.")                
            while True:
                secim = input("Devam etmek istiyor musunuz? (e/h)").lower()
                if secim == "e":
                    tarih = datetime.now().strftime("%Y-%m-%d %H:%M")
                    hedef_yol = klasor_olustur(os.path.join(klasor,uzantilar[uzanti]))
                    for dosya in dosyalar_uzanti:
                        tam_yol = os.path.join(klasor,dosya)
                        shutil.move(tam_yol,hedef_yol)
                        yazilacak.write(f"{tarih} {dosya} --> {hedef_yol}")
                    print("İşlem tamamlandı.")                 
                    break
                elif secim == "h":
                    break
                else:
                    print("Yanlış seçim yapıldı.")
           
def ana():
    klasor_yolu = input("Lütfen klasörünüzü yol olarak giriniz...").replace("\\","/").strip('"')
    klasor_gruplama(klasor_yolu)

if __name__=="__main__":
    ana()

            
        
