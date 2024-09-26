# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 18:22:16 2024

@author: Nevermore
"""

import random as rd
import pandas as pd
import time as t

tabela = pd.read_excel("tabela dos bichos.ods")
fem_nouns = ["Águia","Borboleta","Cabra","Cobra","Vaca"]

def sorteio():
    resultados = []
    for i in range(1,6):
        number = rd.randint(1000,9999)
        resultados.append(number)
    print(f"Resultados: {resultados}")
    return resultados

def apostar():
    
    print("Selecione um tipo de aposta entre as opções abaixo:\n"+
          "Grupo\nDezena\nCentena\nMilhar")
    tipo = input("Tipo de aposta: ").lower().strip()
    
    if tipo == "grupo":
        print("Escolha o animal entre as opções abaixo:\n"+
              "Grupo 1 - Avestruz\nGrupo 2 - Águia\nGrupo 3 - Burro\n"+
              "Grupo 4 - Borboleta\nGrupo 5 - Cachorro\nGrupo 6 - Cabra\n"+
              "Grupo 7 - Carneiro\nGrupo 8 - Camelo\nGrupo 9 - Cobra\n"+
              "Grupo 10 - Coelho\nGrupo 11 - Cavalo\nGrupo 12 - Elefante\n"+
              "Grupo 13 - Galo\nGrupo 14 - Gato\nGrupo 15 - Jacaré\n"+
              "Grupo 16 - Leão\nGrupo 17 - Macaco\nGrupo 18 - Porco\n"+
              "Grupo 19 - Pavão\nGrupo 20 - Peru\nGrupo 21 - Touro\n"+
              "Grupo 22 - Tigre\nGrupo 23 - Urso\nGrupo 24 - Veado\n"+
              "Grupo 25 - Vaca")
        grupo = int(input("Digite o número correspondente ao grupo: "))
    
    if tipo == "dezena":
        two_digits = str(input("Escolha um par de algarismos: "))
        if two_digits == "00":
            two_digits = "100"
        int_two_digits = int(two_digits)
    
    elif tipo == "centena":
        three_digits = input("Escolha um trio de algarismos: ")
        
    elif tipo == "milhar":
        four_digits = input("Escolha um número de quatro algarismos: ")
    
    valor = int(input("Valor da aposta em R$: "))
    quais_premios = input("Escolha os números dos prêmios que você quer "+
                          "jogar (de 1 a 5): ")
    premios_list = list(quais_premios)
    premios_list = [x for x in premios_list if x != ',']
    premios_list = [int(i) for i in premios_list]
    qtd = len(premios_list)
    
    premios = sorteio()
    stringify = [str(i) for i in premios]
    
    digit_list = []
    for i in stringify:
        for digit in i:
            digit_list.append(digit)
    
    dezena_1 = digit_list[2] + digit_list[3]
    dezena_2 = digit_list[6] + digit_list[7]
    dezena_3 = digit_list[10] + digit_list[11]
    dezena_4 = digit_list[14] + digit_list[15]
    dezena_5 = digit_list[-2] + digit_list[-1]
    dezenas_final = [dezena_1,dezena_2,dezena_3,dezena_4,dezena_5]
    for i, n in enumerate(dezenas_final):
        if n == "00":
            dezenas_final[i] = "100"
    if tipo == "grupo" or tipo == "dezena":
        integerify = [int(i) for i in dezenas_final]
    
    centena_1 = digit_list[1] + digit_list[2] + digit_list[3]
    centena_2 = digit_list[5] + digit_list[6] + digit_list[7]
    centena_3 = digit_list[9] + digit_list[10] + digit_list[11]
    centena_4 = digit_list[-7] + digit_list[-6] + digit_list[-5]
    centena_5 = digit_list[-3] + digit_list[-2] + digit_list[-1]
    centenas_final = [centena_1,centena_2,centena_3,centena_4,centena_5]
    if tipo == "centena":
        integerify = centenas_final
        
    milhar_1 = digit_list[0] + digit_list[1] + digit_list[2] + digit_list[3]
    milhar_2 = digit_list[4] + digit_list[5] + digit_list[6] + digit_list[7]
    milhar_3 = digit_list[8] + digit_list[9] + digit_list[10] + digit_list[11]
    milhar_4 = digit_list[-8] + digit_list[-7] + digit_list[-6] + digit_list[-5]
    milhar_5 = digit_list[-4] + digit_list[-3] + digit_list[-2] + digit_list[-1]
    milhares_final = [milhar_1,milhar_2,milhar_3,milhar_4,milhar_5]
    if tipo == "milhar":
        integerify = [int(i) for i in milhares_final]
    
    considered = []
    if 1 in premios_list:
        considered.append(integerify[0])
    if 2 in premios_list:
        considered.append(integerify[1])
    if 3 in premios_list:
        considered.append(integerify[2])
    if 4 in premios_list:
        considered.append(integerify[3])
    if 5 in premios_list:
        considered.append(integerify[4])
    print("Prêmios considerados:",considered)
    
    if tipo == "grupo":
        resultados_grupo = tabela[tabela["grupo"] == grupo]
        resultados_grupo = resultados_grupo.reset_index()
        resultados_grupo = resultados_grupo.drop("index", axis=1)
        results = resultados_grupo.iloc[:,0]
        results_list = list(results.values)
        for i in considered:
            print(f"Conferindo resultado do prêmio {integerify.index(i)+1}"+
                  "...")
            t.sleep(1.5)
            if i in results_list:
                retorno = (40 * valor) / qtd
                if resultados_grupo.iloc[0,2] in fem_nouns:
                    print(f"Você jogou na {resultados_grupo.iloc[0,2]} e "+
                          f"ganhou! O seu retorno é de R$ {retorno}")
                else:
                    print(f"Você jogou no {resultados_grupo.iloc[0,2]} e "+
                          f"ganhou! O seu retorno é de R$ {retorno}")
            else:
                if resultados_grupo.iloc[0,2] in fem_nouns:
                    print(f"Você jogou na {resultados_grupo.iloc[0,2]} e "+
                          "perdeu! Mais sorte na próxima!")
                else:
                    print(f"Você jogou no {resultados_grupo.iloc[0,2]} e "+
                          "perdeu! Mais sorte na próxima!")
        return resultados_grupo
                    
    if tipo == "dezena":
        resultado_dezena = tabela[tabela["dezena"] == int_two_digits]
        resultado_dezena = resultado_dezena.reset_index()
        resultado_dezena = resultado_dezena.drop("index", axis=1)
        if resultado_dezena.iloc[0,0] in considered:
            retorno = (60 * valor) / qtd
            if resultado_dezena.iloc[0,2] in fem_nouns:
                print(f"Você jogou na {resultado_dezena.iloc[0,2]} e "+
                      f"ganhou! O seu retorno é de R$ {retorno}")
            else:
                print(f"Você jogou no {resultado_dezena.iloc[0,2]} e "+
                      f"ganhou! O seu retorno é de R$ {retorno}")
        else:
            if resultado_dezena.iloc[0,2] in fem_nouns:
                print(f"Você jogou na {resultado_dezena.iloc[0,2]} e "+
                      "perdeu! Mais sorte na próxima!")
            else:
                print(f"Você jogou no {resultado_dezena.iloc[0,2]} e "+
                      "perdeu! Mais sorte na próxima!")
        return resultado_dezena
    
    elif tipo == "centena":
        if three_digits in considered:
            retorno = (600 * valor) / qtd
            print(f"Você ganhou! O seu retorno é de R$ {retorno}")
        else:
            print("Você perdeu! Mais sorte na próxima!")
    
    elif tipo == "milhar":
        if four_digits in considered:
            retorno = (4000 * valor) / qtd
            print(f"Você ganhou! O seu retorno é de R$ {retorno}")
        else:
            print("Você perdeu! Mais sorte na próxima!")
    
    return