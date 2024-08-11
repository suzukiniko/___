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

#
if st.button('始める'):
    def list_image_files(directory):
    """指定ディレクトリ内の画像ファイルのリストを作成する関数"""
    valid_extensions = ('.jpg')
    if not os.path.isdir(directoy):
        raise ValueError(f"{directory} は有効なディレクトリではありません")
    return [f for f in os.listdir(directory) if f.lower().endswith(valid_extensions)]

def display_image_info(image_path):
    """画像のパスを表示する関数"""
    print(f"Please check the image located at: {image_path}")

def ask_question(question, correct_answer):
        #質問を表示してユーザーからの回答を受け付ける関数
        user_answer = input(question + "この人は誰？")
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
correct_answer = selected_image.split('.')[0]  # 拡張子を除いたファイル名を正解として使用






1. インデントと構文エラー
インデントの不整合:
list_image_files と display_image_info 関数が if st.button('始める'): の内部にインデントされておらず、インデントエラーが発生します。また、main 関数内のコードもインデントが正しくありません。

directoy の誤字:
list_image_files 関数内で directoy という誤字があり、正しくは directory です。

2. 入力と出力の問題
print 文:
print 文を使って画像パスや質問を表示していますが、Streamlit アプリケーションでは、st.write や st.image などの Streamlit 関数を使う必要があります。print 文はコマンドライン用です。

ユーザー入力:
input 関数を使用してユーザーの回答を受け取ろうとしていますが、Streamlit では st.text_input を使用してユーザー入力を受け付けるべきです。

3. Streamlit 機能の活用
画像表示:
Streamlit で画像を表示するには、st.image を使うべきです。display_image_info 関数内で画像パスを表示するだけではユーザーが画像を確認できません。

正解の比較:
ask_question 関数はユーザー入力を受け取り、正解と比較していますが、Streamlit アプリケーションでは質問を表示し、ユーザーからの入力を取得する部分を st.text_input を使って実装する必要があります。

改善されたコード例
以下はこれらの問題を修正し、Streamlit の機能を正しく使うように改善したコード例です。

python
コードをコピーする
import streamlit as st
import os
import random

# タイトルを設定
st.title("歴史人物フラッシュゲーム")

st.write("これから様々な歴史上の偉人が表示されるので、できるだけ早く回答してください！")

def list_image_files(directory):
    """指定ディレクトリ内の画像ファイルのリストを作成する関数"""
    valid_extensions = ('.jpg', '.png')  # JPGとPNG両方の拡張子をサポート
    if not os.path.isdir(directory):
        raise ValueError(f"{directory} は有効なディレクトリではありません")
    return [f for f in os.listdir(directory) if f.lower().endswith(valid_extensions)]

def main():
    # 画像ファイルが格納されているディレクトリ
    image_directory = 'images'
    
    # 画像ファイルのリストを取得
    image_files = list_image_files(image_directory)
    
    if not image_files:
        st.write(f"'{image_directory}' ディレクトリに画像ファイルが見つかりません。")
        return

    # ボタンが押されたときにゲームを開始
    if st.button('始める'):
        # ランダムに画像ファイルを選択
        selected_image = random.choice(image_files)
        selected_image_path = os.path.join(image_directory, selected_image)
        
        # 画像を表示
        st.image(selected_image_path, caption='この人は誰？')
        
        # 画像に関する質問と正しい答えを設定
        correct_answer = selected_image.split('.')[0]  # 拡張子を除いたファイル名を正解として使用
        
        # ユーザーからの回答を受け付ける
        user_answer = st.text_input("回答を入力してください:")

        if user_answer:
            if user_answer.strip().lower() == correct_answer.strip().lower():
                st.write("正解です！")
            else:
                st.write("不正解です。正しい答えは:", correct_answer)

if __name__ == "__main__":
    main()
修正点の詳細
ディレクトリの存在確認: directory 引数のタイプミスを修正し、画像ファイルの拡張子も .png を追加しました。
Streamlit の関数使用: 画像の表示には st.image を、ユーザー入力には st.text_input を使用しました。
ゲームの流れ: ボタンを押したときにゲームが開始され、画像が表示され、その後にユーザーが回答できるようにしました。
このように、Streamlit の特性に合わせてコードを修正することで、期待通りに動作するアプリケーションを作成できます。



