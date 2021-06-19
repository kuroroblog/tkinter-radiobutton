import tkinter as tk


class Application(tk.Frame):
    # 現在選択されているラジオボタンの値を格納する変数
    variable = None

    # 現在選択されているラジオボタンの値を確認する関数
    def showValue(self):
        # get() : 現在選択されているラジオボタンの値を取得する関数
        print("You selected the option " + self.variable.get())

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")

        # Windowを親要素として、frame Widget(Frame)を作成する。
        # frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)

        # Windowを親要素とした場合に、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # 現在選択されているラジオボタンの値を文字列変数として扱う。
        # StringVarについて : https://kuroro.blog/python/K53voPjJuKFfYrjmP8FP/
        self.variable = tk.StringVar()
        # set() : 初期値としてBの値を設定する。
        self.variable.set('B')

        # frame Widget(Frame)を親要素として、Aのradiobutton Widgetを作成する。
        # variable : 現在選択中のラジオボタンの値を格納する。文字列変数(self.variable)として値を持たせることで、可変として扱い、その他のラジオボタンへ値を共有して選択の状態を管理できる。
        # value : ラジオボタン自身が持つ値の設定。Aとする。
        # text : ラジオボタンを説明するテキスト。Option Aとする。
        # command : ラジオボタンが選択された場合に実行する関数を設定する。self.showValue関数を設定する。
        self.aButton = tk.Radiobutton(frame, variable=self.variable, value='A', text='Option A', command=self.showValue)

        # frame Widget(Frame)を親要素とした場合に、Aのradiobutton Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.aButton.pack()

        # frame Widget(Frame)を親要素として、Bのradiobutton Widgetを作成する。
        # variable : 現在選択中のラジオボタンの値を格納する。文字列変数(self.variable)として値を持たせることで、可変として扱い、その他のラジオボタンへ値を共有して選択の状態を管理できる。
        # value : ラジオボタン自身が持つ値の設定。Bとする。
        # text : ラジオボタンを説明するテキスト。Option Bとする。
        # command : ラジオボタンが選択された場合に実行する関数を設定する。self.showValue関数を設定する。
        self.bButton = tk.Radiobutton(frame, variable=self.variable, value='B', text='Option B', command=self.showValue)

        # frame Widget(Frame)を親要素とした場合に、Bのradiobutton Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.bButton.pack()

        # frame Widget(Frame)を親要素として、Cのradiobutton Widgetを作成する。
        # variable : 現在選択中のラジオボタンの値を格納する。文字列変数(self.variable)として値を持たせることで、可変として扱い、その他のラジオボタンへ値を共有して選択の状態を管理できる。
        # value : ラジオボタン自身が持つ値の設定。Cとする。
        # text : ラジオボタンを説明するテキスト。Option Cとする。
        # command : ラジオボタンが選択された場合に実行する関数を設定する。self.showValue関数を設定する。
        self.cButton = tk.Radiobutton(frame, variable=self.variable, value='C', text='Option C', command=self.showValue)

        # frame Widget(Frame)を親要素とした場合に、Cのradiobutton Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.cButton.pack()

        # frame Widget(Frame)を親要素として、dのradiobutton Widgetを作成する。
        # variable : 現在選択中のラジオボタンの値を格納する。文字列変数(self.variable)として値を持たせることで、可変として扱い、その他のラジオボタンへ値を共有して選択の状態を管理できる。
        # value : ラジオボタン自身が持つ値の設定。Cとする。
        # text : ラジオボタンを説明するテキスト。Option Dとする。
        # command : ラジオボタンが選択された場合に実行する関数を設定する。self.showValue関数を設定する。
        self.dButton = tk.Radiobutton(frame, variable=self.variable, value='C', text='Option D', command=self.showValue)

        # frame Widget(Frame)を親要素とした場合に、Dのradiobutton Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.dButton.pack()

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
