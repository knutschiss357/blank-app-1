import streamlit as st

# タイトル
st.title("🎈 My new app")

# 自己紹介セクション
st.header("About Me")
st.write("""
最初の第一歩  
Kia ora! My name is Chisato....  
""")

import streamlit as st
import random
import pandas as pd

st.subheader("🅱️ Hiragana Bingo (5×5)")

# ひらがなリスト
kana = list("あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん")
grid = random.sample(kana, 25)

# DataFrame化
df = pd.DataFrame([grid[i*5:(i+1)*5] for i in range(5)], columns=list("ABCDE"))

# HTMLテーブルを自作（セルを正方形に）
html = "<table style='border-collapse: collapse; margin:auto;'>"
for row in df.itertuples(index=False):
    html += "<tr>"
    for cell in row:
        html += f"<td style='border:1px solid #aaa; width:70px; height:70px; text-align:center; font-size:24px;'>{cell}</td>"
    html += "</tr>"
html += "</table>"

st.markdown(html, unsafe_allow_html=True)
