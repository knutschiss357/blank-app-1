import streamlit as st

# タイトル
st.title("🎈 My new app")

# 自己紹介セクション
st.header("About Me")
st.write("""
最初の第一歩  
Kia ora! My name is Chisato....  
""")

import streamlit as st, random, pandas as pd

st.subheader("Hiragana Bingo (5×5)")
kana = list("あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん")
grid = random.sample(kana, 25)  # 25文字をランダム抽出
df = pd.DataFrame([grid[i*5:(i+1)*5] for i in range(5)], columns=list("ABCDE"))
st.dataframe(df, use_container_width=True)
