import tkinter as tk

app = tk.Tk()
app.title('Calculadora Simples')
app.geometry('320x320+400+150')
app.configure(bg = 'blue')

def digito(ev):
    global e, lb
    #remove os zeros Ã  esquerda se o segundo caractere for dÃ­gito:
    if len(e) > 1 and e[1].isdigit():
        e = e.lstrip('0')
        lb.config(text=e)
    if ev.widget==b0:
        e+="0"
        lb.config(text=e)
    elif ev.widget==b1:
        e+="1"
        lb.config(text=e)
    elif ev.widget==b2:
        e+="2"
        lb.config(text=e)
    elif ev.widget==b3:
        e+="3"
        lb.config(text=e)
    elif ev.widget==b4:
        e+="4"
        lb.config(text=e)
    elif ev.widget==b5:
        e+="5"
        lb.config(text=e)
    elif ev.widget==b6:
        e+="6"
        lb.config(text=e)
    elif ev.widget==b7:
        e+="7"
        lb.config(text=e)
    elif ev.widget==b8:
        e+="8"
        lb.config(text=e)
    elif ev.widget==b9:
        e+="9"
        lb.config(text=e)

def opera(ev):
    global e,lb
    if ev.widget==bmais:
        e += "+"
        lb.config(text=e)
    elif ev.widget==bmenos:
        e += "-"
        lb.config(text=e)
    elif ev.widget==bvezes:
        e += "*"
        lb.config(text=e)
    elif ev.widget==bdiv:
        e += "/"
        lb.config(text=e)

def parenteses(ev):
    global e,lb
    if ev.widget==babre:
        e += "("
        lb.config(text=e)
    elif ev.widget==bfecha:
        e += ")"
        lb.config(text=e)

def finaliza(ev):
    global e,lb
    r = eval(e)
    e = str(r)
    lb.config(text=e)

def clear(ev):
    global e,lb
    e = "0"
    lb.config(text = e)

# Criando os widgets:
e=""  # A string que aparece no display da calculadora, inicialmente vazia.
lb = tk.Label(app, text = '', width = 21, height = 2, font = ('verdana', '14', 'bold'), bg = 'white')
lb.place(x = 20, y = 20)

b0 = tk.Button(app, text = '0', padx = 1, pady = 1, width = 4, height = 1, font = ('verdana', '11', 'bold'))
b0.place(x = 20, y = 80)

b1 = tk.Button(app, text = '1', padx = 1, pady = 1, width = 4, height = 1, font = ('verdana', '11', 'bold'))
b1.place(x = 78, y = 80)

b2 = tk.Button(app, text = '2', padx = 1, pady = 1, width = 4, height = 1, font = ('verdana', '11', 'bold'))
b2.place(x = 135, y = 80)

b3 = tk.Button(app, text = '3', padx = 1, pady = 1, width = 4, height = 1, font = ('verdana', '11', 'bold'))
b3.place(x = 190, y = 80)

b4 = tk.Button(app, text = '4', padx = 1, pady = 1, width = 4, height = 1, font = ('verdana', '11', 'bold'))
b4.place(x = 248, y = 80)

b5 = tk.Button(app, text = '5', padx = 1, pady = 1, width = 4, height = 1, font = ('verdana', '11', 'bold'))
b5.place(x = 20, y = 120)

b6 = tk.Button(app, text = '6', padx = 1, pady = 1, width = 4, height = 1, font = ('verdana', '11', 'bold'))
b6.place(x = 78, y = 120)

b7 = tk.Button(app, text = '7', padx = 1, pady = 1, width = 4, height = 1, font = ('verdana', '11', 'bold'))
b7.place(x = 135, y = 120)

b8 = tk.Button(app, text = '8', padx = 1, pady = 1, width = 4, height = 1, font = ('verdana', '11', 'bold'))
b8.place(x = 190, y = 120)

b9 = tk.Button(app, text = '9', padx = 1, pady = 1, width = 4, height = 1, font = ('verdana', '11', 'bold'))
b9.place(x = 248, y = 120)

bmais = tk.Button(app, text="+", padx=1, pady=1, width=4, height=1, font = ('verdana', '11', 'bold'))
bmais.place(x = 20, y = 160)
bmenos = tk.Button(app, text="-", padx=1, pady=1, width=4, height=1, font = ('verdana', '11', 'bold'))
bmenos.place(x = 78, y = 160)
bvezes = tk.Button(app, text="x", padx=1, pady=1, width=4, height=1, font = ('verdana', '11', 'bold'))
bvezes.place(x = 135, y = 160)
bdiv = tk.Button(app, text="/", padx=1, pady=1, width=4, height=1, font = ('verdana', '11', 'bold'))
bdiv.place(x = 190, y = 160)
bigual = tk.Button(app, text="=", padx=1, pady=1, width=4, height=3, font = ('verdana', '11', 'bold'))
bigual.place(x = 248, y = 162)
babre = tk.Button(app, text="(", padx=1, pady=1, width=4, height=1, font = ('verdana', '11', 'bold'))
babre.place(x = 20, y = 200)
bfecha = tk.Button(app, text=")", padx=1, pady=1, width=4, height=1, font = ('verdana', '11', 'bold'))
bfecha.place(x = 78, y = 200)
bclear = tk.Button(app, text="C", padx=1, pady=1, width=4, height=1, font = ('verdana', '11', 'bold'))
bclear.place(x = 135, y = 200)
boff = tk.Button(app, text="OFF", padx=1, pady=1, width=4, height=1, font = ('verdana', '11', 'bold'),command=app.quit)
boff.place(x = 190, y = 200)

b0.bind("<Button-1>", digito)
b1.bind("<Button-1>", digito)
b2.bind("<Button-1>", digito)
b3.bind("<Button-1>", digito)
b4.bind("<Button-1>", digito)
b5.bind("<Button-1>", digito)
b6.bind("<Button-1>", digito)
b7.bind("<Button-1>", digito)
b8.bind("<Button-1>", digito)
b9.bind("<Button-1>", digito)
bmais.bind("<Button-1>", opera)
bvezes.bind("<Button-1>", opera)
bmenos.bind("<Button-1>", opera)
bdiv.bind("<Button-1>", opera)
bigual.bind("<Button-1>", finaliza)
babre.bind("<Button-1>", parenteses)
bfecha.bind("<Button-1>", parenteses)
bclear.bind("<Button-1>", clear)

app.mainloop()