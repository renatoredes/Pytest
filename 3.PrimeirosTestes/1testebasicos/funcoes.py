def email_valido(email):
    # Verifica se o email contém um "@" e um "."
    return "@" in email and "." in email


def dividir(a, b):
    # Verifica se o divisor é zero para evitar divisão por zero
    if b == 0:
        return None  # Retorna None se o divisor for zero
    return a / b  # Retorna o resultado da divisão se o divisor não for zero
