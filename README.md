### venv
-  Configurar ambiente virtual
*  python -m venv venv
* .\venv\Script\activate
*  desactivate
*  source venv/Script/activate

# pytest
* pip install pytest

### Para executar o teste, basta digitar:
 * pytest
 ou
 * python -m pytest
 *  definir o arquivo de escolha de teste exemplo:
 python -m pytest test_basico_1.py 
 python -m pytest test_basico_2.py 

O que é o Pytest?
- UM Framework para testes em python

O que são fixtures no contexto do Pytest?
- Funções executadas antes e depois dos testes

Como o Pytest descobre os testes para executar?
- Procurando por funções que iniciam com test_ ou arquivos com o sufixo _test.py

Qual das seguintes frameworks de teste é conhecida por ser mais formal e orientada a objetos?
- unittest.

Qual é a estrutura de diretórios recomendada para organizar os testes no Pytest?
- Um diretório tests com subdiretorios de acordo cmo o projeto.

### Objetivo do assert
``
O assert é uma instrução utilizada em Python (e em muitos outros idiomas de programação) para realizar verificações simples durante a execução do código. No contexto de testes, como com pytest, o objetivo do assert é verificar se uma condição específica é verdadeira. Se a condição não for verdadeira, o assert levantará uma exceção AssertionError, indicando que o teste falhou.
``









