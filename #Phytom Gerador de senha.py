#Phytom Gerador de senha

import random
import string

def gerar_senha(comprimento=12):
    caracteres = string.ascii_letters + string.digits + string
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

# Exemplo de uso
comprimento_desejado = 16  # Você pode ajustar o comprimento da senha conforme necessário
senha_gerada = gerar_senha(comprimento_desejado)
print(f'Senha gerada: {senha_gerada}')