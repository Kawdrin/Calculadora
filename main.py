from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton

Window.size = (360, 540)

class Tela(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validando_operador(self, operador, conta):
        if len(conta) > 0 and conta[-1] in "+-/*" :
            return conta
        return conta+operador

    def somar_conta(self, conta):
        operadores = {"*":0, "/":0, "+":0, "-":0,}
        def separar_numeros(numero):
            ...



class Calculadora(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "500"
        print(self.theme_cls.primary_color)
        return Tela()

Calculadora().run()
