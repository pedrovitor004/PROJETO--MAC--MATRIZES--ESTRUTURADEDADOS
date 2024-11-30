import tkinter as tk
from tkinter import messagebox, Label
from datetime import datetime
import pygame

# Inicializando o mixer do Pygame para o som
#pygame.mixer.init()

# Carregar o som do clique
#som_clique = pygame.mixer.Sound("C:\\Users\\pedro\\Downloads\\projetodemac_matrizes\\SOM\\710039__inkedflorist__mouse-click-sound-for-vlogs-tutorial-videos-and-more.mp3")  # Substitua pelo caminho correto do arquivo de som

# USE O PADRÃO: ACESSE A PASTA PROJETOMAC_MATRIZES ENTRE NA PASTA SOM E SELECIONE O SOM DE CLIQUE. APÓS ISSO BUSQUE POR PROPIEDADES E COPIE O CAMINHO DE \\PROJETOMAC_MATRIZES ANTES 

# Dicionário com os livros e suas respectivas prateleiras
biblioteca = {
    # 1 -> SEM NENHUM LIVRO
    # 2
    "2A": [
        {"titulo": "Introdução à Ergonomia: Da prática à teoria", "autor": "Laerte Sznelwar"},
        {"titulo": "Outro Livro Exemplo", "autor": "Outro Autor"}
    ],
    "2B": [
        {"titulo": "Ergonomia: Projeto e Produção", "autor": "Itiro Lida"}
    ],
    "2C": [
        {"titulo": "Ergonomia Prática", "autor": "Jan Dull, Bernard Weerdmeester"}
    ],
    "2D": [
        {"titulo": "Segurança do Trabalho: Gerenciamento de riscos ocupacionais - GRO/PGR", "autor": "José Augusto da Silva Filho"}
    ],
    "2E": [
        {"titulo": "Legislação de Segurança, Acidente do Trabalho e Saúde do Trabalhador", "autor": "Tufi Messias Saliba"}
    ],
    "2F": [
        {"titulo": "Manual de Segurança e Saúde no Trabalho", "autor": "Danielle Carvalho Gonçalves, Isabelle Carvalho Gonçalves, Edwar Abreu Golçalves"}
    ],
    "2G": [
        {"titulo": "O Mal-estar na Civilização", "autor": "Sigmund Freud"}
    ],
    "2H": [
        {"titulo": "Sobre o Behaviorismo", "autor": "B.F. Skinner"}
    ],

    # 3
    "3A": [
        {"titulo": "Código de Defesa do Consumidor 2024 - 39 edição", "autor": "Inácio Conceição Vieira"}
    ],
    "3B": [
        {"titulo": "Manual do Direito Civil - Vol. Único (2024)", "autor": "Flávio Tartuce"}
    ],
    "3C": [
        {"titulo": "Constituição da República Federativa do Brasil", "autor": "Congresso Nacional"}
    ],
    "3D": [
        {"titulo": "Epistemologia Ambiental", "autor": "Enrique Leff"}
    ],
    "3E": [
        {"titulo": "A Complexidade Ambiental", "autor": "Enrique Leff"}
    ],
    "3F": [
        {"titulo": "Meio Ambiente e Sustentabilidade", "autor": "Viviane Moschini-Carlos"}
    ],
    "3G": [
        {"titulo": "Probabilidade", "autor": "Paul L. Meyer"}
    ],
    "3H": [
        {"titulo": "Estatística", "autor": "Antônio Arnot Crespo"}
    ],

    # 4
    "4A": [
        {"titulo": "Botânica Sistemática", "autor": "Vinícius C. Souza e Harri Lorenzi"}
    ],
    "4B": [
        {"titulo": "Biologia Vegetal", "autor": "Raven Evert Eichhorn"}
    ],
    "4C": [
        {"titulo": "Introdução a Sistemas Elétricos de Potência: Componentes simétricos", "autor": "Nelson Kagan"}
    ],
    "4D": [
        {"titulo": "Fundamentos de Circuitos Elétricos", "autor": "Matthew N. O. Sadiku & Charles Alexander"}
    ],
    "4E": [
        {"titulo": "A Arte da Eletrônica: Circuitos Eletrônicos e Microeletrônica", "autor": "Paul Horowitz"}
    ],
    "4F": [
        {"titulo": "Dispositivos Eletrônicos e Teoria dos Circuitos", "autor": "Louis Nashelsky & Robert L. Boylestad"}
    ],
    "4G": [
        {"titulo": "Eletrônica Industrial: Circuitos e Aplicações", "autor": "José Luíz Antunes de Almeida"}
    ],
    "4H": [
        {"titulo": "Eletroeletrônica Automotiva: Injeção Eletrônica, Arquitetura do Motor e Sistemas Embarcados", "autor": "Alexandre Capelli"}
    ],

    # 5
    "5A": [
        {"titulo": "Planejamento e Controle de Obras", "autor": "Aldo Dórea Mattos"}
    ],
    "5B": [
        {"titulo": "Introdução à Engenharia Civil", "autor": "Rudney C. Queiroz"}
    ],
    "5C": [
        {"titulo": "Como Preparar Orçamentos de Obras", "autor": "Aldo Dórea Mattos"}
    ],
    "5D": [
        {"titulo": "Trincas em Edifícios: Causas, Prevenção e Recuperação", "autor": "Ercio Thomaz"}
    ],
    "5E": [
        {"titulo": "Concreto Armado - Eu Te Amo", "autor": "Rômulo Castello Henriques Ribeiro"}
    ],
    "5F": [
        {"titulo": "Cálculo e Detalhamento de Estruturas Usuais de Concreto Armado", "autor": "Jasson Rodrigues de Figueiredo Filho e Roberto Chust Carvalho"}
    ],
    "5G": [
        {"titulo": "Desconstruindo o Projeto de Edifícios: Concreto Armado e Protegido", "autor": "José Sérgio dos Santos"}
    ],
    "5H": [
        {"titulo": "Dimensionamento de Elementos e Ligações em Estruturas de Aço", "autor": "Alex Sander Clemente de Souza"}
    ],

    # 6
    "6A": [
        {"titulo": "O Conto da Aia", "autor": "Margaret Atwood"}
    ],
    "6B": [
        {"titulo": "A Fundação", "autor": "Isaac Asimov"}
    ],
    "6C": [
        {"titulo": "Eu e Outras Poesias", "autor": "Augusto dos Anjos"}
    ],
    "6D": [
        {"titulo": "Alguma Poesia", "autor": "Carlos Drummond de Andrade"}
    ],
    "6E": [
        {"titulo": "A Preparação do Ator", "autor": "Konstantin Stanislavski"}
    ],
    "6F": [
        {"titulo": "Sobre o Teatro", "autor": "Bertolt Brecht"}
    ],
    "6G": [
        {"titulo": "1984", "autor": "George Orwell"}
    ],
    "6H": [
        {"titulo": "Frankenstein", "autor": "Mary Shelley"}
    ],

    # 7
    "7A": [
        {"titulo": "Todos os Contos", "autor": "Clarice Lispector"}
    ],
    "7B": [
        {"titulo": "Contos de Amor, de Loucura e de Morte", "autor": "Machado de Assis"}
    ],
    "7C": [
        {"titulo": "A Montanha Mágica", "autor": "Thomas Mann"}
    ],
    "7D": [
        {"titulo": "Dom Quixote", "autor": "Miguel de Cervantes"}
    ],
    "7E": [
        {"titulo": "A Culpa é das Estrelas", "autor": "John Green"}
    ],
    "7F": [
        {"titulo": "Orgulho e Preconceito", "autor": "Jane Austen"}
    ],
    "7G": [
        {"titulo": "O Diário de Bridget Jones", "autor": "Helen Fielding"}
    ],
    "7H": [
        {"titulo": "Um Amor Para Recordar", "autor": "Nicholas Sparks"}
    ],

    # 8
    "8A": [
        {"titulo": "A História de Lampião e Maria Bonita", "autor": "Leandro Gomes de Barros"}
    ],
    "8B": [
        {"titulo": "O Menino que Aprendeu a Ver", "autor": "José Pacheco"}
    ],
    "8C": [
        {"titulo": "As Crônicas de Nárnia", "autor": "C.S. Lewis"}
    ],
    "8D": [
        {"titulo": "O Homem que Calculava", "autor": "Malba Tahan"}
    ],
    "8E": [
        {"titulo": "Geografia: uma Introdução", "autor": "Carlos Alberto de Morais"}
    ],
    "8F": [
        {"titulo": "Geografia Humana", "autor": "Milton Santos"}
    ],
    "8G": [
        {"titulo": "A Natureza do Espaço", "autor": "Milton Santos"}
    ],
    "8H": [
        {"titulo": "Feliz Ano Velho", "autor": "Marcelo Rubens Paiva"}
    ],
}

# Variáveis para controle da navegação
linha_atual = 0
coluna_atual = 0
linhas, colunas = 8, 8

def iniciar_sistema():
    usuario = entrada_usuario.get().upper()
    if usuario.isalpha():
        janela_login.withdraw()
        mostrar_pagina_principal(usuario)
    else:
        messagebox.showerror("Erro", "Por favor, insira um nome válido.")

def mostrar_pagina_principal(usuario):
    janela_principal = tk.Toplevel()
    janela_principal.title("Biblioteca - IFPB")
    janela_principal.state('zoomed')  # Maximizar a janela principal
    janela_principal.config(bg="#f0f0f0")
    
    janela_principal.protocol("WM_DELETE_WINDOW", lambda: janela_login.deiconify() or janela_principal.destroy())

    cabecalho = tk.Frame(janela_principal, bg="#2E8B57", height=80)
    cabecalho.pack(fill="x")

    titulo = tk.Label(cabecalho, text="📚 Biblioteca IFPB 📚", font=("Segoe UI", 24, "bold"), fg="white", bg="#2E8B57")
    titulo.pack(pady=20)

    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
    label_data_hora = tk.Label(janela_principal, text=f"Data e Hora: {data_hora}", font=("Segoe UI", 12, "bold"), bg="#f0f0f0")
    label_data_hora.pack(pady=10)

    label_usuario: Label = tk.Label(janela_principal, text=f"Bem-vindo(a), {usuario}!", font=("Segoe UI", 14, "bold"), bg="#f0f0f0")
    label_usuario.pack(pady=10)

    label_opcoes = tk.Label(janela_principal, text="Selecione uma opção:", font=("Segoe UI", 14, "bold"), bg="#f0f0f0")
    label_opcoes.pack(pady=10)

    estilo_botao = {
        "width": 20, "height": 2, "font": ("Segoe UI", 12),
        "bg": "#4CAF50", "fg": "white", "relief": "flat", "bd": 0,
    }

    botao_prateleiras = tk.Button(
        janela_principal, text="Prateleiras", **estilo_botao,
        command=lambda: [mostrar_prateleiras(janela_principal, usuario)]
    )
    botao_prateleiras.pack(pady=15)

    botao_sair = tk.Button(
        janela_principal, text="Sair", **estilo_botao, command=lambda: [janela_principal.destroy()]
    )
    botao_sair.pack(pady=15)

def mostrar_prateleiras(janela_principal, usuario):
    global linha_atual, coluna_atual

    janela_principal.withdraw()
    janela_prateleiras = tk.Toplevel()
    janela_prateleiras.title("Prateleiras - Biblioteca IFPB")
    janela_prateleiras.state('zoomed')  # Maximizar a janela de prateleiras
    janela_prateleiras.config(bg="#f0f0f0")

    janela_prateleiras.protocol("WM_DELETE_WINDOW", lambda: janela_principal.deiconify() or janela_prateleiras.destroy())

    cabecalho_prateleira = tk.Frame(janela_prateleiras, bg="#2E8B57", height=50)
    cabecalho_prateleira.pack(fill="x")

    titulo_prateleira = tk.Label(cabecalho_prateleira, text="Prateleiras", font=("Segoe UI", 18, "bold"), fg="white", bg="#2E8B57")
    titulo_prateleira.pack(pady=10)

    frame_central = tk.Frame(janela_prateleiras, bg="#f0f0f0")
    frame_central.pack(expand=True, pady=20)

    fundo_matriz = tk.Frame(frame_central, bg="red", bd=5, relief="solid", highlightbackground="white", highlightthickness=2)
    fundo_matriz.pack(padx=10, pady=10, side="left")

    frame_prateleiras = tk.Frame(fundo_matriz, bg="red")
    frame_prateleiras.pack(pady=20)

    botoes = []

    def acessar_prateleira(linha, coluna):
        prateleira = f"{linha+1}{chr(65 + coluna)}"
        livros = get_livros_da_prateleira(prateleira)
        mostrar_mensagem_livros(livros, prateleira)
        
        for linha_botoes in botoes:
            for botao in linha_botoes:
                botao.config(bg="red")
        botoes[linha][coluna].config(bg="#2E8B57")


        janela_prateleiras.focus_set()

    for l in range(linhas):
        linha_botoes = []
        for c in range(colunas):
            botao = tk.Button(
                frame_prateleiras, text=f"{l+1}{chr(65 + c)}", bg="red",
                width=6, height=2, font=("Segoe UI", 9, "bold"), fg="white",
                command=lambda i = l, j = c: [acessar_prateleira(l, c)]
            )
            botao.grid(row=l, column=c, padx=5, pady=5)
            botao.config(borderwidth=4, relief="solid", highlightbackground="white", highlightthickness=1)
            linha_botoes.append(botao)
        botoes.append(linha_botoes)

    def mover_cursor(event):
        global linha_atual, coluna_atual
        
        if event.keysym == "Up" and linha_atual > 0:
            linha_atual -= 1
        elif event.keysym == "Down" and linha_atual < linhas - 1:
            linha_atual += 1
        elif event.keysym == "Left" and coluna_atual > 0:
            coluna_atual -= 1
        elif event.keysym == "Right" and coluna_atual < colunas - 1:
            coluna_atual += 1
        
        for linha_botoes in botoes:
            for botao in linha_botoes:
                botao.config(bg="green")
        botoes[linha_atual][coluna_atual].config(bg="#2E8B57")


    janela_prateleiras.bind("<Up>", mover_cursor)
    janela_prateleiras.bind("<Down>", mover_cursor)
    janela_prateleiras.bind("<Left>", mover_cursor)
    janela_prateleiras.bind("<Right>", mover_cursor)

    def acessar_prateleira_com_enter(event):
        acessar_prateleira(linha_atual, coluna_atual)
        janela_prateleiras.focus_set()

    janela_prateleiras.bind("<Return>", acessar_prateleira_com_enter)

    botoes[linha_atual][coluna_atual].config(bg="#2E8B57")

    botao_voltar = tk.Button(
        janela_prateleiras, text="⬅️ Voltar", font=("Segoe UI", 12), bg="green",
        fg="white", relief="flat", command=lambda: [janela_prateleiras.destroy(), janela_principal.deiconify(), janela_principal.state("zoomed")]
    )
    botao_voltar.pack(pady=10, side="left")

def get_livros_da_prateleira(prateleira):
    return biblioteca.get(prateleira, [])

def mostrar_mensagem_livros(livros, prateleira):
    if livros:
        livros_texto = "\n".join([f"{livro['titulo']} - {livro['autor']}" for livro in livros])
        messagebox.showinfo(f"Prateleira {prateleira}", livros_texto)
    else:
        messagebox.showinfo(f"Prateleira {prateleira}", "Esta prateleira está vazia!")

# Tela de login
janela_login = tk.Tk()
janela_login.title("Login - Sistema de Biblioteca")
janela_login.state('zoomed')  # Maximizar a janela de login
janela_login.config(bg="#f0f0f0")

# Carregar e redimensionar a imagem da logomarca
logo = tk.PhotoImage(file="C:\\Users\\pedro\\Downloads\\projetodemac_matrizes\\IMAGES\\monteiro.png")  # Substitua pelo caminho correto da logomarca

# USE O PADRÃO: ACESSE A PASTA PROJETOMAC_MATRIZES ENTRE NA PASTA IMAGES E SELECIONE A IMAGEM DO CAMPUS MONTEIRO. APÓS ISSO BUSQUE POR PROPIEDADES E COPIE O CAMINHO DE \\PROJETOMAC_MATRIZES ANTES

logo_redimensionada = logo.subsample(3)  # Ajuste o valor conforme necessário para redimensionar a imagem

# Título da tela de login
cabecalho_login = tk.Frame(janela_login, bg="#2E8B57", height=80)
cabecalho_login.pack(fill="x")

titulo_login = tk.Label(cabecalho_login, text="📚 Sistema de Biblioteca 📚", font=("Segoe UI", 24, "bold"), fg="white", bg="#2E8B57")
titulo_login.pack(pady=20)

# Exibir logomarca abaixo do título
logo_label = tk.Label(janela_login, image=logo_redimensionada, bg="#f0f0f0")
logo_label.pack(pady=20)

# Entrada do nome de usuário
frame_usuario = tk.Frame(janela_login, bg="#f0f0f0")
frame_usuario.pack(pady=50)

label_usuario = tk.Label(frame_usuario, text="Nome de Usuário:", font=("Segoe UI", 14, "bold"), bg="#f0f0f0")
label_usuario.grid(row=0, column=0, padx=10)

entrada_usuario = tk.Entry(frame_usuario, font=("Segoe UI", 14), width=20)
entrada_usuario.grid(row=0, column=1, padx=10)

botao_entrar = tk.Button(
    janela_login, text="Entrar", font=("Segoe UI", 14, "bold"), width=20, height=2, bg="#4CAF50", fg="white",
    command=iniciar_sistema
)
botao_entrar.pack(pady=20)

janela_login.mainloop()
