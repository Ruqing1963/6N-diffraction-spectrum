#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verifier + data for Part XXIV (diffraction spectrum of twin-pair correlation).

Checks, on the spectral window q in {5,...,37}, j in 1..35:
  (1) at j=1 every prime is in State C (no constructive/partial resonance);
  (2) R(1) is the cumulative MINIMUM and is strictly positive -- a suppression,
      equal to the quadruplet prefactor S_quad/S_twin^2, NOT an annihilation (R=0);
  (3) j=35=5*7 triggers State A at both q=5 and q=7 and is the cumulative MAXIMUM.
Also writes data/R_j_table.csv. Standard library only.
"""
import os, csv

PRIMES = [5,7,11,13,17,19,23,29,31,37]
def inv(a,m):
    for x in range(1,m):
        if (a*x)%m==1: return x
def state(j,q):
    i3=inv(3,q)
    if j%q==0: return "A"
    if (j-i3)%q==0 or (j+i3)%q==0: return "B"
    return "C"
def Rq(j,q):
    s=state(j,q)
    return {"A":q/(q-2),"B":q*(q-3)/(q-2)**2,"C":q*(q-4)/(q-2)**2}[s]
def R(j):
    p=1.0
    for q in PRIMES: p*=Rq(j,q)
    return p

def main():
    js=range(1,36)
    Rj={j:R(j) for j in js}
    jmin=min(js,key=lambda j:Rj[j]); jmax=max(js,key=lambda j:Rj[j])

    c1 = all(state(1,q)=="C" for q in PRIMES)
    print(f"(1) at j=1 every prime in State C: {c1}")

    # quadruplet prefactor S_quad/S_twin^2 on the same window
    Squad_over_Stwin2=1.0
    for q in PRIMES:
        Squad_over_Stwin2 *= (1-4/q)/((1-2/q)**2)   # = q(q-4)/(q-2)^2 = State C value
    c2 = (jmin==1) and (Rj[1]>0) and abs(Rj[1]-Squad_over_Stwin2)<1e-12
    print(f"(2) R(1)={Rj[1]:.4f} is min & >0 & equals S_quad/S_twin^2={Squad_over_Stwin2:.4f}: {c2}")

    c3 = (state(35,5)=="A" and state(35,7)=="A") and (jmax==35)
    print(f"(3) j=35: State A at q=5 and q=7, and global max R(35)={Rj[35]:.4f}: {c3}")

    here=os.path.dirname(os.path.abspath(__file__))
    out=os.path.join(os.path.dirname(here),"data"); os.makedirs(out,exist_ok=True)
    with open(os.path.join(out,"R_j_table.csv"),"w",newline="") as f:
        w=csv.writer(f); w.writerow(["j","R_j","note"])
        for j in js:
            note=""
            if j==jmin: note="min: max two-body suppression (quadruplet prefactor)"
            if j==jmax: note="max: super-resonance j=5*7"
            w.writerow([j,f"{Rj[j]:.6f}",note])
    print(f"\nwrote data/R_j_table.csv")
    print("ALL CHECKS PASS:", c1 and c2 and c3)

if __name__=="__main__":
    main()
