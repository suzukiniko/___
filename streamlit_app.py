# Streamlitライブラリをインポート
import streamlit as st

# タイトルを設定
    st.title("BMI診断")

    st.write("身長と体重を入力してください。")
    weight=st.text_input("体重")
    tall=st.text_imput("身長")
    bmi= weight / ( tall * tall )
    st.write("あなたのBMIは"+str(bmi)+です。)