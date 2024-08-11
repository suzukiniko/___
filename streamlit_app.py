# Streamlitライブラリをインポート
import streamlit as st
import pandas as pd
import numpy as np
import os
import random
import time
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

#
if st.button('始める'):
    def list_image_files(directory):
    #指定ディレクトリ内の画像ファイルのリストを作成する関数
    validextensions = ('.jpg')
    return [f for f in os.listdir(directory) if f.lower().endswith(validextensions)]

    def display_image_info(image_path):
    #画像のパスを表示する関数
    print(f"Please check the image located at: {image_path}")

    def ask_question(question, correct_answer):
        #質問を表示してユーザーからの回答を受け付ける関数
        user_answer = input(question + " ")
        return user_answer.strip().lower() == correct_answer.strip().lower()

    def main():
    # 画像ファイルが格納されているディレクトリ
        image_directory = 'images'
    
    # 画像ファイルのリストを取得
        image_files = list_image_files(image_directory)
    
        if not image_files:
            print(f"No image files found in directory '{image_directory}'.")
            return
    
    # ランダムに画像ファイルを選択
        selected_image = random.choice(image_files)
        selected_image_path = os.path.join(image_directory, selected_image)
    
    # 画像に関する質問と正しい答えを設定
    # ここでは画像ファイル名を正解として利用する例
        question = 'What is the name of this image file?'
        correct_answer = selected_image.split('.')[0]  # 拡張子を除いたファイル名を正解として使用