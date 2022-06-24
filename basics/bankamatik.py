# Bankamatik Uygulaması

SelimHesap = {
    'hesapNo': '123456',
    'ad': 'Selim Tekin',
    'bakiye': 3000,
    'ekHesap': 2000
}

YavuzHesap = {
    'hesapNo': '123456789',
    'ad': 'Yavuz Tekin',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('paranızı alabilrsiniz')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if(toplam >= miktar):
            ekHesapKullanimi = input('Ek hesap kullanılsın mı? (e/h)')

            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('paranızı alabilirsiniz')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} no'lu hesabınızda {hesap['bakiye']} TL bulunmaktadır.")
                print(f"{hesap['hesapNo']} no'lu ek hesabınızda {hesap['ekHesap']} TL bulunmaktadır.")
        else:
            print("üzgünüz bakiye yetersiz")
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} no'lu hesabınızda {hesap['bakiye']} TL bulunmaktadır.Limtiniz ise {hesap['ekHesap']} TL'dir.")

paraCek(SelimHesap, 4000)

print("***************")

paraCek(SelimHesap, 3000)