def test_sim():
    # A função test_sim é um teste unitário que verifica uma condição específica
    # Usa a função sum() para calcular a soma dos elementos da lista [1, 2, 3]
    resultado = sum([1, 2, 3])

    # A instrução assert verifica se o resultado da soma é igual a 6
    # Se a condição for verdadeira, o teste passa e a execução continua normalmente
    # Se a condição for falsa, um AssertionError será levantado, indicando a falha do teste
    assert resultado == 6

# Para rodar o teste usando pytest, você executaria no terminal:
# pytest nome_do_arquivo.py
