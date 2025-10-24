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
日本語学習に使えるアプリを作ってみたいです。
""")

# -------------------------------
# 🅱️ ひらがなビンゴセクション
# -------------------------------
st.subheader("Hiragana Bingo (5×5)")

# ボタンでリロード（新しいカード生成）
if "refresh" not in st.session_state:
    st.session_state.refresh = 0
if st.button("🎲 新しいビンゴカードを作る"):
    st.session_state.refresh += 1

rng = random.Random(st.session_state.refresh)
kana = list("あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん")
grid = rng.sample(kana, 25)
df = pd.DataFrame([grid[i*5:(i+1)*5] for i in range(5)], columns=list("ABCDE"))

# 正方形・左寄せテーブル
html = "<table style='border-collapse: collapse; margin-left:0;'>"
for row in df.itertuples(index=False):
    html += "<tr>"
    for cell in row:
        html += ("<td style='border:1px solid #aaa; width:70px; height:70px; "
                 "text-align:center; font-size:24px;'>{}</td>").format(cell)
    html += "</tr>"
html += "</table>"

st.markdown(html, unsafe_allow_html=True)
