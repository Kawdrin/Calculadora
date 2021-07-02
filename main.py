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

    def verifica_operador(self, operador):
        if self.ids.valor_operado.text=="":
            return self.ids.numeros.text+ F" {operador}"
        return self.calcular(operador)

    def calcular(self, operador=""):
        valor_total = 0
        valor_operado = self.ids.valor_operado.text
        valor_atual = self.ids.numeros.text

        if self.ids.valor_operado.text == "":
            self.ids.valor_operado.text = "0"
        if self.ids.numeros.text == "":
            self.ids.numeros.text = "0"

        if self.ids.valor_operado.text[-1] == "/":
            valor_operado = self.ids.valor_operado.text.replace(" /", "")
            valor_total = float(valor_operado) / float(valor_atual)

        if self.ids.valor_operado.text[-1] == "*":
            valor_operado = self.ids.valor_operado.text.replace(" *", "")
            valor_total = float(valor_operado) * float(valor_atual)

        if self.ids.valor_operado.text[-1] == "+":
            valor_operado = self.ids.valor_operado.text.replace(" +", "")
            valor_total = float(valor_operado) + float(valor_atual)

        if self.ids.valor_operado.text[-1] == "-":
            valor_operado = self.ids.valor_operado.text.replace(" -", "")
            valor_total = float(valor_operado) - float(valor_atual)
        return F"{valor_total} {operador}"





class Calculadora(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "500"
        print(self.theme_cls.primary_color)
        return Tela()

Calculadora().run()
