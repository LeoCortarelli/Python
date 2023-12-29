from django.urls import path
from app_cadastro_usuarios import views # VOCÊ PRECISA IMPORTAR A VIEWS QUE ESTÁ NO SEU APP

urlpatterns = [
    # rota, view responsavel, nome referencia 
    # ex: usuarios.com (Não vai ser isso)
    path('',views.home,name='home'),  # ASSIM VOCÊ IMPORTA UMA FUNÇÃO CHAMADA (HOME) QUE ESTÁ EM VIEWS
    # Se quiser que fosse outra url deve colocar 
    # path('leocortarelli/')
    
    # parou no min 6:58
]
