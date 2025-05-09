# RepMat: Representation theory of finite groups in Python.

**RepMat**: Representation theory of finite groups in Python. RepMat also includes the creation of other custom or predefined mathematical objects in abstract algebra such as fields and vector spaces of n- or infinite dimensions.

## Description

RepMat is a Python library which aims to provide a comprehensive toolkit for constructing and analyzing mathematical structures central to representation theory. It enables users to define groups, fields, and vector spaces, facilitating the creation of representations according to their formal definition.

## Getting Started

## Defining/Operating On Representations 

In this tutorial we will explore some of RepMat's 'built-in' representations, look at creating our own, then see what basic operations we can perform on them.

RepMat allows the user to create a representation as follows:

```python
import RepMat

new_representation = RepMat.Rep(group, matrices, vspace)
```

So our standout function requires us to (1) define a group, (2) a list of matrices, and (3) a vector space. Before diving into creating our own custom representations, let's explore RepMat's built in groups and vector spaces.

### Vector Spaces

In RepMat we must define a vector space over a specified field K. For fields, RepMat provides a host of 'elementary' infinite fields like $$, $$, and $$, but also allows for the creation of finite, or Galois, fields with the integers mod p where p is a prime number.

```python


```

To create a vector space, we must 
For example, 

```python
basis_vectors = [np.array([1, 0]), np.array([0, 1])]
vspace = RepMat.VctSp(RepMat.Reals, basis_vectors)

```

These simple mathematical objects can be used in midly interesting way. For instance,

```python
fggg
```

### Groups

```python
C8 = Cyclic(8)
RepMat.Display(C8)
```

We can also return values from the group and add elements of the group like this

```python

sum = RepMat.Optn(RepMat.GroupElements(C8, 4), RepMat.GroupElements(C8, 4))
print(sum)
```

We can create our own custom groups using the RepMat.Group() function:

```python
elements = [0, 1, 2, 3]
operation = lambda a, b: (a + b) % 4
custom_group = RepMat.Group(elements, operation)
RepMat.Display(custom_group)
```
If the user's choice of elements and operation don't fit the group axioms, an informative error will appear in their terminal.

RepMat has many other elementary groups, such as symmetric, dihedral, klein-4, and even quarternion groups, but their functionality in RepMat is mainly designed as a means to an end to create representations. 

### Representations and their operations

Now let's create a representation of the cyclic group with 8 elements. We have a group, a vector space, and we also need the set of matrix representations themselves. For large groups like C8, we will achieve this as follows using numpy:

```python

import numpy as np

# Number of elements in C8
n = 8

# Create the list of matrices
C8_matrices = []

for k in range(n):
    angle = 2 * np.pi * k / n
    matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle),  np.cos(angle)]
    ])
    C8_matrices.append(matrix)

rep = RepMat.Rep(C8, C8_matrices, R(1))

```

tbc....

## How to guides

### How create a character table

## Schur's Lemma

### Formal Definition of a Group Representation

Let $G$ be a group and $V$ be a vector space over a field $K$. A **representation** of $G$ on $V$ is a group homomorphism s.t.

$$
\rho: G \to \mathrm{GL}(V)
$$


where $\mathrm{GL}(V)$ denotes the general linear group of invertible linear transformations on $V$. This means that for all $g_1, g_2 \in G$,

$$
\rho(g_1 g_2) = \rho(g_1) \circ \rho(g_2)
$$

and

$$
\rho(e) = \mathrm{id}_V
$$

where $e$ is the identity element of $G$ and $\mathrm{id}_V$ is the identity transformation on $V$.

In this context, $\rho$ defines how each element of $G$ acts as a linear transformation on the vector space $V$, preserving the group structure. RepMat allows these groups to be leveraged with advanced utility functions such as tensor products and character tables.

According to this formal definition of a representation, RepMat must allow for the creation of vector spaces and fields. Although these mathematical objects aren't intended to be as interesting in isolation, we have implemented several utility functions which may be of use. Additionally, we have included the applications of some of Representation Theory's most notable theorems and lemmas in the tutorial as a demonstration of its mathematical soundness.




### Dependencies

* Sympy, Numpy
* Python

### Installing

To install the library, follow these steps:

#### 1. Install via GitHub

You can install the library directly from GitHub using `pip`. Run the following command in your terminal:

```bash
pip install git+https://github.com/george-elliott-git/RepMat
```

#### 2. Install via Pip

We are working on making the library available via PyPI. Once it's available, you will be able to install it using pip like this:

```
pip install repmat
```

Check back later for updates on this!

* Any modifications needed to be made to files/folders

### Executing program

* How to run the program
* Step-by-step bullets

## Reference

### List of functionality

This software implements a wide array of functions:

#### 1. Fields & Vector Spaces:
  ##### CREATION
1. `R(n)`
2. `C(n)`
3. `Z(n)`
4. `FiniteField(prime_number)` #creates a finite field
5. `VctSp(field, basis_vectors)` #creates a custom vector space
  ##### RECALL
7. `dim(VctSp)` #returns the numerical dimension of any given vector space


#### 2. Groups:
  ##### CREATION
1. `Cyclic(elements)` #creates cyclic group
2. `Perm(elements)` #creates permutation group
3. `Alt(elements)` #creates alternating group
4. `Dihl(elememts)` #creates dihedral group
5.  `modN(elements)` #creates modulo n group
6.  `K4(elements)` #creates Klein-4 group
7.  `Quat(elements)` #creates quaternion group
8.  `Group(elements, operation)` #creates custom group - use lambda operation
  ##### RECALL
10.  `GroupElements(group)`
11.  `Optn(group)`
12.  `Identity(group)`
13.  `Inverse(group)`

#### 3. Representations
  ##### CREATION
1. `Rep(group, matrices, vspace)`
  ##### RECALL
2. `Check_Homomorphism(rep_a, rep_b)`
3. `Check_Isomorphism(rep_a, rep_b)`

#### 4. Characters
  #### CREATION

  #### RECALL

#### 5. Utility Functions
1. `Display(Field/Vspace/Group/Representation)` #displays objects attributes


### Bibliography

The wikipedia page on the TSP offers good background reading:
https://en.wikipedia.org/wiki/Travelling_salesman_problem

The following text is a recommended text on neighbourhood search algorithms:

> Aarts, Emile, Emile HL Aarts, and Jan Karel Lenstra, eds. Local search in
> combinatorial optimization. Princeton Univers

