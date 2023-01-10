import tkinter as tk
from tkinter import filedialog
import platform

# https://blog.sakaki333.com/blog/view/84
def set_invisible():
    root = tk.Tk() # ダイアログ用のルートウィンドウの作成
    root.geometry("0x0") # ウィンドウサイズを0にする（Windows用の設定）
    root.overrideredirect(1) # ウィンドウのタイトルバーを消す（Windows用の設定）
    root.withdraw() # ウィンドウを非表示に
    system = platform.system()
    if system == "Windows":
        root.deiconify()

set_invisible()

# 入力ファイルの選択
input_filepaths = filedialog.askopenfilenames()
if len(input_filepaths) == 0:
    exit()
input_filepaths = list(input_filepaths)

# 出力ファイルの選択
output_filepath = filedialog.asksaveasfilename()
if len(output_filepath) == 0:
    exit()

# 書き込み
with open(output_filepath, mode='w', encoding='utf-8') as output_file:
    for i, input_filepath in enumerate(input_filepaths):
        if i != 0: output_file.write('\n')
        with open(input_filepath, encoding='utf-8') as input_file:
            output_file.write(input_file.read())