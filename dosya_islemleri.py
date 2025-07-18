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
        toplam = 0
        for uzanti in uzantilar:
            dosyalar_uzanti = [dosya for dosya in dosyalar if os.path.splitext(dosya)[1] == uzanti]
            uzantı_adet = len(dosyalar_uzanti)
            toplam += uzantı_adet
            if not dosyalar_uzanti:
                continue
            print(f"{uzantı_adet } tane {uzanti} dosyası bulundu.")                
            while True:
                print("""1- Taşı
                    2- Kopyala
                    3- Atla""")
                secim = input("Seçiminizi yapınız:")
                if secim == "1":
                    for dosya in dosyalar_uzanti: 
                        klasor_olustur("tasinacak/")   
                        hedef_yol = os.path.join("tasinacak",dosya)
                        tam_yol = os.path.join(klasor,dosya)
                        shutil.move(tam_yol,hedef_yol)
                    yazilacak.write(f"{uzantı_adet} tane {uzanti} dosyası {datetime.now().strftime("%Y-%m-%d %H:%M")} tarihinde taşındı.")
                    break
                elif secim == "2":
                    for dosya in dosyalar_uzanti:
                        tam_yol = os.path.join(klasor,dosya)
                        klasor_olustur("kopyalanacak/")
                        hedef_yol = os.path.join("kopyalanacak",dosya)
                        shutil.copy(tam_yol,hedef_yol)
                    yazilacak.write(f"{uzantı_adet} tane {uzanti} dosyası {datetime.now().strftime("%Y-%m-%d %H:%M")} tarihinde kopyalandı.")
                    break
                elif secim == "3":
                    pass
                else:
                    print("Hatalı seçim yapıldı.")
            


         
def ana():
    klasor_yolu = input("Lütfen klasörünüzü yol olarak giriniz...").replace("\\","/").strip('"')
    klasor_gruplama(klasor_yolu)

if __name__=="__main__":
    ana()

            
        
