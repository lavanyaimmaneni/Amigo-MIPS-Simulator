from GUI import GUI
from main import Main


class App:
    def __init__(self):
        self.gui = GUI()
        self.main = Main()
        self.link_parts()

    def link_parts(self):
        self.main.link_with_gui(self.gui)
        self.gui.link_with_main(self.main)


def main():
    app = App()
    app.gui.mainloop()


if __name__ == '__main__':
    main()
