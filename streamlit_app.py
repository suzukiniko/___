# Streamlitライブラリをインポート
import streamlit as st
import re
# タイトルを設定
st.title("歴史人物フラッシュゲーム")

st.write("これから様々な歴史上の偉人が表示されるので、できるだけ早く回答してください！")
#背景色の設定
st.write(
    f"""
    <style>
        .stApp{{
            background-color: #abced8;
        }}
    </style>
    """,
    unsafe_allow_html=True
)