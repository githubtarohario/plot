#-----------------------------------
#解説のためのサンプルプログラム
#
#---------------------------------------
import tkinter as tk
#-----------------------
# ボタンのイベント
# ------------------------ 
def btn_click():
    #テキストボックスに文字列abcを挿入
    str="Hello!"
    txt_test.delete(0, tk.END)#いったんテキストボックスクリア。0から最後までtk.END
    txt_test.insert(tk.END,str)
 
if __name__ == "__main__":    
    #rootウィンドウを作成
    root = tk.Tk()
    #rootウィンドウのタイトルを設定
    root.title("tkinter")
    #rootウィンドウのサイズを320x240にに設定
    root.geometry("320x240")
    #-------------------------------
    # ラベル　ラベルの文字列を指定
    #--------------------------------
    lbl_test = tk.Label(text='メッセージ')#ラベル名
    lbl_test.place(x=20, y=70)   # 表示位置 
    #---------------
    #メインループ
    #-----------------
    root.mainloop()