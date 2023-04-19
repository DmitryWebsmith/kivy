from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        return Button(text='Hello world')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MyApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
