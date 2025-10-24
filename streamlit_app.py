import streamlit as st
import random
import pandas as pd

# -------------------------------
# 💬 自己紹介セクション
# -------------------------------
st.title("🎈 My App")

st.header("About Me")
st.write("""
最初の第一歩

言語学習・習慣管理・タスク管理に使えるアプリを作ってみたいです。

""")
  
  
  
  

# -------------------------------
# 🅱️ ひらがなビンゴセクション
# -------------------------------
st.subheader("Hiragana Bingo (5×5)")

# 状態管理（何回目のリロードか）
if "refresh" not in st.session_state:
    st.session_state.refresh = 0

rng = random.Random(st.session_state.refresh)
kana = list("あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん")
grid = rng.sample(kana, 25)
df = pd.DataFrame([grid[i*5:(i+1)*5] for i in range(5)], columns=list("ABCDE"))

# 正方形・左寄せテーブルを作成
html = "<table style='border-collapse: collapse; margin-left:0;'>"
for row in df.itertuples(index=False):
    html += "<tr>"
    for cell in row:
        html += ("<td style='border:1px solid #aaa; width:70px; height:70px; "
                 "text-align:center; font-size:24px;'>{}</td>").format(cell)
    html += "</tr>"
html += "</table>"

# ① まずビンゴ表を表示
st.markdown(html, unsafe_allow_html=True)

# ② その下にボタンを配置（押すとリロード）
if st.button("🎲 新しいビンゴカードを作る"):
    st.session_state.refresh += 1
    st.rerun()
