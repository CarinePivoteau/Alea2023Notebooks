import random
import math

def draw(k_init, init, next, lbd):
    U = random.random()
    p = init
    S = init
    k = k_init
    while U > S:
        p = next(p, lbd, k)
        S += p
        k += 1
    return k

""" Bernoulli Law """
def bern(lbd):
    return random.random() < lbd


""" Geometric Law """
def next_geom(p, lbd, k):
    return lbd * p

def geom(lbd):
    return draw(0, (1 - lbd), next_geom, lbd)

def fast_geom(lbd):
    U = random.random()
    return (int)(math.floor(math.log(U) / math.log(lbd)))


""" Poisson Law """
def next_poiss(p, lbd, k):
    return lbd * p / (k + 1)

def poiss(lbd):
    return draw(0, math.exp(-lbd), next_poiss, lbd)

def non_zero_poiss(lbd):
    return draw(1, lbd / (math.exp(lbd) - 1), next_poiss, lbd)


""" Logarithmic Law """
def next_loga(p, lbd, k):
    return lbd * p * (k) / (k + 1)

def loga(lbd):
    return draw(1, -lbd / math.log(1 - lbd), next_loga, lbd)
