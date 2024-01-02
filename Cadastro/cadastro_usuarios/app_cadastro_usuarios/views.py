from django.shortcuts import render
from .models import Usuario

def home(request):  # (request) ele te permite acessar os dados dentro da pagina
    return render(request,'usuarios/home.html')  # (render) ele vai renderizar a pagina
                # Coloca o request e depois coloca a pagina html
                # Você precisa criar a pasta templates e precisa ter esse nome porque e a pasta que o django vai procurar

def usuarios(request):
    # Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    # Exibir todos os usuarios ja cadastrados em uma nova página
    # Preimeiro colocar dentro de um dicionario
    usuarios = {
        'usuarios': Usuario.objects.all() # Retornando todas as informações de todos os usuarios cadastrados no banco
    }
    
    # Retornar os dados para a pagina de listagem de usuarios
    return render(request,'usuarios/usuarios.html',usuarios) # passando o dicionario