import pytest #motor / engine
import requests #biblioteca para comunicar com apis
from requests import Response

base_url = 'https://petstore.swagger.io/v2' #endereço da api
headers = {'Content-Type': 'application/json'} #os dados serão no formato json #headers, significa cabeçalho

def testar_incluir_pet():
# Configura
 # Dados de entrada: virão do pet1.json
 # Resultado Esperado
    status_code_esperado = 200 #status code 200 quer dizer comunicação concluída/que aceitou
    nome_pet_esperado = 'Bolinha'
    tag_esperada = 'Vacinado'

# Executa
    resultado_obtido: Response = requests.post(url=base_url + '/pet',
                  data=open('C:\\Users\\kbjantsch\\PycharmProjects\\133pets\\vendors\\json\\pet1.json', 'rb'),
                  headers=headers
                  )
# Valida
    print(resultado_obtido)
        assert resultado_obtido.status_code == status_code_esperado


def testar_excluir_pet()
    pet_id = 'XXXXX'
    status_code_espetado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    message_esperada = str(pet_id)

    resultado_esperado = requests.delete(
        url=base_url + '/pet/' + pet_id,
        headers=headers
    )

    assert resultado_obtido.status_code == status_code_esperado
    corpo_da_resposta = resultado_obtido.json()
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == pet_id
