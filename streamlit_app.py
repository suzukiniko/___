# Streamlitライブラリをインポート
import streamlit as st
import random

# タイトルを設定
st.title("おみくじアプリ")

#結果に応じたコメントやアドバイス
comments={
    "大吉":"おめでとう！素晴らしい一日になりそうです！！",
    "吉":"一日ラッキーな日になるでしょう。",
    "中吉":"良いことがおこるかも？",
    "小吉":"何もない一日になるといいですが...",
    "凶":"周りに気をつけましょう。",
    "大凶":"生きて帰れるといいですね^^",
    }

if  st.button("おみくじを引く"):
    results=["大吉","吉","中吉","小吉","凶","大凶"]
    result=random.choice(results)
    st.write(f"結果:{result}"
    comments)

