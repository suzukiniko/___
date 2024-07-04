# Streamlitライブラリをインポート
import streamlit as st

# タイトルを設定
import plotly.express as px

# データフレームを作成
df = px.data.gapminder().query("country=='Japan'")

# 地図を描画
fig = px.scatter_geo(df, locations="iso_alpha",
                     size="pop", # ポイントのサイズを人口に応じて変える
                     )

# 地図を表示
fig.show()
