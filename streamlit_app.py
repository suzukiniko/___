# Streamlitライブラリをインポート
import streamlit as st

# タイトルを設定
import tempfile
import webbrowser
from PIL import Image, ImageDraw

# 仮の画像を作成する（例として赤い四角形を描画）
image = Image.new('RGB', (200, 200), color='blue')
draw = ImageDraw.Draw(image)
draw.rectangle([50, 50, 150, 150], fill='red')

# 一時ファイルに保存する
temp_image_path = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
image.save(temp_image_path.name)
temp_image_path.close()

# 一時ファイルをブラウザで開く
webbrowser.open('file://' + temp_image_path.name)

