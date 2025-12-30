# Numerical-Analysis
Solving Conjugate Gradient in Numeral Analysis
## Solving Linear Systems Using the Conjugate Gradient Method (Python)
### 📌 Project Overview
This mini project demonstrates how to solve a system of linear equations using ideas from the **Conjugate Gradient (CG) method** in numerical analysis. The implementation is written in **Python** using NumPy and focuses on iterative approximation of the solution to:
[Ax = b]
where:
- (A) is a **symmetric and positive definite matrix**
- (b) is a given vector
The project illustrates how the solution improves across iterations and evaluates accuracy using a relative error measure.

---
## 📐 Mathematical Background
The Conjugate Gradient method is an efficient iterative algorithm for solving large linear systems without computing matrix inverses. It works by:
- Starting from an initial guess
- Iteratively updating the solution along **An-orthogonal (conjugate) directions**
- Minimizing the error at each step    
In this implementation:
- Two predefined orthogonal search directions are used
- Each iteration updates the solution using a scalar step size
- The final approximation is compared to the true solution
  
  ## 🧮 Problem Definition
We solve the linear system:

\[
A =
\begin{bmatrix}
3 & -1 & 1 \\
-1 & 6 & 2 \\
1 & 2 & 7
\end{bmatrix},
\quad
b =
\begin{bmatrix}
1 \\
0 \\
4
\end{bmatrix}
\]

with an initial guess:

\[
x_0 = \begin{bmatrix} 0 & 0 & 0 \end{bmatrix}
\]

---

## 🛠️ Implementation Details
The algorithm proceeds as follows:

1. Define the matrix \(A\) and vector \(b\)
2. Choose an initial guess \(x_0\)
3. Define orthogonal search directions \(v_1\) and \(v_2\)
4. Compute the residual at each iteration
5. Update the solution using step sizes \(\alpha\) and \(\beta\)
6. Compute the **true solution** using NumPy for comparison
7. Evaluate accuracy using the **relative error (∞-norm)**

---

## 📂 File Structure
