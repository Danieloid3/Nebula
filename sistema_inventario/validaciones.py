def validar_texto(texto):
    if texto.strip() == "":
        raise ValueError("Text cannot be empty")
    return texto


def validar_numero(numero):
    try:
        valor = float(numero)
        if valor < 0:
            raise ValueError
        return valor
    except:
        raise ValueError("Invalid number")
