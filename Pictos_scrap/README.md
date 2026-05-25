# Marcador de Pictos - Clair Obscur Expedition 33

Um aplicativo desktop desenvolvido em Python para rastrear e gerenciar Fortalecimentos (Pictos) do jogo Clair Obscur: Expedition 33*. 
O programa extrai dados em tempo real da wiki oficial e salva o progresso do usuário localmente, permitindo por meio de check-list o rastreio dos pictos ja coletados

# Funcionalidades
Web Scraping Automático: Extrai a lista atualizada de Pictos diretamente da Wiki Fextralife usando.
Interface Gráfica: Interface intuitiva em Dark Mode construída para melhor visualização e conforto.
Banco de Dados Local: Sistema de salvamento automático em json com estrutura de dicionário para gerenciar múltiplos status (Obtido / Necessário).
Live Update & Integração Web: Ações na interface atualizam a tela em tempo real, com botões dinâmicos que redirecionam para a localização exata do item no navegador.
Standalone: tudo Compilado como  executável .exe independente.

# Tecnologias Utilizadas 
Código em Python 
Tkinter para a Interface Gráfica
BeautifulSoup4 e Requests** para o Web Scraping
JSON e OS para o Gerenciamento de Dados e Persistência

## Como executar o projeto
1. Clone este repositório: `git clone https://github.com/Matheus-Luongo/Checklist_Clair_Obscur.git`
2. Instale as dependências: `pip install requests beautifulsoup4`
3. Execute o arquivo principal: `python Interface.py`
*(Ou simplesmente baixe o arquivo `.exe` na aba "Releases" para testar diretamente no Windows).*

<img width="1340" height="967" alt="image" src="https://github.com/user-attachments/assets/b0666829-43f8-464e-9b5f-b83e3ad0aa66" />


