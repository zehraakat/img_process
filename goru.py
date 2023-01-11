try:
  from.google.colab import drive
  drive.mount('/content/drive')

except:
  ImportError
  print("Error!!!!")

# kütüphaneler
''' import cv2 
    import numpy as np
    import matplotlib.pyplot as plt '''

# okuyacağımız görüntüyü bir değişkene aktarıyoruz.
''' resim1 = cv2.imread('/content/drive/lights.jpg') '''

# ekrana bastırıyoruz. Ama BGR formatında gelcek (yani kırmızı yerler mavi olur)
''' plt.imshow(resim1)
    plt.show() '''

#  RGB formatına dönüştürüyoruz. Bunu yaparken de bi değişkene ata(orijinal forma)
''' resim2 = cv2.cvtColor(resim1,cv2.COLOR_BGR2RGB)
    plt.imshow(resim2)
    plt.show() '''

# Boyutlara bak.
''' print(resim2.shape) '''

# renk değerlerine bak. o pikselde kaç birim renk var 
''' renk = resim2[25,120]
    print(renk) '''
# çıktının [149 134 129] olması lazım.

# bu pikselleri değişkenlere atadık.
''' kirmizi = resim2[25,120,0]
    print('kirmizi:',kirmizi)

    yesil = resim2[25,120,1]
    print('yesil:',yesil)

    mavi = resim2[25,120,2]
    print('mavi:',mavi) ''',
