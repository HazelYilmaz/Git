# coding: utf-8

os.system("del /q .\\obf\\__pycache__")

import easygui
import obf.Recipes
import obf.Meals
import os


def secimekrani():
    try:
        yemek = easygui.choicebox(msg="Seçim yapın.", title="Seçim Ekranı", choices=obf.Meals.meals)
    except:
        easygui.exceptionbox()

    try:
        easygui.codebox(msg="Tarife göz atın.", title="Tarif Ekranı", text=obf.Recipes.recipes[str(yemek[:4])])
    except:
        easygui.exceptionbox()

while True:
    secimekrani()
