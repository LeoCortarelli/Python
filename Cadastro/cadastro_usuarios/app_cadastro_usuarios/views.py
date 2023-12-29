from django.shortcuts import render

def home(request):  # (request) ele te permite acessar os dados dentro da pagina
    return render(request,'usuarios/home.html')  # (render) ele vai renderizar a pagina
                # Coloca o request e depois coloca a pagina html
                # Você precisa criar a pasta templates e precisa ter esse nome porque e a pasta que o django vai procurar