# streamlit_template

## 概要
Streamlitを使用して開発するためのテンプレートです。このテンプレートは「Public」で作成することを推奨します

## 特徴
- Streamlitを使用した開発に特化した初学者用のテンプレート
- Python、Streamlitの基本的な使い方を学ぶことができます

## 使用方法
1. リポジトリをクローンまたはダウンロードします
2. Streamlitのマイページから、デプロイしてください（ https://streamlit.io/ ）




Pythonの標準ライブラリだけを使用して、複数の画像からランダムに1つを選び、その画像に関するクイズを出題するプログラムを作成することは可能です。以下のコードは、指定されたディレクトリ内の複数の画像からランダムに1つを選び、その画像のファイルパスを表示し、クイズを出題する方法を示しています。

コード例: 複数の画像からランダムに選んでクイズを出題する
このコードでは、画像のファイルパスを表示し、ユーザーにその画像に関する質問を出題します。画像自体の表示は行いませんが、画像のパスを表示することで、ユーザーが手動で画像を確認することができます。

python
コードをコピーする
import os
import random

def list_image_files(directory):
    """指定ディレクトリ内の画像ファイルのリストを作成する関数"""
    valid_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
    return [f for f in os.listdir(directory) if f.lower().endswith(valid_extensions)]

def display_image_info(image_path):
    """画像のパスを表示する関数"""
    print(f"Please check the image located at: {image_path}")

def ask_question(question, correct_answer):
    """質問を表示してユーザーからの回答を受け付ける関数"""
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
    
    # 画像のパスを表示
    display_image_info(selected_image_path)

    # 質問を表示してユーザーの回答を確認
    if ask_question(question, correct_answer):
        print("Correct!")
    else:
        print("Incorrect. The correct answer was:", correct_answer)

if __name__ == "__main__":
    main()
説明
list_image_files 関数:

指定されたディレクトリ内の画像ファイルをリストアップします。サポートされている画像形式は .png, .jpg, .jpeg, .gif, .bmp です。
display_image_info 関数:

画像ファイルのパスをユーザーに表示します。ユーザーはこのパスを使って手動で画像を確認することができます。
ask_question 関数:

ユーザーに質問を出し、その回答が正しいかどうかを判定します。
main 関数:

画像ファイルが保存されているディレクトリを指定し、ディレクトリ内の画像ファイルからランダムに1つを選びます。
選択した画像ファイルのパスを表示し、その画像に関する質問を出題します。
使用方法
画像ファイルの準備:

images という名前のディレクトリを作成し、その中にクイズで使用する画像ファイルを保存します。
スクリプトの実行:

上記のコードをPythonファイル（例: quiz.py）として保存し、ターミナルやコマンドプロンプトで実行します。
bash
コードをコピーする
python quiz.py
このコードは、指定されたディレクトリ内の画像からランダムに1つを選び、その画像のファイル名に関する質問を出題します。画像自体の表示は行いませんが、画像のパスを表示してユーザーにその画像を確認してもらうことができます。