from conexao_ORM import Base, engine, session
from User import User
from Post import Post

# Criando tabelas
Base.metadata.create_all(engine)


# Função para exibir o menu de opções 
def show_menu():
    print("Menu de opções:")
    print("1. Adicionar Usuário")
    print("2. Adicionar Post")
    print("3. Consultar usuários")
    print("4. Sair")

def add_user():
    print("Adicionar novo usuário:\n")
    name = input("Digite o nome de usuário: \n")
    email = input("Digite o email:\n")
    user = User(name, email)
    session.add(user)
    session.commit()
    print("Usuário adicionado com sucesso!!")

# Função para adicionar novo Post
def add_post():
    print("Adicionar novo post:\n")
    title = input("Digite o titulo do post: \n")
    content = input("Digite o conteúdo do post: \n")
    author_id = input("Digite o ID do autor: \n")
        # Para adicionar o post tem que ver se o id do autor(chave estrageira) existe
        # Para isso a variavel user
    user = session.query(User).filter_by(id=author_id).first()
    if user:
        post = Post(title=title, content=content, author=user)
        session.add(post)
        session.commit()
        print("Post adicionado com sucesso!")
        

def query_user_post():
    users = session.query(User).join(User.posts).order_by(User.name).all()
    for user in users:
        print(f"User: {user.name}, email: {user.email}")
        for post in user.posts:
                print(f"Post: {post.title}, conteúdo: {post.content}")
