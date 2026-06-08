#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Figure for Part XXIV: the quasi-periodic diffraction spectrum of twin-pair
correlation on the 6N skeleton. Renders the single-frequency interference tensor
R_q(j) (Part XX three states) and the cumulative R(j)=prod_q R_q(j) (Parts XX-XXII).
No seaborn dependency. Requires numpy, matplotlib.
"""
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

def inv(a, m):
    for x in range(1, m):
        if (a*x) % m == 1: return x
    return None
def Rq(j, q):
    i3 = inv(3, q)
    if j % q == 0:                              return q/(q-2)            # State A
    if (j-i3) % q == 0 or (j+i3) % q == 0:      return q*(q-3)/(q-2)**2   # State B
    return q*(q-4)/(q-2)**2                                                # State C

primes = [5,7,11,13,17,19,23,29,31,37]
js = np.arange(1, 36)
M = np.array([[Rq(j,q) for j in js] for q in primes])
R = np.prod(M, axis=0)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 9),
                               gridspec_kw={"height_ratios":[2.4,1]})
fig.suptitle("Quasi-periodic diffraction spectrum of twin-pair correlation "
             "on the 6N skeleton (closed-form $R(j)$, not prime data)",
             fontsize=13, fontweight="bold")

# --- (top) single-frequency interference tensor R_q(j) ---
norm = TwoSlopeNorm(vmin=0.55, vcenter=1.0, vmax=1.70)
im = ax1.imshow(M, aspect="auto", cmap="RdBu_r", norm=norm)
ax1.set_yticks(range(len(primes))); ax1.set_yticklabels(primes)
ax1.set_xticks(range(len(js)));     ax1.set_xticklabels([])
ax1.set_ylabel("spatial frequency (prime $q$)")
ax1.set_title("(A) single-frequency amplitude $R_q(j)$ — State A (constructive) "
              "marked $\\circ$; amplitude fades as $O(1/q^2)$ with $q$")
for i,q in enumerate(primes):
    for k,j in enumerate(js):
        if j % q == 0:
            ax1.plot(k, i, "o", ms=7, mfc="none", mec="k", mew=1.2)
cb = fig.colorbar(im, ax=ax1, fraction=0.025, pad=0.01)
cb.set_label("$R_q(j)$")

# --- (bottom) cumulative diffraction grating R(j) ---
ax2.bar(js, R, color="#4169e1", alpha=0.85, edgecolor="black", linewidth=0.5)
ax2.axhline(1.0, color="red", ls="--", lw=1.4, label="independent baseline $R=1$")
jmin = int(np.argmin(R)); jmax = int(np.argmax(R))
ax2.annotate(f"max two-body suppression\n$j=1$ (quadruplet)\n$R={R[jmin]:.2f}=\\mathfrak{{S}}_{{quad}}/\\mathfrak{{S}}_{{twin}}^2>0$",
             xy=(1,R[0]), xytext=(4.5,R[0]+0.45),
             arrowprops=dict(arrowstyle="->"), color="#8b0000", fontsize=8.5, fontweight="bold")
ax2.annotate(f"super-resonance\n$j=35=5\\cdot7$\n$R={R[jmax]:.2f}$",
             xy=(35,R[jmax]), xytext=(30,R[jmax]-0.55),
             arrowprops=dict(arrowstyle="->"), ha="center", color="#8b0000", fontsize=8.5, fontweight="bold")
ax2.set_xlabel("spatial shift $j$ on the 6N lattice")
ax2.set_ylabel("cumulative $R(j)$")
ax2.set_xlim(0.4, 35.6); ax2.set_xticks(js); ax2.tick_params(labelsize=8)
ax2.legend(fontsize=9)
fig.tight_layout(rect=[0,0,1,0.96])
fig.savefig("fig_lattice_diffraction.png", dpi=200)
fig.savefig("fig_lattice_diffraction.pdf")
print("wrote fig_lattice_diffraction.{png,pdf}")
print(f"R(1)={R[0]:.4f} (min, >0)  R(35)={R[34]:.4f} (max)")
