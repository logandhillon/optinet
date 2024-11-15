import tkinter as tk


class VirtualMedium:
    def __init__(self):
        self.__root = tk.Tk()
        self.__root.title("Optinet Virtual Medium")
        self.show_hex("000000")

    def start(self):
        try:
            self.__root.mainloop()
        except RuntimeError:
            pass

    def show_hex(self, hex_code):
        try:
            self.__root.config(bg='#'+hex_code)
        except:
            raise ValueError("invalid hex code")


if __name__ == "__main__":
    from threading import Thread
    tx = VirtualMedium()

    Thread(target=tx.start).start()

    while True:
        try:
            tx.show_hex(input("> "))
        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            exit()
