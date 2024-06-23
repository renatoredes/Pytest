import pytest

# Definição de uma fixture que prepara dados de teste


@pytest.fixture
def sample_data():
    # Código de configuração
    data = [1, 2, 3]
    return data

# Uso da fixture em um teste


def test_sum(sample_data):
    assert sum(sample_data) == 6
