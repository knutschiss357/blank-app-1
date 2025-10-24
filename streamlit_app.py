import streamlit as st
import random
import pandas as pd

# -------------------------------
# 💬 自己紹介セクション
# -------------------------------
st.title("🎈 My App")

st.header("About Me")
st.write("""
Kia ora! My name is Chisato.  
言語学習につかえるアプリを作ってみたいです。
""")

# st.image("profile.jpg", caption="こんにちは！Chisatoです", width=300)
# ↑ 画像を入れない場合はこの行を削除またはコメントアウト！

# -------------------------------
# 🅱️ ひらがなビンゴセクション
# -------------------------------
st.subheader("Hiragana Bingo (5×5)")

kana = list("あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん")
grid = random.sample(kana, 25)
df = pd.DataFrame([grid[i*5:(i+1)*5] for i in range(5)], columns=list("ABCDE"))

html = "<table style='border-collapse: collapse; margin-left:0;'>"
for row in df.itertuples(index=False):
    html += "<tr>"
    for cell in row:
        html += f"<td style='border:1px solid #aaa; width:70px; height:70px; text-align:center; font-size:24px;'>{cell}</td>"
    html += "</tr>"
html += "</table>"

st.markdown(html, unsafe_allow_html=True)

# 🎲 ボタンで再生成（オプション）
if st.button("🎲 新しいビンゴカードを作る"):
    st.experimental_rerun()
