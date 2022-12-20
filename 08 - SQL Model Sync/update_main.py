"""
1 - Buscar o registro a ser atualizado;
2 - Faz as alterações no registro;
3 - Salva o registro no banco de dados;
"""
from conf.db_session import create_session

from sqlmodel import select

from models.sabor import Sabor
from models.picole import Picole


def select_filtro_picole(id_picole: int) -> None:
    with create_session() as session:
        picole: Picole = session.get(Picole, id_picole)

        if picole:
            print(f'ID: {picole.id}')
            print(f'Sabor: {picole.sabor.nome}')
            print(f'Preço: {picole.preco}')
        else:
            print('Não existe o picole com o id informado')



def atualizar_sabor(id_sabor: int, novo_nome: str) -> None:
    with create_session() as session:
        # Passo 1
        sabor: Sabor = session.get(Sabor, id_sabor)

        if sabor:
            # Passo 2
            sabor.nome = novo_nome
            # Passo 3
            session.commit()
        else:
            print(f'Não existe sabor com ID {id_sabor}')



def atualizar_picole(id_picole: int, novo_preco: float, novo_sabor: int = None):
    with create_session() as session:
        # Passo 1
        picole: Picole = session.get(Picole, id_picole)

        if picole:
            # Passo 2
            picole.preco = novo_preco
            # Se quisermos alterar o sabor também....
            if novo_sabor:
                picole.id_sabor = novo_sabor
            # Passo 3
            session.commit()
        else:
            print(f'Não existe picole com id {id_picole}')




if __name__ == '__main__':
    # from select_main import select_filtro_sabor

    # id_sabor = 42

    # # # Antes
    # select_filtro_sabor(id_sabor=id_sabor)

    # # # Atualizando
    # atualizar_sabor(id_sabor=id_sabor, novo_nome='Banana')

    # # # Depois
    # select_filtro_sabor(id_sabor=id_sabor)

    id_picole = 21
    novo_preco = 6.66
    id_novo_sabor = 42

    # Antes
    select_filtro_picole(id_picole=id_picole)

    # Atualizando
    atualizar_picole(id_picole=id_picole, novo_preco=novo_preco, novo_sabor=id_novo_sabor)

    # Depois
    select_filtro_picole(id_picole=id_picole)

