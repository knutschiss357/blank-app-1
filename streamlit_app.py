import streamlit as st

# タイトル
st.title("🎈 My new app")

# 自己紹介セクション
st.header("About Me")
st.write("""
Kia ora! My name is Chisato.  
I’m a Japanese Language Adviser based in New Zealand, supporting teachers and promoting Japanese language education.  
I’m passionate about language learning, cultural exchange, and building connections through communication.
""")

# 画像を追加（同じフォルダに "profile.jpg" を置く場合）
st.image("profile.jpg", caption="こんにちは！Chisatoです", width=300)

# 追加のメッセージ
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
