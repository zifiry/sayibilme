import streamlit as st
while True:
    b = input("Aklınızdan bir sayı tutun: ").strip().lower()

    # 1) Özel kelimeler
    if b == "ege":
        print("bravo kardeşim ege çakmağı buldun ve ondan bir öpücük kazandın")
    elif b == "furkan":
        print("yamukluk sınırını aştınız nolur kendinize gelin!")
    elif b == "yiğit":
        print("moruk sen beat yap ben geliyom")
    elif b == "yavuz":
        print("kanka uykum var plan iptal")
    elif b == "defne":
        print("uyanamadım ilk dersi kaçırdım devamsızlıktan kalıcam")
    elif b == "doğan":
        print("moruk tavla malatya kayısı falan ya")
        # 2) Sayı mı değil mi
    try:
        a = int(b)
    except ValueError:
        print("Sayı ya da özel kelime gir.")
        continue

    son = a % 10
    if a==31 :
        print("ne kadar komik anasını siktiğim ")
    elif a<0:
        print("he amk bi akıllı sensin de negatif tutuyon")
    elif a==0:
        print("aferin harezmi kılıklı orospu evladı seni")
        break
    elif a==36 :
        print("36, ananın amı yarrrama battı xD")
    elif a==44 :
         print("doğan demir 44 malatya saygılar....")
    elif a==69 :
        print("annen de çok sever orospucocu")
    elif 0<a<18 :
        print("tam senlik sayılar sübyancı herif")
    elif son in   (0,6,-6):
        print("tuttuğunuz sayı" , a , "mı?????")
    elif son in(1,2,5,7,8,-1,-2,-5,-7,-8):
        print("tuttuğunuz sayı" , a , "mi?????")
    elif son in(3,4,-3,-4):
        print("tuttuğunuz sayı" , a , "mü?????")
    elif son in(9,-9):
        print("tuttuğunuz sayı" , a , "mu?????")
    
