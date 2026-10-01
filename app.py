import streamlit as st

OZEL_KELIMELER = {
    "ege": "bravo kardeşim ege çakmağı buldun ve ondan bir öpücük kazandın",
    "furkan": "yamukluk sınırını aştınız nolur kendinize gelin!",
    "yiğit": "moruk sen beat yap ben geliyom",
    "yavuz": "kanka uykum var plan iptal",
    "defne": "uyanamadım ilk dersi kaçırdım devamsızlıktan kalıcam",
    "doğan": "moruk tavla malatya kayısı falan ya",
}

def cevap_ver(b):
    b = b.strip().lower()

    # 1) Özel kelimeler
    if b in OZEL_KELIMELER:
        return OZEL_KELIMELER[b]

    # 2) Sayı mı değil mi
    try:
        a = int(b)
    except ValueError:
        return "Sayı ya da özel kelime gir."

    son = a % 10

    # 3) Özel sayılar (en özelden genele)
    if a == 31:
        return "aklın fikrin 31 "
    elif a < 0:
        return "aferin kanka eksili tuttun çok zekisin"
    elif a == 0:
        return "bravo sana harezmi orospu cocu"
    elif a == 36:
        return "36,ananın amı sikimde kaldı"
    elif a == 44:
        return "doğan demir 44 malatya saygılar...."
    elif a == 69:
        return "annen sever 69"
    elif 0 < a < 18:
        return "niye",a,"kanka sevgilinin yaşı mı"
    # 4) Genel durum: soru eki
    elif son in (0, 6):
        return f"Tuttuğunuz sayı {a} mı?????"
    elif son in (1, 2, 5, 7, 8):
        return f"Tuttuğunuz sayı {a} mi?????"
    elif son in (3, 4):
        return f"Tuttuğunuz sayı {a} mü?????"
    else:
        return f"Tuttuğunuz sayı {a} mu?????"


st.title("Sayı Tahmin")

with st.form("tahmin_formu", clear_on_submit=True):
    giris = st.text_input("Aklınızdan bir sayı tutun:")
    gonder = st.form_submit_button("Tahmin et")

if gonder and giris:
    st.write(cevap_ver(giris))
