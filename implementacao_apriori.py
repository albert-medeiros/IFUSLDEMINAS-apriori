# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 17:58:00 2020

@author: Albert
"""

import pandas as pd

dados = pd.read_csv(r'C:\Users\Albert\Downloads\apriori\pizzaria.csv', header = None)
transacoes = []
for i in range(0,2244):
    transacoes.append([str(dados.values[i,j]) for j in range (0, 7)])

from apyori import apriori
regras = apriori(transacoes, min_support = 0.3, min_confidence = 0.8, min_lift = 1)

resultados = list(regras)
resultados

resultados2 = [list(x) for x in resultados]
resultados2

resultadoFormatado = []
for j in range(0, 7):
    resultadoFormatado.append([list(x) for x in resultados2[j][2]])

resultadoFormatado