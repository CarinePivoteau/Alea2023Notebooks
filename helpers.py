from random import *
import time
import math
import sys
import matplotlib.pyplot as plt
import graphviz

#!{sys.executable} -m pip install graphviz
   
def flip_a_coin():
    return bool(getrandbits(1))

def random_permutation(n):
    p = list(range(1,n+1))
    shuffle(p)
    return p

###############################################################################
###############################################################################

def count_occurences(gen, nb):
    dico = {}
    for i in range(nb):
        tmp = str(gen())
        if tmp in dico:
            dico[tmp] += 1
        else:
             dico[tmp] = 1
    print("nb:", len(dico))
    for key in dico:
        print(key, "{0:.2f}".format(dico[key] / nb * 100))

def plot_time(gen, maxi, nb_steps = 20, nb=100):
    sizes, timings = [], []
    step = (maxi-1)//nb_steps
    for size in range(1, maxi, step):
        print(size, end=" ")
        sizes.append(size)        
        t1 = time.time()
        for _ in range(nb):
            gen(size)
        timings.append((time.time() - t1) / nb)
    plt.plot(sizes, timings)
    plt.show()
    
def plot_values(gen, maxi, nb_steps = 20, nb=100):
    sizes, values = [], []
    step = (maxi-1)//nb_steps
    for size in range(1, maxi, step):
        print(size, end=" ")
        sizes.append(size)        
        v = 0
        for _ in range(nb):
            v += gen(size)
        values.append(v / nb)
    plt.plot(sizes, values)
    plt.show()

###############################################################################
###############################################################################

def draw_tree_labelled(t,w,l):
    dot = graphviz.Graph(graph_attr={'size' : str(w)+","+str(l)}, node_attr={'shape':'circle', 'fillcolor ':'white', 'style':'filled', 'fixedsize':'true'})
    def draw(t,r):
        node = str(t[0])
        if len(t)==1:
            dot.node(node, fillcolor='white', fontcolor='white')
        else : 
            dot.node(node, fillcolor='black', fontcolor='black')
        dot.edge(r, node)
        for st in t[1:]:
            draw(st,node)
    draw(t,'0')
    display(dot)

def draw_tree_unlabelled(t,w,l):
    dot = graphviz.Graph(graph_attr={'size' : str(w)+","+str(l)}, node_attr={'shape':'circle', 'fillcolor ':'white', 'style':'filled', 'fixedsize':'true'})
    count = 1
    def draw(t,r):
        nonlocal count
        node = str(count)
        count += 1
        if len(t)==0:
            dot.node(node, fillcolor='white', fontcolor='white')
        else : 
            dot.node(node, fillcolor='black', fontcolor='black')
        dot.edge(r, node)
        for st in t[1:]:
            draw(st,node)
    draw(t,'0')
    display(dot)