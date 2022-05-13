from ast import Str
from functools import partial
from msilib.schema import ComboBox
from tkinter import *
from tkinter.ttk import Combobox
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def inicio(root):
    root.title("***MÉTODOS DE BÚSQUEDA***")
    root.geometry("1280x800")
    root.configure(bg='pink')
    titulo = Label(root, text="INTELIGENCIA ARTIFICIAL \n Soto Larios Maribella \n Torres Amezcua María Guadalupe \n Grupo A",
                   font=("Times New Roman", 15),foreground="black", background="#EDDEFA").pack()
    labelass = Label(root, text="CRUD del grafo", font=("Times New Roman", 12), background="pink").place(x=300, y=250)
    frame = Frame(root, width=700, height=500, background="#EDDEFA",
                  bd=1, relief="sunken").place(x=260, y=275)


def showGraph():
    nx.draw_networkx(G)
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    plt.show()


def recibiryGuardar():
    nodo1 = nodo1_var.get()
    nodo2 = nodo2_var.get()
    peso = peso_var.get()
    G.add_edge(nodo1, nodo2, weight=peso)


def crearGrafos(root):
    nodos1 = Entry(root, textvariable=nodo1_var).place(x=350, y=680)
    nodos2 = Entry(root, textvariable=nodo2_var).place(x=550, y=680)
    peso = Entry(root, textvariable=peso_var).place(x=750, y=680)
    guardar = Button(root, text="Guardar", command=lambda: recibiryGuardar(), height=3,
                     width=20).place(x=539, y=720)
    node1Label = Label(root, text="Nodo 1", background="#EDDEFA").place(x=350, y=650)
    node2Label = Label(root, text="Nodo 2", background="#EDDEFA").place(x=550, y=650)
    pesoLabel = Label(root, text="Peso", background="#EDDEFA").place(x=750, y=650)


def recibiryBorrarnono():
    nono = nodoB_var.get()
    G.remove_node(nono)


def borrarNono(root):
    Bnono = Button(root, text="Borrar Nodo", height=3, background="red",
                   width=20, command=lambda: recibiryBorrarnono()).place(x=539, y=470)
    nono = Entry(root, textvariable=nodoB_var).place(x=552, y=430)
    nonoLabel = Label(root, text="Nodo a borrar:", background="#EDDEFA").place(x=560, y=405)


def parte1():
    parte1 = Toplevel()
    parte1.title("Parte 1")
    parte1.geometry("980x350")
    parte1.configure(bg='#E8F8F5')
    titulo = Label(parte1, text="PARTE 1", font=("Times New Roman", 20), background="#E8F8F5").pack()
    recorr1 = Button(parte1, text="Recorrido 1", height=3, background="#31E5F4",
                     width=20, command=lambda: p11(r1Nodoi.get(), r1Nodof.get())).place(x=230, y=100)
    recorr2 = Button(parte1, text="Recorrido 2", height=3, background="#31E5F4",
                     width=20, command=lambda: p12(r2Nodoi.get())).place(x=430, y=100)
    recorr3 = Button(parte1, text="Recorrido 3", height=3, background="#31E5F4",
                     width=20, command=lambda: p13(r3Nodoi.get())).place(x=630, y=100)
    labelR1 = Label(parte1, text="Nodo inicial", background="#E8F8F5").place(x=230, y=180)
    r1NodoI = Entry(parte1, textvariable=r1Nodoi).place(x=230, y=200)

    labelR1f = Label(parte1, text="Nodo final", background="#E8F8F5").place(x=230, y=250)
    r1NodoF = Entry(parte1, textvariable=r1Nodof).place(x=230, y=270)

    labelR3 = Label(parte1, text="Nodo inicial", background="#E8F8F5").place(x=630, y=180)
    r3NodoI = Entry(parte1, textvariable=r3Nodoi).place(x=630, y=200)

    labelR3 = Label(parte1, text="Nodo inicial", background="#E8F8F5").place(x=430, y=180)
    r2NodoI = Entry(parte1, textvariable=r2Nodoi).place(x=430, y=200)


def parte2():
    parte2 = Toplevel()
    parte2.title("Parte 2")
    parte2.geometry("920x350")
    parte2.configure(bg='#E8F8F5')
    titulo = Label(parte2, text="PARTE 2", font=("Times New Roman", 20), background="#E8F8F5").pack()
    recorrA1 = Button(parte2, text="Recorrido Anchura", height=3, background="#31E5F4",
                      width=20, command=lambda: busquedaAunchura(P2r1Nodoi.get(), P2r1Nodof.get())).place(x=230, y=100)
    recorrP2 = Button(parte2, text="Recorrido Profundidad", height=3, background="#31E5F4",
                      width=20, command=lambda: busquedaProfundidad(P2r3Nodoi.get(), P2r2Nodoi.get())).place(x=430, y=100)

    labelR1 = Label(parte2, text="Nodo inicial", background="#E8F8F5").place(x=230, y=180)
    P2r1NodoI = Entry(parte2, textvariable=P2r1Nodoi).place(x=230, y=200)

    labelR1f = Label(parte2, text="Nodo final", background="#E8F8F5").place(x=230, y=250)
    P2r1NodoF = Entry(parte2, textvariable=P2r1Nodof).place(x=230, y=270)

    labelR3 = Label(parte2, text="Nodo inicial", background="#E8F8F5").place(x=430, y=180)
    P2r3NodoI = Entry(parte2, textvariable=P2r3Nodoi).place(x=430, y=200)

    labelR3 = Label(parte2, text="Nodo Final", background="#E8F8F5").place(x=430, y=250)
    P2r2NodoI = Entry(parte2, textvariable=P2r2Nodoi).place(x=430, y=270)


def busquedaAunchura(inicio, fin):
    T = dict(nx.bfs_successors(G, source=int(inicio)))
    hoal = T
    print(hoal)
    posibles = []
    llaves = []
    for key in hoal:
        posibles.append(hoal[key])
        llaves.append(key)
    final = int(fin)
    camino = []
    camino.append(final)
    for i in reversed(range(len(llaves))):
        for j in posibles[i]:
            if j == final:
                camino.append(llaves[i])
                final = llaves[i]
    camino.reverse()
    aux = camino[0]
    graficacionFinal = []
    aux2 = []
    for i in range(len(camino)-1):
        aux2 = []
        aux2.append(aux)
        aux2.append(camino[i+1])
        graficacionFinal.append(aux2)
        aux = camino[i+1]

    G90 = nx.Graph()
    G90.add_edges_from(graficacionFinal)
    nx.draw_networkx(G90)
    plt.axis("off")
    plt.show()


def busquedaProfundidad(inicio, fin):
    T = nx.dfs_successors(G, source=int(inicio))
    hoal = T
    posibles = []
    llaves = []
    for key in hoal:
        posibles.append(hoal[key])
        llaves.append(key)
    final = int(fin)
    camino = []
    camino.append(final)
    for i in reversed(range(len(llaves))):
        for j in posibles[i]:
            if j == final:
                camino.append(llaves[i])
                final = llaves[i]
    camino.reverse()
    aux = camino[0]
    graficacionFinal = []
    aux2 = []
    for i in range(len(camino)-1):
        aux2 = []
        aux2.append(aux)
        aux2.append(camino[i+1])
        graficacionFinal.append(aux2)
        aux = camino[i+1]

    G90 = nx.Graph()
    G90.add_edges_from(graficacionFinal)
    nx.draw_networkx(G90)
    plt.axis("off")
    plt.show()


def parte3():
    parte3 = Toplevel()
    parte3.title("Parte 3")
    parte3.geometry("980x350")
    parte3.configure(bg='#E8F8F5')
    titulo = Label(parte3, text="Parte 3", font=("Times New Roman", 20),background="#E8F8F5").pack()
    primeroMejor = Button(parte3, text="Busqueda primero el mejor", height=3, background="#31E5F4",
                          width=20, command=lambda: bfs(nodoim.get(), nodofm.get())).place(x=230, y=100)
    A = Button(parte3, text="Busqueda A*", height=3, background="#31E5F4",
               width=20, command=lambda: busquedaAstar(nodoia.get(), nodofa.get())).place(x=430, y=100)
    dijkstra = Button(parte3, text="Algoritmo de Dijkstra", height=3, background="#31E5F4",
                      width=20, command=lambda: busquedaDijkstra(nodoid.get(), nodofd.get())).place(x=630, y=100)

    labeliM = Label(parte3, text="Nodo inicial", background="#E8F8F5").place(x=230, y=180)
    NodoIM = Entry(parte3, textvariable=nodoim).place(x=230, y=200)

    labelif = Label(parte3, text="Nodo final", background="#E8F8F5").place(x=230, y=250)
    NodoFM = Entry(parte3, textvariable=nodofm).place(x=230, y=270)

    labeliA = Label(parte3, text="Nodo inicial", background="#E8F8F5").place(x=430, y=180)
    NodoIA = Entry(parte3, textvariable=nodoia).place(x=430, y=200)

    labelfA = Label(parte3, text="Nodo final", background="#E8F8F5").place(x=430, y=250)
    NodoFA = Entry(parte3, textvariable=nodofa).place(x=430, y=270)

    labeliD = Label(parte3, text="Nodo inicial", background="#E8F8F5").place(x=630, y=180)
    NodoID = Entry(parte3, textvariable=nodoid).place(x=630, y=200)

    labelfD = Label(parte3, text="Nodo final", background="#E8F8F5").place(x=630, y=250)
    NodoFD = Entry(parte3, textvariable=nodofd).place(x=630, y=270)


def busquedaAstar(inicio, final):
    astar = nx.astar_path(G, source=int(inicio), target=int(
        final), heuristic=None, weight='weight')

    aux = astar[0]
    graficacionFinal = []
    aux2 = []
    for i in range(len(astar)-1):
        aux2 = []
        aux2.append(aux)
        aux2.append(astar[i+1])
        graficacionFinal.append(aux2)
        aux = astar[i+1]

    G1 = nx.Graph()
    G1.add_edges_from(graficacionFinal)
    nx.draw_networkx(G1)
    plt.axis("off")
    plt.show()


def busquedaDijkstra(inicio, final):
    dij = nx.shortest_path(G, source=int(inicio), target=int(
        final), weight='weight', method='dijkstra')

    aux = dij[0]
    graficacionFinal = []
    aux2 = []
    for i in range(len(dij)-1):
        aux2 = []
        aux2.append(aux)
        aux2.append(dij[i+1])
        graficacionFinal.append(aux2)
        aux = dij[i+1]

    G1 = nx.Graph()
    G1.add_edges_from(graficacionFinal)
    nx.draw_networkx(G1)
    plt.axis("off")
    plt.show()


def bfs(inicio, final):
    all_paths = []
    paths = nx.all_simple_paths(G, source=int(inicio), target=int(final))
    for path in map(nx.utils.pairwise, paths):
        si = list(path)
        all_paths.append(si)
    cual = np.random.randint(0, len(all_paths))
    G1 = nx.Graph()
    G1.add_edges_from(all_paths[0])
    nx.draw_networkx(G1)

    plt.axis("off")
    plt.show()


def botones(root):
    Vgrafo = Button(root, text="Visualizar el grafo", background="yellow",
                    height=3, width=50, command=lambda: showGraph()).place(x=439, y=320)
    Bparte1 = Button(root, text="Parte 1", font=("Times New Roman", 10), background="#974195", foreground="white", height=3, width=20,
                     command=lambda: parte1()).place(x=339, y=160)
    Bparte2 = Button(root, text="Parte 2", font=("Times New Roman", 10), background="#974195", foreground="white", height=3, width=20,
                     command=lambda: parte2()).place(x=539, y=160)
    Bparte3 = Button(root, text="Parte 3", font=("Times New Roman", 10), background="#974195", foreground="white", height=3, width=20,
                     command=lambda: parte3()).place(x=739, y=160)
    Bgrafo = Button(root, text="Borrar Grafo", background="red", height=3,
                    width=50, command=lambda: borrar()).place(x=439, y=550)

def p11(inicio, final):
    all_paths = []
    paths = nx.all_simple_paths(G, source=int(inicio), target=int(final))
    for path in map(nx.utils.pairwise, paths):
        si = list(path)
        all_paths.append(si)
    cual = np.random.randint(0, len(all_paths))
    G1 = nx.Graph()
    G1.add_edges_from(all_paths[cual])
    nx.draw_networkx(G1)

    plt.axis("off")
    plt.show()

def p12(inicio):
    global cogido
    cogido = []
    if cogido != []:
        cogido = []
    else:
        cogido.append(inicio)
        parte12 = Toplevel()
        parte12.title("Parte 1,2")
        parte12.geometry("980x500")

        titulo = Label(parte12, text="Recorrido Guiado",
                       font=("Comic Sans MS", 20)).pack()
        T = nx.dfs_tree(G, source=int(inicio))
        si = list(T.edges())

        seleccion = int(inicio)
        posibles = []
        for i in range(len(si)):
            if(si[i][0] == seleccion):
                posibles.append(si[i][1])

        caminos = "Los caminos disponibles son: "
        for x in posibles:
            caminos += str(x) + ", "
        caminos = caminos[0:-2]
        caminosStV.set(caminos)
        nodos_cb = Label(parte12, textvariable=caminosStV,
                         font=("Comic Sans MS", 20)).pack()
        LabelNodo = Label(parte12, text="Selecciona un nodo: ").pack()
        nodo = Entry(parte12, textvariable=sel).pack()
        siguiente = Button(parte12, text="Siguiente",
                           command=lambda: cambioBox(sel.get(), inicio)).pack()


def cambioBox(seleccionado, inicio):
    T = nx.dfs_tree(G, source=int(inicio))
    si = list(T.edges())
    seleccion = int(seleccionado)
    posibles = []

    for i in range(len(si)):
        if(si[i][0] == seleccion):
            posibles.append(si[i][1])
    print(posibles)
    if posibles != []:
        cogido.append(seleccionado)
        caminos = "Los caminos disponibles son: "
        for x in posibles:
            caminos += str(x) + ", "
        caminos = caminos[0:-2]
        caminosStV.set(caminos)
    else:
        cogido.append(seleccionado)
        print(cogido)
        caminosStV.set("Fin del recorrido")
        aux = cogido[0]
        graficacionFinal = []
        aux2 = []
        for i in range(len(cogido)-1):
            aux2 = []
            aux2.append(aux)
            aux2.append(cogido[i+1])
            graficacionFinal.append(aux2)
            aux = cogido[i+1]
        print(graficacionFinal)

        G3 = nx.Graph()
        G3.add_edges_from(graficacionFinal)
        nx.draw_networkx(G3)

        plt.axis("off")
        plt.show()


def p13(inicio):
    T = nx.dfs_tree(G, source=int(inicio))
    si = list(T.edges())
    pos = nx.kamada_kawai_layout(T)
    nx.draw_networkx(T, pos=pos)
    plt.axis("off")
    plt.show()


def borrar():
    G.clear()


root = Tk()
nodo1_var = StringVar()
nodo2_var = StringVar()
peso_var = StringVar()
nodoB_var = StringVar()
r1Nodoi = StringVar()
r3Nodoi = StringVar()
r1Nodof = StringVar()
r2Nodoi = StringVar()

P2r1Nodoi = StringVar()
P2r3Nodoi = StringVar()
P2r1Nodof = StringVar()
P2r2Nodoi = StringVar()

nodoim = StringVar()
nodofm = StringVar()

nodoia = StringVar()
nodofa = StringVar()

nodoid = StringVar()
nodofd = StringVar()

nodo_cb = StringVar()
sel = StringVar()
caminos = ""
caminosStV = StringVar()

posibles = []
G = nx.Graph()

inicio(root)
botones(root)
crearGrafos(root)
borrarNono(root)
root.mainloop()
