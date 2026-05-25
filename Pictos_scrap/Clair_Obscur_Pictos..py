import requests
from bs4 import BeautifulSoup
import tkinter as tk
import json
import os
import webbrowser

ARQUIVO_SAVE = "meus_pictos.json"



def extrair_pictos():
    url = "https://expedition33-wiki-fextralife-com.translate.goog/Pictos?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc"
    print("Conectando ao site...")
    try:
        resposta = requests.get(url)
    except Exception:
        print("Erro de conexão. Verifique sua internet ou o link.")
        return []

    sopa = BeautifulSoup(resposta.text, 'html.parser')
    tabela_pictos = sopa.find('table', class_='wiki_table')
    lista_temporaria = []

    if tabela_pictos is not None:
        linhas = tabela_pictos.find_all('tr')
        for linha in linhas[1:]:
            colunas = linha.find_all('td')
            if len(colunas) > 0:
                primeira_coluna = colunas[0]
                links_da_coluna = primeira_coluna.find_all('a')
                for link in links_da_coluna:
                    nome_do_picto = link.text.strip()
                    if nome_do_picto != "" and "DLC" not in nome_do_picto:

                        link_parcial = link.get('href')
                        if link_parcial.startswith("http"):
                            link_completo = link_parcial
                        else:
                            link_completo = "https://expedition33.wiki.fextralife.com" + link_parcial

                        ja_existe = False
                        for item in lista_temporaria:
                            if item["nome"] == nome_do_picto:
                                ja_existe = True

                        if not ja_existe:
                            lista_temporaria.append({"nome": nome_do_picto, "link": link_completo})
    return lista_temporaria


def carregar_save():
    if os.path.exists(ARQUIVO_SAVE):
        try:
            with open(ARQUIVO_SAVE, "r") as arquivo:
                dados = json.load(arquivo)
                if type(dados) == dict:
                    return dados
        except Exception:
            pass
    return {}


def salvar_progresso():
    progresso_completo = {}
    for item in lista_botoes_criados:
        nome_picto = item["nome"]
        status_obtido = item["var_obtido"].get()
        status_build = item["var_build"].get()

        progresso_completo[nome_picto] = {
            "obtido": status_obtido,
            "build": status_build
        }

    with open(ARQUIVO_SAVE, "w") as arquivo:
        json.dump(progresso_completo, arquivo)

    print("Progresso salvo com sucesso!")

janela = tk.Tk()
janela.title("Marcador de Pictos")
janela.geometry("450x600")
janela.configure(bg="black")

titulo = tk.Label(janela, text="Meus Pictos", font=("Arial", 16, "bold"), bg="black", fg="white")
titulo.pack(pady=10)

area_principal = tk.Frame(janela, bg="black")
area_principal.pack(fill="both", expand=True)

canvas = tk.Canvas(area_principal, bg="black", highlightthickness=0)
scrollbar = tk.Scrollbar(area_principal, orient="vertical", command=canvas.yview)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

frame_botoes = tk.Frame(canvas, bg="black")
canvas.create_window((0, 0), window=frame_botoes, anchor="nw")


def configurar_scroll(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


frame_botoes.bind("<Configure>", configurar_scroll)

def acao_clique():
    salvar_progresso()
    for item in lista_botoes_criados:
        botao = item["botao_ajuda"]
        if item["var_obtido"].get() == 1:
            botao.pack_forget()
        else:
            botao.pack(side="left", padx=10)

print("Iniciando extração dos dados...")
lista_oficial = extrair_pictos()
print("Extração concluída! Abrindo janela...")

lista_botoes_criados = []
pictos_ja_salvos = carregar_save()

if len(lista_oficial) == 0:
    erro = tk.Label(frame_botoes, text="Erro ao carregar dados.", bg="black", fg="red")
    erro.pack(pady=20)
else:
    for picto in lista_oficial:
        nome = picto["nome"]
        link = picto["link"]

        var_obtido = tk.IntVar(janela)
        var_build = tk.IntVar(janela)

        if nome in pictos_ja_salvos:
            dado_salvo = pictos_ja_salvos[nome]


            if type(dado_salvo) == dict:
                var_obtido.set(dado_salvo.get("obtido", 0))
                var_build.set(dado_salvo.get("build", 0))
            else:
                var_obtido.set(1 if dado_salvo == 1 else 0)
                var_build.set(0)

        linha_frame = tk.Frame(frame_botoes, bg="black")
        linha_frame.pack(fill="x", pady=2)

        caixa_obtido = tk.Checkbutton(
            linha_frame,
            text=nome,
            variable=var_obtido,
            font=("Arial", 11),
            bg="black", fg="white", selectcolor="black",
            command=acao_clique
        )
        caixa_obtido.pack(side="left", padx=10)

        caixa_build = tk.Checkbutton(
            linha_frame,
            text=" Build",
            variable=var_build,
            font=("Arial", 9),
            bg="black", fg="#ffaa00", selectcolor="#1e1e1e",
            command=salvar_progresso
        )
        caixa_build.pack(side="left", padx=5)

        botao_ajuda = tk.Button(
            linha_frame,
            text="Onde achar?",
            bg="#1e1e1e", fg="#00a2ff",
            font=("Arial", 9, "bold"),
            borderwidth=0, cursor="hand2",
            command=lambda url=link: webbrowser.open(url)
        )

        if var_obtido.get() == 0:
            botao_ajuda.pack(side="left", padx=10)

        lista_botoes_criados.append({
            "nome": nome,
            "var_obtido": var_obtido,
            "var_build": var_build,
            "botao_ajuda": botao_ajuda
        })

janela.mainloop()