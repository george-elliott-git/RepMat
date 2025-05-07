# RepMat: Representation theory of finite groups in Python.

**RepMat**: Representation theory of finite groups in Python. RepMat also includes the creation of other custom or predefined mathematical objects in abstract algebra such as fields and vector spaces of n- or infinite dimensions.

## Description

RepMat is a Python library which aims to provide a comprehensive toolkit for constructing and analyzing mathematical structures central to representation theory. It enables users to define groups, fields, and vector spaces, facilitating the creation of representations according to their formal definition.

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

## Getting Started

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

