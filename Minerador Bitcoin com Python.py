from hashlib import sha256
import time

print(f'\033[32mcomeçando...\033[m\n \033[34m')


# função que vai tirar, é por as criptografias
def aplicar_sha256(texto):
    return sha256(texto.encode("ascii")).hexdigest()


# função que vai minerar as info passada
def minerar(num_bloco, transacoes, hash_anterior, qtde_zeros):
    nonce = 0
    while True:
        texto = str(num_bloco) + transacoes + hash_anterior + str(nonce)
        meu_hash = aplicar_sha256(texto)
        if meu_hash.startswith("0" * qtde_zeros):
            return nonce, meu_hash
        nonce += 1


# VOCÊ PODE PEGAR AS INFO: https://www.blockchain.com/pt/explorer
if __name__ == "__main__":
    # NUMERO DO BLOCO
    num_bloco = 15

    # NOME DAs TRANSAÇOES
    transacoes = """
    pereira->Reis->10
    joao->Joao->5
    Joao->Vitor->11"""

    # QUANTIDADE DE ZEROS... HOJE E DE 20 ZEROS
    qtde_zeros = 6  # 20

    # NOME DA HASH
    hash_anterior = "cc00cd144dbe625a7d46d7e705fcad43974b3af779d7b325b2d6505de99b7f4a"

    # VAIESCREVER N ATELA O RESULTADO!
    inicio = time.time()
    resultado = minerar(num_bloco, transacoes, hash_anterior, qtde_zeros)
    print(resultado, end='\n')
    print()
    tempo = f'{time.time() - inicio:.2f}'
    print(f'foram gasto {tempo}')
