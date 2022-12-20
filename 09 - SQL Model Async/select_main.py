import asyncio

from typing import List

from sqlalchemy import func # Funções de agregação 

from sqlmodel import select
from sqlalchemy.future import select as _select


from conf.helpers import formata_data
from conf.db_session import create_session



# Select Simples
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.revendedor import Revendedor

# Select Compostos / Complexos
from models.picole import Picole

## Select simples -> SELECT * FROM aditivos_nutritivos;
async def select_todos_aditivos_nutritivos() -> None:
    async with create_session() as session:
        query = select(AditivoNutritivo)
        aditivos_nutritivos = await session.exec(query) # Objeto iterável
        aditivos_nutritivos = aditivos_nutritivos.all() # Lista

        for an in aditivos_nutritivos:
            print(f'ID: {an.id}')
            print(f'Data: {formata_data(an.data_criacao)}')
            print(f'Nome: {an.nome}')
            print(f'Fórmula Química: {an.formula_quimica}')


# SELECT * FROM sabores WHERE sabor.id == 21;
async def select_filtro_sabor(id_sabor: int) -> None:
    async with create_session() as session:
        # query = select(Sabor).filter(Sabor.id == id_sabor)
        # query = select(Sabor).where(Sabor.id == id_sabor)
        # resultado = await session.exec(query)
        
        # Pode ter vários, pega o primeiro resultado
        # sabor: Sabor = resultado.first() # None
       
        # Execção em não resultado ou mais de 1
        # sabor: Sabor = resultado.one() 
        
        # None se não encontrar
        sabor: Sabor = await session.get(Sabor, id_sabor)
       
        print(f'ID: {sabor.id}')
        print(f'Data: {formata_data(sabor.data_criacao)}')
        print(f'Nome: {sabor.nome}')


async def select_complexo_picole() -> None:
    async with create_session() as session:
        query = select(Picole)
        resultado = await session.exec(query)
        picoles: List[Picole] = resultado.unique().all()

        for picole in picoles:
            print(f'ID: {picole.id}')
            print(f'Data: {formata_data(picole.data_criacao)}')
            print(f'Preço: {picole.preco}')

            print(f'ID Sabor: {picole.id_sabor}')
            print(f'Sabor: {picole.sabor.nome}')

            print(f'ID Embalagem: {picole.id_tipo_embalagem}')
            print(f'Embalagem: {picole.tipo_embalagem.nome}')

            print(f'ID Tipo Picole: {picole.id_tipo_picole}')
            print(f'Tipo Picole: {picole.tipo_embalagem.nome}')

            print(f'Ingredientes: {picole.ingredientes}')
            print(f'Aditivos Nutritivos: {picole.aditivos_nutritivos}')
            print(f'Conservantes: {picole.conservantes}')


async def select_order_by_sabor() -> None:
    async with create_session() as session:
        query = select(Sabor).order_by(Sabor.data_criacao.desc())
        resultado = await session.exec(query)

        sabores: List[Sabor] = resultado.all()

        for sabor in sabores:
            print(f'ID: {sabor.id}')
            print(f'Nome: {sabor.nome}')


async def select_group_by_picole() -> None:
    async with create_session() as session:
        query = select(Picole).group_by(Picole.id, Picole.id_tipo_picole)
        resultado = await session.exec(query)
        picoles: List[Picole] = resultado.unique().all()

        for picole in picoles:
            print(f'ID: {picole.id}')
            print(f'Tipo Picole: {picole.tipo_picole.nome}')
            print(f'Sabor: {picole.sabor.nome}')
            print(f'Preço: {picole.preco}')


async def select_limit() -> None:
    async with create_session() as session:
        query = select(Sabor).limit(25)
        # query = select(Sabor).offset(25).limit(25)
        resultado = await session.exec(query)
        sabores: List[Sabor] = resultado.all()

        for sabor in sabores:
            print(f'ID: {sabor.id}')
            print(f'Sabor: {sabor.nome}')


async def select_count_revendedor() -> None:
    async with create_session() as session:
        query = select(func.count(Revendedor.id))
        resultado = await session.execute(query)
        qtd: int = resultado.scalar()

        print(f'Quantidade de revendedores: {qtd}')



async def select_agregacao() -> None:
    async with create_session() as session:
        query = select(
            func.sum(Picole.preco).label('soma'),
            func.avg(Picole.preco).label('media'),
            func.min(Picole.preco).label('mais_barato'),
            func.max(Picole.preco).label('mais_caro'),
        )
        resultado = await session.execute(query)
        resultado = resultado.all()

        print(f'Resultado: {resultado}')

        print(f'A soma de todos os picolés é: {resultado[0][0]}')
        print(f'A média de todos os picolés é: {resultado[0][1]}')
        print(f'O picolé mais barato é: {resultado[0][2]}')
        print(f'O picolé mais caro é: {resultado[0][3]}')



if __name__ == '__main__':
    # asyncio.run(select_todos_aditivos_nutritivos())
    
    # asyncio.run(select_filtro_sabor(21))

    # asyncio.run(select_complexo_picole())

    # asyncio.run(select_order_by_sabor())

    # asyncio.run(select_group_by_picole())

    # asyncio.run(select_limit())

    # asyncio.run(select_count_revendedor())

    asyncio.run(select_agregacao())
