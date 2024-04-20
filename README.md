# Numerical PDE Solver

## Overview
This package provides numerical solutions to Partial Differential Equations (PDEs) using Euler and Milstein methods, tailored for use in financial mathematics and other fields requiring the numerical solution of stochastic differential equations.

## Installation
Install this package by running:
```bash
pip install numerical-pde-solver

##  Usage 

from numerical_pde_solver.euler import euler_method

# Define your drift and diffusion functions
def f(x, t):
    # Drift coefficient function
    return -x

def g(x, t):
    # Diffusion coefficient function
    return 0.1

# Initial condition, start time, end time, and step size
x0, t0, T, dt = 0, 0, 1, 0.01

# Solve the SDE
t, x = euler_method(f, g, x0, t0, T, dt)

# Now `t` holds the time points, and `x` holds the solution at those points
from numerical_pde_solver.milstein import milstein_method

# Define your drift and diffusion functions for the SDE
def f(x, t):
    # Drift coefficient function as a placeholder example
    return 0.05 * x

def g(x, t):
    # Diffusion coefficient function as a placeholder example
    return 0.2 * x

# Define the partial derivative of the diffusion function with respect to x
def dg(x, t):
    # For the diffusion term g(x, t) = 0.2 * x, the derivative with respect to x is 0.2
    return 0.2

# Initial condition, start time, end time, and step size
x0, t0, T, dt = 1, 0, 1, 0.01

# Solve the SDE using the Milstein method
t, x = milstein_method(f, g, dg, x0, t0, T, dt)

# t holds the array of time points, and x holds the array of solution values at those points

