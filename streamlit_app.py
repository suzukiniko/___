# Streamlitライブラリをインポート
import streamlit as st

# タイトルを設定
st.title("BMI診断")

st.write("身長と体重を入力してください。")
weight=st.number_input("体重",min_value=1.0)
tall=st.number_input("身長",min_value=1.0)
if st.button("BMIを計測"):
    bmi=weight/tall**2
    rounded_bmi=round(bmi, 2)
st.write("あなたのBMIは"+str(bmi)+"です。")