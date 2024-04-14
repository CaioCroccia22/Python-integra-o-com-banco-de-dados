from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

user = 'postgres'
password = 'root'
host = 'localhost'
database = 'blog'

# Passa os dados para a URI que estabelece a conexao com o banco
DATABASE_URI = f'postgresql://{user}:{password}{host}/{database}'

# Cria uma engine baseada na URI
engine = create_engine(DATABASE_URI)

# Cria uma sessão
Session = sessionmaker(bind=engine)

# Inicia a sessão
session = Session()


# Estabelece a declaraçao básica para ter a config da conexão inicial
Base = declarative_base()