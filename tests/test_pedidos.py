import pytest
import pedidos
import manipulacaoArquivos
import interface
from unittest.mock import ANY


@pytest.mark.unitario_pedidos_adicionar
def test_adicionar_pedido(mocker):
    """

    Testa o cenário de adicionar um pedido.

    """

    mocker.patch('pedidos.listaPedido', [])

    # 2. Simulamos a resposta da API e dos ficheiros locais
    produtos_api_falsos = [
        {"id": 1, "title": "Produto API A", "price": 10.0},
        {"id": 2, "title": "Produto API B", "price": 20.0} # Vamos escolher este
    ]
    produtos_locais_falsos = [{"id": 101, "title": "Produto Local", "price": 15.0}]
    
    # Mock para a chamada de rede
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = produtos_api_falsos
    mocker.patch('pedidos.requests.get', return_value=mock_response)
    
    # Mock para a leitura de ficheiro local
    mocker.patch('manipulacaoArquivos.lerProdutosLocais', return_value=produtos_locais_falsos)

    # 3. Simulamos o input do utilizador a escolher o produto com ID 2
    mocker.patch('builtins.input', side_effect=['2'])

    # 4. Mocks para as funções de interface
    mocker.patch('interface.limpar_tela')
    mocker.patch('interface.mostrar_tabela_produtos')
    mock_mensagem_sucesso = mocker.patch('interface.mensagem_sucesso')
    mocker.patch('interface.pausar')

    # --- ACT ---
    pedidos.adicionar_pedido()

    # --- ASSERT ---
    # Verifica se a lista tem o produto escolhido
    assert len(pedidos.listaPedido) == 1
    assert pedidos.listaPedido[0] == (2, "Produto API B", 20.0)
    mock_mensagem_sucesso.assert_called_once_with("✅ Produto adicionado ao pedido.")

@pytest.mark.unitario_pedidos_fechar
def test_fechar_pedido(mocker):
    """

    Testa o cenário de fechar um pedido.

    """

    

@pytest.mark.unitario_pedidos_remover_item
def test_remover_item_pedido(mocker):
    """

    Testa o cenário de remover um item do pedido.

    """

@pytest.mark.unitario_pedidos_listar
def test_listar_pedido(mocker):
    """
    Testa o cenário de listar o pedido.

    """