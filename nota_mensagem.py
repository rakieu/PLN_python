# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
usuario = str(input("Digite o usuário: "))
senha = str(input("Digite uma senha: "))
while usuario == senha:
    print ('Não pode, né!')
    usuario = str(input("Digite o usuário: "))
    senha = str(input("Digite uma senha: "))
else:
    print ("Correto!")
