import re

result = dir(re)

# re module

str = "Selim Tekin Selim Python 40 saat"

# re.findAll()
result = re.findall("Selim", str)
result = len(result)

#re.split()
result = re.split(" ", str)
result = re.split("T", str) # T'den böler fakat T'yi yazmaz

# re.sub()
result = re.sub(" ", "-",str) # boşlukları "-" ifadesi ile değiştirir
result = re.sub("\s","-", str) # aynı

# re.search()
result = re.search('Selim',str) #re.Match objesi döndürdü çıktıda span=(0,5) ifadesi de yer alır.(pattern'in(Selim) bulunduğu konum)
# result = result.span() # Çıktı: (0, 5)
# result = result.start() # Çıktı: 0
# result = result.end() # Çıktı: 5
# result = result.group() # Çıktı: Selim
result = result.string # Çıktı: Selim Tekin Selim (yani Selim'i nerede arıyor onun cevabı)

# regular Expression
'''

    [abc] => a: 1 match
             ac: 2 match
             Python: No match

    [a-e] => [abcde]
    [1-5] => [12345]
    [0-39] => [01239] # 0-3 arası arar 9 orada sabit kalır

    [^abc] => abc dışındaki karakterler
    [^0-9] => rakam olmayan karakterler

'''

result = re.findall("[abc]",str) # ['a', 'a']
result = re.findall("[sat]",str) # ['t', 's', 'a', 'a', 't']
result = re.findall("[a-e]",str) # abcde ' yi arar
result = re.findall("[a-z]",str) # a'dan z'ye kadar arar
result = re.findall("[0-5]",str) # 1-5 arasındakileri arar ['4', '0']
result = re.findall("[^abc]",str) # abc dışındakileri arar
result = re.findall("[^0-9]",str) # rakam haricindekileri arar

'''

    . - Herhangi bir tek karakteri belirtir.

        .. => a: No match       # ".." 2 basamaklı herhangi bir ifadeyi arar. "a" tek karakter olduğu için eşleşme bulunamaz
              ab: 1 match       # "ab" 2 karakterli 1 eşleşme
              abc: 1 match      # "abc" 2 karakter barındırdığı için 1 eşleşme
              abcd: 2 match     # "abcd" 2 adet 2 karakter barındırdığı için 2 eşleşme ("ab" ve "cd")

'''

result = re.findall("...", str) # Boşluklar dahil 3 basamaklıları arar. # Çıktı: ['Sel', 'im ', 'Tek', 'in ', 'Sel', 'im ', 'Pyt', 'hon', ' 40', ' sa']
result = re.findall("Py..on", str) # Noktaların yerine "ab" de olsa yine döner # Çıktı: ['Python']

'''

    ^ - Belirtilen string karakterlerle başlıyor mu ?

    ^a => a: 1 match
         abc: 1 match
         bac: No match

'''

result = re.findall("^P", str) # str ifadesi P ile başlıyor mu # Çıktı: []

'''

    $ - Belirtilen string karakterlerle bitiyor mu ?

    a$ => a: 1 match
         lamba: 1 match
         Python: No match

'''

result = re.findall("t$", str) # t ile mi bitiyor ? # Çıktı: ['t']
result = re.findall("saat$", str) # Çıktı: ['saat']
result = re.findall("saatt$", str) # Çıktı: []

'''

    . - Bir karakterin 0 ya da daha fazla sayıda olmasını kontrol eder.

    ma*n => mn: 1 match
         man: 1 match
         maan: 1 match
         main: No match (a'nı arkasına n gelmiyor)

'''

result = re.findall("sa*t", str) # a'dan 0 ya da daha fazla olmasını kontrol eder. # Çıktı: ['saat']

'''

    + - Bir karakterin 1 ya da daha fazla sayıda olmasını kontrol eder.

    ma+n => mn: No match
         man: 1 match
         maan: 1 match
         main: No match (a'nı arkasına n gelmiyor)

'''

result = re.findall("sa+t", str) # a'dan 1 ya da daha fazla olmasını kontrol eder. # Çıktı: ['saat']

'''

    ? - Bir karakterin 0 ya da 1 kez olmasını kontrol eder.

    ma?n => mn: 1 match
         man: 1 match
         maan: No match
         main: No match (a'nı arkasına n gelmiyor)

'''

result = re.findall("sa?t", str) # a'dan 0 ya da 1 kez olmasını kontrol eder. a'dan 2 tane var. # Çıktı: []

'''

    {} - Karakter sayısını kontrol eder.

         al{2} => a karakterinin arkasına l 2 kez tekrarlamalı
         al{2,3} => a karakterinin arkasına l en az 2 en fazla 3 kez tekrarlamalı
         [0-9]{2,4} => en az 2 en çok 4 basamaklı sayları geri getirir

'''

result = re.findall("a{2}", str) # Çıktı: ['aa']
result = re.findall("[0-9]{2}", str) # Çıktı: ['40']

'''

    | - Alternatif seçeneklerden birinin gerçekleşmesi gerekir

        a|b => a ya da b
               
               cde => No match
               ade => 1 match
               acdbea => 3 match

'''

'''

    () - Gruplamak için kullanılır.

        (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir. (axz, bxz, cxz olur)

'''

'''

    \ - Özel karakterleri aramamızı sağlar.
        \$a => $ karakterinin arkasına a karakterini arar. Yani $ regular exp. engine tarafından yorumlanmaz.

    \A - Belirtilen karakter stringin başında mı ?
        \Athe => the stringin başında mı ?

    \Z - Belirtilen karakter stringin sonunda mı ?
        the\Z => the stringin sonunda mı ?

        result = re.findall("\ASelim", str) # Çıktı: ['Selim']
        result = re.findall("saat\Z", str) # Çıktı: ['saat']

    \b - Belirtilen karakter kelimenin en başında ya da sonunda mı ?
          \bthe => the kelimenin en başında mı ?
          the\b => the kelimenin en sonunda  mı ?

    \B - Belirtilen karakter kelimenin en başında ya da sonunda değil mi ?
          \Bthe => the kelimenin en başında değil mi ?
          the\B => the kelimenin en sonunda  değil mi ?

    \d - [0-9] ile aynı anlama gelir yani rakamları arar.
         \d => 12abc34 (1234 döndürür)

    \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
         \D => 1ab44_50 (ab_ döndürür)

    \s - Boşluk karakterlerini arar.
    \S - Boşluk karakterleri dışındakiler.
    \w - Alfabetik karakterler , rakamlar ve alt çizgi karakteri.
    \s - \w ' nin tam tersi
'''

print(result)