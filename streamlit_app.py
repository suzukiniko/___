# Streamlitライブラリをインポート
import streamlit as st

# タイトルを設定
import time

def count_up_timer():
    start_time = time.time()

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        seconds = int(elapsed_time % 60)

        timer_string = f"{hours:02}:{minutes:02}:{seconds:02}"
        
        print(f"\r{timer_string}", end="", flush=True)
        time.sleep(1)

try:
    count_up_timer()
except KeyboardInterrupt:
    print("\nTimer stopped.")
