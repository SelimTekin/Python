with open("newfile.txt", "r", encoding="utf-8") as file: # close() fonksiyonuna gerek kalmaz bu şekilde. Kendisi kapanır blok bitince
    content = file.read(10)
    print(content)
    file.seek(0) # cursor 0. konuma gider
    print(file.tell()) # tell() fonksiyonu cursor'ın kaçıncı karakterde olduğunu söyler
    content2 = file.read(10)
    print(content2)