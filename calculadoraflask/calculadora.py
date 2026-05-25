import requests
from flask import Flask, render_template, request

def calcular():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operacao = request.form['operacao']


    if operacao == '+':
        resultado = num1 + num2
        etapas = f'{num1} + {num2} = {resultado}'

    elif operacao == '-':
        resultado = num1 - num2
        etapas = f'{num1} - {num2} = {resultado}'
    
    elif operacao == '*':
        resultado = num1 * num2
        etapas = f'{num1} * {num2} = {resultado}'
    
    elif operacao == '/':
        if num1 and num2 !=0:
            resultado = num1 / num2
            etapas = f'{num1} / {num2} = {resultado}'
        else:
            print("Números invalidos!")
    

    return render_template('calculadora.html', etapas=etapas, resultados=resultado)