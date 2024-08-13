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
        st.error(f"{directory} は有効なディレクトリではありません")
        return []
    return [f for f in os.listdir(directory) if f.lower().endswith(valid_extensions)]

def main():
    # 画像ファイルが格納されているディレクトリ
    image_directory = '/workspaces/___/easy'
    
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