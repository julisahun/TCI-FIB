from utilsP import divP, sumP, prodP, grauP
from utilsG import expG
import math

def EEP(poly1, poly2, grau, modulus):
  p1 = poly1
  p2 = poly2
  r = []
  w = p2
  while (grauP(p2, modulus) >= grau):
    [quotient, remainder] = divP(p1, p2, modulus)
    r.append(quotient)
    w = remainder
    p1, p2 = p2, remainder
  
  l1 = []
  l2 = [1]
  p1 = [1]
  p2 = []
  l, p = [], []
  for reminder in r: 
    l = sumP(l1, prodP(reminder, l2, modulus))
    p = sumP(p1, prodP(reminder, p2, modulus))
    l1, l2 = l2, l
    p1, p2 = p2, p
  return [w, p, l]

def genRS(r, b, modulus):
  g = [1]
  for i in range(r):
    g = prodP(g, [expG(b, i+1, modulus), 1], modulus)
  return g

def subsP(value, poly, modulus):
  remainder = divP(poly, [value, 1], modulus)[1] or [0]
  return remainder[0]

def sindRS(received, b, r, g):
  return [subsP(expG(b, i+1, g), received, g) for i in range(r)]

def sugiRS(syndrome, r, modulus):
  xr = [0] * r + [1]
  [w, p, _] = EEP(syndrome, xr, r//2, modulus)
  return [w, p]

def roots(pol, modulus):
  m = math.floor(math.log(modulus, 2))
  return [i for i in range(2**m) if (subsP(i, pol, modulus) == 0)]

def derivate(pol):
  d = []
  for i, e in enumerate(pol):
    if (i == 0): continue
    if (i % 2 == 0): d.append(0)
    else: d.append(e)
  return d