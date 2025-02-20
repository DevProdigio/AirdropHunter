from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.airdrop_list, name='airdrop_list'), #página principal
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('indique-airdrop/', views.indique_airdrop, name='indique_airdrop'),
    path('indique-airdrop/sucesso/', views.indique_airdrop_sucesso, name='indique_airdrop_sucesso'),
    path('airdrop/<int:airdrop_id>/', views.detalhes_airdrop, name='detalhes_airdrop'),
    path('quem-somos/', views.quem_somos, name='quem_somos'),
]