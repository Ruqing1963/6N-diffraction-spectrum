# Part XXIV — The Quasi-Periodic Diffraction Spectrum of Twin-Pair Correlation

*Volume II of the Arithmetic Geodynamics programme on the 6N skeleton.*

Parts XX–XXII derived, in closed form, the spatial correlation of twin centres as
an infinite product `R(j) = ∏_{q>3} R_q(j)` of quantized single-frequency factors.
**This paper renders that closed form** as a two-panel *diffraction spectrum*.

Single-frequency states (Part XX), for prime q > 3 and shift j:

- **State A** (constructive): `R_q = q/(q−2)` when `q | j`
- **State B** (partial): `R_q = q(q−3)/(q−2)²` when `j ≡ ±3⁻¹ (mod q)`
- **State C** (destructive): `R_q = q(q−4)/(q−2)²` otherwise

### What the picture shows (window q ∈ {5,…,37}, j ∈ 1..35)

- **O(1/q²) spectral decay** — amplitude fades down the frequency axis; low primes
  (q ≤ 13) dominate the structure (Part XXII).
- **Maximal two-body suppression at j=1** (a prime quadruplet): every prime is in
  State C, and the cumulative product reaches its minimum
  `R(1) = 𝔖_quad/𝔖_twin² ≈ 0.41`. **This is a suppression, strictly positive — an
  admissible quadruplet, NOT annihilation.** Genuine zero-measure annihilation
  (R=0) needs the dead-sets to *tile* ℤ/q; the twin is immune to two-body
  annihilation, which is lowest-order three-body (Part XXI).
- **Super-resonance at j=35 = 5·7**: State A fires at both q=5 and q=7, lifting the
  cumulative product to its maximum `R(35) ≈ 2.26`.

## Layout

```
.
├── paper/    Chen_6N_Paper24.{tex,pdf} + figure
├── figures/  fig_lattice_diffraction.{pdf,png}
├── data/     R_j_table.csv  (j, R(j), with min/max notes)
├── code/
│   ├── fig_lattice_diffraction_make.py  # renders the two-panel spectrum (no seaborn)
│   └── verify_diffraction.py            # checks j=1 suppression, R(1)=S_quad/S_twin², j=35 resonance
├── CITATION.cff · .zenodo.json · LICENSE (MIT)
```

## Reproducing

```bash
pip install numpy matplotlib
python code/verify_diffraction.py          # all checks pass; writes data/
python code/fig_lattice_diffraction_make.py # regenerates the figure
```

Expected: j=1 all State C; `R(1)=0.4062` (min, > 0, = 𝔖_quad/𝔖_twin²); `R(35)=2.2566` (max).

## Scope

A visualization of the closed-form correlation R(j); at integer lags it equals the
discrete singular-series ratio. No new prime data, no infinitude claim. Continues
Part XXIII (doi:10.5281/zenodo.20586919).

## License

MIT — see `LICENSE`.
