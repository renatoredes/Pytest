import pytest

# Definição de uma fixture com setup e teardown


@pytest.fixture
def resource():
    # Setup: Código para configurar o recurso
    res = setup_resource()

    yield res  # O valor retornado será passado para os testes que usam esta fixture

    # Teardown: Código para limpar o recurso
    teardown_resource(res)


def setup_resource():
    # Simulação de criação de recurso
    return "resource"


def teardown_resource(res):
    # Simulação de limpeza de recurso
    print(f"Cleaning up {res}")

# Uso da fixture em um teste


def test_resource_usage(resource):
    assert resource == "resource"
