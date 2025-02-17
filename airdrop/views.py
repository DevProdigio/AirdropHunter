from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Airdrop
from .forms import IndiqueAirdropForm


def airdrop_list(request):
    plataforma = request.GET.get('plataforma')
    data_publicacao = request.GET.get('data_publicacao')
    status = request.GET.get('status')
    investimento = request.GET.get('investimento')

    airdrops = Airdrop.objects.all()

    if plataforma:
        airdrops = airdrops.filter(plataforma=plataforma)
    if data_publicacao:
        airdrops = airdrops.filter(data_publicacao=data_publicacao)
    if status:
        airdrops = airdrops.filter(status=status)
    if investimento:
        airdrops = airdrops.filter(investimento=investimento)

    return render(request, 'airdrop/index.html', {'airdrops': airdrops})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('airdrop_list') # retorna a página principal apos login
        else:
            messages.error(request, 'Usuario ou senha inválidos.')
    else:
        form = AuthenticationForm()
    return render(request, 'airdrop/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) #login auto após registro
            return redirect('airdrop_list') 
        else:
            messages.error(request, 'Erro ao cadastrar usuario. Tente novamente mais tarde!')
    else:
        form = UserCreationForm()
    return render (request, 'airdrop/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('airdrop_list')

def indique_airdrop(request):
    if request.method == 'POST':
        
        form = IndiqueAirdropForm(request.POST)
        if form.is_valid():
            
            print("Dados do formulário:", form.cleaned_data)
            return redirect('indique_airdrop_sucesso')  
    else:
        
        form = IndiqueAirdropForm()

    return render(request, 'airdrop/indique_airdrop.html', {'form': form})

def indique_airdrop_sucesso(request):
    return render(request, 'airdrop/indique_airdrop_sucesso.html')

def detalhes_airdrop(request, airdrop_id):
    # isso irá buscar o airdrop pelo id, se não existir vai retornar um erro 404
    airdrop = get_object_or_404(Airdrop, id=airdrop_id)
    return render(request, 'airdrop/detalhes_airdrop.html', {'airdrop' : airdrop})

def quem_somos(request):
    return render(request, 'airdrop/quem_somos.html')