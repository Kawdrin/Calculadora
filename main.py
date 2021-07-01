from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton

Window.size = (360, 540)

class Tela(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Calculadora(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "A400"
        print(self.theme_cls.primary_color)
        return Tela()

Calculadora().run()
