# Muon Decay: Relativistic Effects on Muon Survival

A physics simulation written in Python that investigates how relativistic time dilation influences muon decay.

The project calculates the number of muons surviving after traveling through Earth's atmosphere and visualizes the results using scientific plots.

---

## Overview

Muons are unstable elementary particles with a very short lifetime. Despite this, many muons created in the upper atmosphere successfully reach Earth's surface.

This phenomenon is explained by Einstein's theory of relativity:

- Time moves differently for fast-moving particles.
- Moving clocks appear to run slower.
- Muons therefore survive longer from the perspective of an observer on Earth.

This simulation models these effects and compares the resulting muon survival counts.

---

## Physics Concepts

### Special Relativity

The Lorentz factor is:

γ = 1 / √(1 − v²/c²)

where:

- v = velocity of the muon
- c = speed of light

At relativistic speeds, time dilation increases the observed lifetime of muons.

---

### Gravitational Time Dilation

The simulation also includes gravitational effects using:

γ_GR = √(1 − 2Φ/c²)

where:

- Φ = gravitational potential
- c = speed of light

This accounts for the influence of Earth's gravity on the passage of time.

---

## Features

- Muon decay simulation
- Relativistic time dilation calculations
- Gravitational correction factor
- Scientific visualization with Matplotlib
- High-resolution graph generation
- Educational physics project

---

## Technologies Used

- Python
- NumPy
- SymPy
- Matplotlib

---

## Applications

### Particle Physics
Study the behavior and decay of unstable particles.

### Astrophysics
Understand cosmic ray muons traveling through Earth's atmosphere.

### Physics Education
Visualize relativity concepts through simulation.

### Scientific Computing
Combine symbolic and numerical methods for physical modeling.

---

## Output

The program generates a comparison graph showing:

- Relativistic muon survival
- Non-relativistic muon survival

The difference illustrates how time dilation affects particle lifetimes.

---

## Installation

```bash
pip install numpy matplotlib sympy
