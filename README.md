# Numerical-Analysis
Solving Conjugate Gradient in Numeral Analysis
## Solving Linear Systems Using the Conjugate Gradient Method (Python)
### Project Overview
This  project demonstrates how to solve a system of linear equations using ideas from the **Conjugate Gradient (CG) method** in numerical analysis. The implementation is written in **Python** using NumPy and focuses on iterative approximation of the solution to:
[Ax = b]
where:
- (A) is a **symmetric and positive definite matrix**
- (b) is a given vector
The project illustrates how the solution improves across iterations and evaluates accuracy using a relative error measure.

---
### Mathematical Background
The Conjugate Gradient method is an efficient iterative algorithm for solving large linear systems without computing matrix inverses. It works by:
- Starting from an initial guess
- Iteratively updating the solution along **An-orthogonal (conjugate) directions**
- Minimizing the error at each step    
In this implementation:
- Two predefined orthogonal search directions are used
- Each iteration updates the solution using a scalar step size
- The final approximation is compared to the true solution
  
### Problem Definition
We solve the linear system:

<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/a42f7d61-4717-47de-ab8b-4f4100d30469" />

with an initial guess:

<img width="320" height="300" alt="image" src="https://github.com/user-attachments/assets/694f4b6b-c435-445a-9081-1fd0005710df" />

---

### Implementation Details
The algorithm proceeds as follows:

1. Define the matrix \(A\) and vector \(b\)
2. Choose an initial guess \(x_0\)
3. Define orthogonal search directions \(v_1\) and \(v_2\)
4. Compute the residual at each iteration
5. Update the solution using step sizes \(\alpha\) and \(\beta\)
6. Compute the **true solution** using NumPy for comparison
7. Evaluate accuracy using the **relative error (∞-norm)**

---

### File Structure
#### Important Note for Users
The matrix A, vector b, and initial guess x₀ provided in this code are *examples only.*
To solve your own problem, you must:
- Replace A with your own symmetric positive definite matrix.

- Replace b with your corresponding vector.

- Provide an appropriate initial guess x₀.

- The algorithm will then compute an approximate solution for your system.


*Note: Code Explanation*

The Python script performs the following steps:
- Defines the matrix A and vector b
- Initializes the starting guess x₀
- Defines orthogonal search directions
- Computes residuals at each iteration
- Updates the solution iteratively
- Computes the exact solution using NumPy
- Evaluates accuracy using the relative infinity norm



## 📈 

The program prints:

The solution after the first iteration (x1)

The solution after the second iteration (x2)

The relative error compared to the exact solution

*all depends on your matrices and vectors you're working it*
