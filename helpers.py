import time
import math
import sys
import random
import matplotlib.pyplot as plt
import graphviz

#!{sys.executable} -m pip install graphviz
   
def flip_a_coin():
    return bool(random.getrandbits(1))

def random_permutation(n):
    p = list(range(1,n+1))
    random.shuffle(p)
    return p

###############################################################################
###############################################################################

# renvoie un gen. en taille fixe en utlisant le générateur libre gen
def gen_random_fixed_size(gen, x, n): 
    nb_trials, size_trials = 0, 0
    while True :
        t,s = gen(x, n)
        nb_trials += 1
        size_trials += s
        if s == n:
            return nb_trials,size_trials,t

# renvoie un gen. en taille approchée en utlisant le générateur libre gen
def gen_random_approx_size(gen, x, mini, maxi):
    nb_trials, size_trials = 0, 0
    while True :
        t,s = gen(x, maxi)
        nb_trials += 1
        if nb_trials % 100 == 0 :
            print(".", end = "")
        size_trials += s
        if mini <= s <= maxi:
            print()
            return nb_trials,size_trials,t,s

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
    return dico

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

def counts_max_and_average(gen,nb): # pour tracer la distrib. des tailles
    counts = []
    discard = 0
    for i in range(nb):
        size = gen()
        if size > 0:
            counts.append(size)
        else:
            discard +=1
    print("trop grands = {}, taille max = {}, moyenne des tailles = {}".format(discard, max(counts), sum(counts)/nb))
    return counts

###############################################################################
###############################################################################

def draw_tree_labelled(t,w,l):
    dot = graphviz.Graph(graph_attr={'size' : str(w) + "," + str(l)}, node_attr={'shape':'circle', 'fillcolor ':'white', 'style':'filled', 'fixedsize':'true'})
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
    dot = graphviz.Graph(graph_attr={'size' : str(w) + "," + str(l)}, node_attr={'label':'','shape':'circle', 'fillcolor ':'white', 'style':'filled', 'fixedsize':'true'})
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

def draw_tree_unlabelled2(t,w,l): # arbres dont on compte uniquement les feuilles
    dot = graphviz.Graph(graph_attr={'size' : str(w)+","+str(l)}, node_attr={'label':'','shape':'circle', 'fillcolor ':'white', 'style':'filled', 'fixedsize':'true'})
    count = 1
    def draw(t,r):
        nonlocal count
        node = str(count)
        count += 1
        if len(t)==1:
            dot.node(node, fillcolor='black', fontcolor='black')
            dot.edge(r, node)
        else : 
            dot.node(node, label="", style='invis', width='0')
            dot.edge(r, node)
            for st in t:
                draw(st,node)
    draw(t,'0')
    display(dot)