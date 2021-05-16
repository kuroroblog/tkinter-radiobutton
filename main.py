import tkinter as tk


class Application(tk.Frame):
    # 現在選択されているボタンの値を格納する変数
    variable = None
    # Aラジオボタンを格納する変数
    aButton = None
    # Bラジオボタンを格納する変数
    bButton = None
    # Cラジオボタンを格納する変数
    cButton = None

    # 現在選択されているラジオボタンの値を確認する関数
    def showValue(self):
        # get() : 現在選択されているラジオボタンの値を取得する関数
        print("You selected the option " + self.variable.get())

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        self.master.geometry("300x200")

        # Windowを親要素として、frame Widget(Frame)を作成する。
        # frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)

        # Windowを親要素とした場合に、frame Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # stringを格納するように初期化。
        self.variable = tk.StringVar()
        # set() : 引数に該当するラジオボタンを選択する。初期値としてBの値を持つラジオボタンを選択。
        self.variable.set('B')

        # frame Widget(Frame)を親要素として、Aのradiobutton Widgetを作成する。
        # variable : 現在利用中のラジオボタンの値を格納する。その他のラジオボタンへ値を共有するために利用する。
        # value : ラジオボタン自身が持つ値。Aとする。
        # text : ラジオボタンを説明するテキスト。Option Aとする。
        # command : ラジオボタンが選択された場合に実行する関数を設定する。showValue関数を設定する。
        self.aButton = tk.Radiobutton(frame, variable=self.variable, value='A', text='Option A', command=self.showValue)

        # frame Widget(Frame)を親要素とした場合に、Aのradiobutton Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.aButton.pack()

        # frame Widget(Frame)を親要素として、Bのradiobutton Widgetを作成する。
        # variable : 現在利用中のラジオボタンの値を格納する。その他のラジオボタンへ値を共有するために利用する。
        # value : ラジオボタン自身が持つ値。Bとする。
        # text : ラジオボタンを説明するテキスト。Option Bとする。
        # command : ラジオボタンが選択された場合に実行する関数を設定する。showValue関数を設定する。
        self.bButton = tk.Radiobutton(frame, variable=self.variable, value='B', text='Option B', command=self.showValue)

        # frame Widget(Frame)を親要素とした場合に、Bのradiobutton Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.bButton.pack()

        # frame Widget(Frame)を親要素として、Cのradiobutton Widgetを作成する。
        # variable : 現在利用中のラジオボタンの値を格納する。その他のラジオボタンへ値を共有するために利用する。
        # value : ラジオボタン自身が持つ値。Cとする。
        # text : ラジオボタンを説明するテキスト。Option Cとする。
        # command : ラジオボタンが選択された場合に実行する関数を設定する。showValue関数を設定する。
        self.cButton = tk.Radiobutton(frame, variable=self.variable, value='C', text='Option C', command=self.showValue)

        # frame Widget(Frame)を親要素とした場合に、Cのradiobutton Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.cButton.pack()

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    app.mainloop()
