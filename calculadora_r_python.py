import tkinter as tk # Importando uma biblioteca de criação de aplicativos e colocando apelido de tk para facilitar

# Função para inserir um número ou símbolo no campo de entrada

def inserir(valor) : # Inserindo valores quando clicar em algo
    """
        Insere o valor digitado ( número ou operador ) no final do campo de entrada
        Parâmetro :
            valor ( str ): o número ou símbolo a ser adicionado

    """
    entrada.insert(tk.END, str(valor)) # Adiciona o valor ao final do texto atual, ou seja, adicionando mais coisas

# Função para limpar os itens que estão no campo de entrada
def limpar() :
    """
        Limpa completamente o campo de entrada.
    """
    entrada.delete(0, tk.END) # Apaga do início ao fim, do índice de número 0 até o tk.END (FIM)


# Função para apagar apenas o último caractere
def apagar() :
    """
        Apaga apenas o último caractere digitado na caixa de entrada ( aonde aparece os números e resultados )
    """
    texto = entrada.get() # Pega o texto atual do campo (GET = Pegar)
    if texto : # Se o campo não estiver vazio ( Se o campo tiver algum número, ou seja válido (true) )
        entrada.delete(len(texto) - 1, tk.END) # Apaga o último caractere
        # Ele vai no tk.end ( no final ) e apaga o último caractere, ou seja, -1

def calcular() :
    """
        Avalia a expressão matemática digitada pelo usuário e mostra o resultado
        Se houver erro, por exemplo se divide por 0, ele dá erro
    """
    expressao = entrada.get() # Pega os números que estão na caixa de entrada ("Ex : 7+7*4")
    try : # O usuário vai tentar, ou seja, fazer o primeiro cálculo
        # A função eval() interpreta o texto como uma expressão matemática
        resultado = eval(expressao)
        """
            O Resultado vai ser calculado da seguinte forma
            Vou pegar a expressão que está como "7+7*4"
            nessa expressão eu vou deixar dentro de eval()
            eval prioriza a multiplicação e divisão e depois mais e menos
            Ele funciona como expressão númerica de equações
            ou seja, 4*7 = 28 + 4 = 32
        """

        # limpa a tela e mostra o resultado
        entrada.delete(0, tk.END) # Ele vai apagar tudo que está na caixa de entrada
        entrada.insert(0, str(resultado)) # E insere o resultado

    except Exception : # Se ele escrever algo errado, por exemplo: dividir por 0, dá exception
        # Se o usuário escrever algo errado
        entrada.delete(0, tk.END) # Apaga tudo que está na caixa de entrada
        entrada.insert(0, "Erro") # E mostra a mensagem de erro


#                                   Criação da Janela principal (interface)

# Cria a janela principal do aplicativo
root = tk.Tk() # Ele cria a janela do aplicativo

# Define o título da janela
root.title("Calculadora 2000 Generator")

# Define uma cor de fundo (opcional)
root.configure(bg="#f2f2f2")

#                                    Criação do campo de entrada (display)

# O entry é o local onde o usuário digita e vê os resultados.

entrada = tk.Entry( # Esta é a caixa de entrada que foi falada anteriormente
    root,               # Define que ela pertence à janela principal, ou seja, ela vai fazer parte do programa
    font=("Arial", 20),  # Define a fonte e tamanho do texto
    bd=5,                # Define a espessura da borda da caixa de entrada
    relief=tk.RIDGE,      # Define este tipo de borda como se fosse uma caixa 3D
    justify='right'      # Define que a caixa de entrada está justificada na direita

)

# Posiciona o campo na janela
entrada.grid( # Aonde a caixa de entrada vai estar
    row=0, column=0,         # Ele vai ficar na primeira linha e primeira coluna, ou seja, (0,0)
    columnspan=4,            # Ocupa 4 colunas (Operações númericas)
    padx=10, pady=10,         # espaçamento interno (padding é um espaçamento entre o espaço do aplicativo)
    sticky='we'              # faz o campo ocupar toda a largura

)


#                                     Criação dos botões da calculadora

# Lista de botões (texto, linha, coluna)
botoes = [
    ('C', 1, 0), ('⌫', 1, 1), ('(', 1, 2), (')', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),

]

# Cria cada botão a partir da lista acima
for (texto, linha, coluna) in botoes:
    # Define qual função será executada quando o botão for clicado
    if texto == 'C' :
        comando = limpar # botão "C" Executa a função de limpar dados
    elif texto == '⌫' :
        comando = apagar # Este botão executa a função de apagar o último caractere
    elif texto == '=' :
        comando = calcular # este botão executa o calcular, ou seja, aparece o resultado na tela
    else :
        # Para números e operadores, insere o texto no display
        comando = lambda t=texto: inserir(t) # Ele pega o botão que você clicou e transforma em número para entrar
        # na caixa de entrada, ou seja, apertei o botão 7, ele retorna o número 7 na caixa de entrada

    # Cria o botão
    botao = tk.Button(
        root,               # ele faz parte do aplicativo, ou seja, ele entra na janela principal
        text=texto,         # Texto mostrado no botão
        width=6, height=2,   # Tamanho dos botões dos números
        font=("Arial", 14),  # tipo de fonte e tamanho da fonte
        bg='#ffffff',        # Cor de fundo do botão
        relief=tk.RAISED,    # Estilo do botão
        command=comando      # O comando vai funcionar igual os comandos que estão lá em cima quando clica em algum botão


    )

    # Posiciona o botão no grid
    botao.grid(row=linha, column=coluna, padx=5, pady=5)


# Iniciar o loop principal

# O main loop() Mantém a janela aberta até o usuário fechá-la.
root.mainloop()


