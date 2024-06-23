from funcoes import *


def test_email_valido():
    # Testa se o email válido retorna True
    assert email_valido("exemplo@dominio.com") is True
    # Testa se um email inválido (sem "@") retorna False
    assert email_valido("exemplo.com") is False


def test_dividir():
    # Testa a divisão de 4 por 2, que deve retornar 2
    assert dividir(4, 2) == 2
    # Testa a divisão por zero, que deve retornar None
    assert dividir(4, 0) is None
