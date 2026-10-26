import streamlit as st
import pickle

model = pickle.load(open('model.pkl', 'rb'))

etiketler = ['Zararlı', 'Çok zararlı', 'Müstehcen', 'Tehdit', 'Hakaret', 'Kimliğe yönelik nefret']

st.title('Zararlı Yorum Tespiti :speech_balloon:')

yorum = st.text_area('Yorumu İngilizce yazın:', 'Thank you for your help, this article is really well written.')

if st.button('Analiz Et'):
    p = [x[0][1] for x in model.predict_proba([yorum])]
    durum = 'Zararlı ⚠️' if p[0] > 0.5 else 'Zararlı değil ✅'
    ozet = ' | '.join(f'{ad}: %{o * 100:.1f}' for ad, o in zip(etiketler, p))
    st.success(f'{durum}  ({ozet})')