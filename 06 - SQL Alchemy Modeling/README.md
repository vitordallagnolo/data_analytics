
#  Crawlers AVITAseg

> Repositório para crawlers que rodam na AVITAseg.

![](https://cdn.hackersandslackers.com/2020/12/sqlalchemy_series_redo.png)

<!-- ##  Requirements (Pré requisitos) -->

<!-- Bibliotecas utilizadas para o projeto. -->

<!-- * Python 3.8+ [Install](https://www.python.org/downloads/) -->
<!-- * Pandas [Install](https://pandas.pydata.org/) -->
<!-- * NumPY [Install](https://numpy.org/) -->
<!-- * Tabula [Install](https://tabula-py.readthedocs.io/en/latest) -->
<!-- * AVITA [Install](https://gitlab.com/avitaseg/bibliotecas/avita-financeiro-utility-python-lib) -->
<!-- * PySpark [Install](https://spark.apache.org/docs/latest/api/python/) -->

##  Installation

```
$ pip install requirements.txt
```

<!-- ##  Screenshots -->

<!-- Screenshot de exemplo apenas para manter este README organizado. -->

<!-- ![Screenshots of projects](https://dradisframework.com/images/pro/screenshots/screenshot-62_small.png) -->
Screenshots do projeto

##  Features

Este projeto é uma modelagem de dados e possuí algumas features para auxiliar na estruturação do estudo:

* Criação das tabelas em banco de dados

* Geração de dados fictícios para manipulação das bases

##  Usage example

Exemplo das importações utilizadas para fazer a leitura e tratamento dos dados advindos das fontes citadas acima.

```python
from conf.db_session import create_session

# Insert de models sem relacionamento
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.revendedor import Revendedor

# Insert de models com relacionamento
from models.lote import Lote
from models.nota_fiscal import NotaFiscal
from models.picole import Picole

```