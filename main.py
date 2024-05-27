import tkinter as tk
from tkinter import ttk

# cores
cor1 = "#1d9099"  # azul escuro
cor2 = "#2b364a"  # roxo escuro
cor3 = "#11130e"  # preto
cor4 = "#f77825"  # laranja
cor5 = "#d5d2c8"  # cinza

#variavel global 
valor_displey = "0"

# funcao para limpar o display
def limpar_display():
    global valor_displey
    valor_displey = "0"
    display_label.config(text=valor_displey)

#funcion para atualizar o valor do display
def atualizar_display(valor):
    global valor_displey
    valor_displey = valor
    display_label.config(text=valor_displey)

def somar(valor):
    global valor_displey
    valor_displey = str(float(valor_displey)) + float(valor)
    atualizar_display(valor_displey)

def subtrair(valor):
    global valor_displey
    valor_displey = str(float(valor_displey)) - float(valor)
    atualizar_display(valor_displey)

def multiplicar(valor):
    global valor_displey
    valor_displey = str(float(valor_displey)) * float(valor)
    atualizar_display(valor_displey)

def dividir(valor):
    global valor_displey
    valor_displey = str(float(valor_displey)) / float(valor)
    atualizar_display(valor_displey)
    
#funcion clicar 
def clicar_numero(valor):
    global valor_displey
    if valor_displey == "0":
        valor_displey = valor
        atualizar_display(valor_displey)
    else:
        valor_displey += valor
        atualizar_display(valor_displey)
    
def clicar_operacao(operacao):
    global valor_displey
    try:
        if operacao == "=":
            valor_displey = str(eval(valor_displey))
            atualizar_display(valor_displey)
        else:
            if valor_displey[-1] in ["+", "-", "/", "*", "%"]:
                valor_displey = valor_displey[:-1] + operacao
            else:
                valor_displey += operacao
                atualizar_display(valor_displey)
    except:
        limpar_display()
        valor_displey = "erro"
        atualizar_display(valor_displey)
        limpar_display()
        atualizar_display(valor_displey)



# janela
tamanho_janela = tk.Tk()
tamanho_janela.title("Calculadora")
tamanho_janela.configure(background=cor3)
tamanho_janela.geometry("351x347")

# frame para o display
display_frame = tk.Frame(tamanho_janela, width=270, height=50, bg=cor5)
display_frame.grid(row=0, column=0, sticky="nsew")
display_label = tk.Label(display_frame, text="0", bg=cor5, fg=cor3, anchor="e", font=("Helvetica", 18))
display_label.pack(side="right", padx=10, pady=10, fill="x", expand=True)

# frame para os botões
buttons_frame = tk.Frame(tamanho_janela, width=250, height=250, bg=cor3)
buttons_frame.grid(row=1, column=0, sticky="nsew")

# primeira linha de botões
button_1 = tk.Button(buttons_frame, text="C", bg=cor5, fg=cor3, font=("Helvetica", 14), width=6, height=2)
button_1.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
button_1.config(command=lambda: limpar_display())
button_2 = tk.Button(buttons_frame, text="%", bg=cor5, fg=cor3, font=("Helvetica", 14), width=5, height=2)
button_2.grid(row=0, column=2, padx=3, pady=5)
button_2.config(command=lambda: clicar_operacao("%"))
button_3 = tk.Button(buttons_frame, text="/", bg=cor4, fg=cor3, font=("Helvetica", 14), width=5, height=2)
button_3.grid(row=0, column=3, padx=3, pady=5)
button_3.config(command=lambda: clicar_operacao("/"))

# segunda linha de botões
button_4 = tk.Button(buttons_frame, text="1", bg=cor5, fg=cor3, font=("Helvetica", 14), width=6, height=2)
button_4.grid(row=1, column=0, padx=2, pady=2, sticky="ew")
button_4.config(command=lambda: clicar_numero("1"))
button_5 = tk.Button(buttons_frame, text="2", bg=cor5, fg=cor3, font=("Helvetica", 14), width=6, height=2)
button_5.grid(row=1, column=1, padx=2, pady=2, sticky="ew")
button_5.config(command=lambda: clicar_numero("2"))
button_6 = tk.Button(buttons_frame, text="3", bg=cor5, fg=cor3, font=("Helvetica", 14), width=5, height=2)
button_6.grid(row=1, column=2, padx=2, pady=2)
button_6.config(command=lambda: clicar_numero("3"))
button_7 = tk.Button(buttons_frame, text="*", bg=cor4, fg=cor3, font=("Helvetica", 14), width=5, height=2)
button_7.grid(row=1, column=3, padx=2, pady=2)
button_7.config(command=lambda: clicar_operacao("*"))

# terceira linha linha de botões
button_8 = tk.Button(buttons_frame, text="4", bg=cor5, fg=cor3, font=("Helvetica", 14), width=6, height=2)
button_8.grid(row=2, column=0, padx=2, pady=2, sticky="ew")
button_8.config(command=lambda: clicar_numero("4"))
button_9 = tk.Button(buttons_frame, text="5", bg=cor5, fg=cor3, font=("Helvetica", 14), width=6, height=2)
button_9.grid(row=2, column=1, padx=2, pady=2, sticky="ew")
button_9.config(command=lambda: clicar_numero("5"))
button_10 = tk.Button(buttons_frame, text="6", bg=cor5, fg=cor3, font=("Helvetica", 14), width=5, height=2)
button_10.grid(row=2, column=2, padx=2, pady=2)
button_10.config(command=lambda: clicar_numero("6"))
button_11 = tk.Button(buttons_frame, text="-", bg=cor4, fg=cor3, font=("Helvetica", 14), width=5, height=2)
button_11.grid(row=2, column=3, padx=2, pady=2)
button_11.config(command=lambda: clicar_operacao("-"))

# quarta linha linha de botões
button_12 = tk.Button(buttons_frame, text="7", bg=cor5, fg=cor3, font=("Helvetica", 14), width=6, height=2)
button_12.grid(row=3, column=0, padx=2, pady=2, sticky="ew")
button_12.config(command=lambda: clicar_numero("7"))
button_13 = tk.Button(buttons_frame, text="8", bg=cor5, fg=cor3, font=("Helvetica", 14), width=6, height=2)
button_13.grid(row=3, column=1, padx=2, pady=2, sticky="ew")
button_13.config(command=lambda: clicar_numero("8"))
button_14 = tk.Button(buttons_frame, text="9", bg=cor5, fg=cor3, font=("Helvetica", 14), width=5, height=2)
button_14.grid(row=3, column=2, padx=2, pady=2)
button_14.config(command=lambda: clicar_numero("9"))
button_15 = tk.Button(buttons_frame, text="+", bg=cor4, fg=cor3, font=("Helvetica", 14), width=5, height=2)
button_15.grid(row=3, column=3, padx=2, pady=2)
button_15.config(command=lambda: clicar_operacao("+"))

# quinta linha linha de botões
button_16 = tk.Button(buttons_frame, text="0", bg=cor5, fg=cor3, font=("Helvetica", 14), width=6, height=2)
button_16.grid(row=4, column=0, padx=2, pady=2, sticky="ew")
button_16.config(command=lambda: clicar_numero("0"))
button_17 = tk.Button(buttons_frame, text=".", bg=cor5, fg=cor3, font=("Helvetica", 14), width=6, height=2)
button_17.grid(row=4, column=1, padx=2, pady=2, sticky="ew")
button_17.config(command=lambda: clicar_numero("."))
button_18 = tk.Button(buttons_frame, text="=", bg=cor4, fg=cor3, font=("Helvetica", 14), width=6, height=2)
button_18.grid(row=4, column=2, columnspan=2, padx=5, pady=5, sticky="ew")
button_18.config(command=lambda: clicar_operacao("="))


# configurar redimensionamento
tamanho_janela.grid_rowconfigure(0, weight=1)
tamanho_janela.grid_rowconfigure(1, weight=4)
tamanho_janela.grid_columnconfigure(0, weight=1)

# loop da janela
tamanho_janela.mainloop()