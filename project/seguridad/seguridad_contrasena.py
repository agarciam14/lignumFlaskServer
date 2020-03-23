# La validacion de una contrasena segura se esta haciendo
# basados en la normatividad NIST 800-63 en la que se valida
# longitud mayor a 8
# tener letras mayusculas y minusculas
# tener numeros
# tener caracteres especiales
# el usuario no este en la contrasena

import re


def validacion_contrasena_segura(usuario, contrasena):
    if validar_longitud(contrasena) and validar_mayusculas(contrasena) and validar_minusculas(contrasena) and validar_numeros(contrasena) and validar_caracter_especial(contrasena) and validar_usuario_en_contrasena(usuario, contrasena):
        return True
    return False


def validar_longitud(contrasena):
    if len(contrasena) < 8:
        return False
    return True


def validar_mayusculas(contrasena):
    for char in contrasena:
        if char.isupper():
            return True
    return False


def validar_minusculas(contrasena):
    for char in contrasena:
        if char.islower():
            return True
    return False


def validar_numeros(contrasena):
    for char in contrasena:
        if char.isdigit():
            return True
    return False


def validar_caracter_especial(contrasena):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if(regex.search(contrasena) == None):
        return False    
    return True


def validar_usuario_en_contrasena(usuario, contrasena):
    if usuario in contrasena:
        return False
    return True
