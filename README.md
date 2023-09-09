# Community Detection on Random Graphs 

## Motivation

  My objective is to investigate the behavior of random graphs produced by a  generative Stochastic Block Model. I will explore the performance of community  detection and partial recovery techniques in uncovering the latent community structure of these graphs, and will analyze these algorithms on the average case. Finally, I will apply these methods to real-life data: a graphical representation of related artists through Spotify's Web API.


## Set up

  Construct undirected graph $G$ with vertex set $V$ and edge set $E$. We want to explore the possibility that $G$ has a underlying community structure, meaning that vertices are connected via edges with varying densities. In this case, communities are groups of vertices where edges occur more frequently between each other than others.   
  
  We will use the Stochastic Block Model to analyze the community structure of random graph $G$. This model takes a vertex set $V$ with n nodes, a partition of the n vertices into r disjoint subsets $C_1,..,C_r$ that we call **communities**, and a symmetric $r$ x $r$ matrix $P$ of edge probabilites 

```math
\begin{equation}
P=
\begin{bmatrix}
P_{11} & \cdots & P_{1r}\\
\vdots & \ddots & \vdots\\
P_{r1} & \cdots & P_{rr}
\end{bmatrix}
\end{equation}
```



The edge set is then sampled at random so that two vertices $u$ and $v$ are  connected with probability as a function of the communities they belong to. Specifically, given $u∈C_i$ and $v∈C_j$, an edge exists between $u$ and $v$ with probability $P_{ij}$. 

In the case where there are two distinct communities $r=2$, $P$ becomes a symmetric $2$ x $2$ matrix with two distinct probabilities. The probability of an edge connecting $u∈C_i$ and $v∈C_j$ becomes

```math
\begin{equation}
P_{uv} = 
\left\{ 
  \begin{array}{rl}
   P_{in} & \textrm{if} \; i = j \\
   P_{out} & \textrm{if} \; i \neq j
\end{array}\right\}
\end{equation}
```

  Given this structure, we define partial recovery as producing a partition of nodes through labeling $\hat{\textbf{σ}}$ that is significantly more correlated with the true labeling $\textbf{σ}$ than a random labeling. I will explore dimensionality reduction through Spectral Clustering as a partial recovery technique, including an algorithmic analysis of the performance in the worst and average case. 



## Objective

I will begin with an assumption about our graph's probability parameters and structure. First, graph $G$ is assumed to be at least *weakly assortive*, meaning that $P_{ii} > P_{ij}$ $∀$ $C_i,C_j$, but with diagonals in $P$ only dominating their respective row and column. Descriptively, this means two vertices within a community share an edge with probability greater than a vertex within this community and a vertex in another. However, other vertices in other communities may have higher edge probabilities, suggesting uneven community densities. 


To further simplify analysis, we will later assume a planted partition model, where the $P$ probabilities on the diagonal are all constant $P_{in}$, and probabilities off the diagonal are constant $P_{out}$, with $P_{in}>P_{out}$.

In this simplified version, we will also assume that $r=2$ and we partition into two equal sized communities, so label $\textbf{σ}$ is a vector ${±1}^{n}$, and the sum of all labels over the vertex set $V$ is 0. 


We can now formalize our partial recovery objective by insisting that $\lvert ⟨\textbf{σ̂},\textbf{σ}⟩ \rvert ≥ (1-2ε)n$ for some $ε>0$. Therefore, a label $\textbf{σ}$ that meets this objective labels  $1-ε$ fraction of the vertices correctly.


## Community Detection 

Given this setup, we want to devise partial recovery technique that attempts to detect communities in graph $G$ by finding labeling $\textbf{σ}$ that adheres to our formalized objective.

I will be examining a specific Spectral Clustering technique to accomplish this task which utilizes the spectrum of a matrix representation to perform dimensionality reduction. This method takes advantage of the graph's Laplacian Matrix representation and its Algebraic Connectivity to study possible partitions in a lower dimensional space.

The basis of the proof of correctness and case analysis on this algorithm will  use a matrix extension of the Chernoff Bound called the Ahlswede-Winter Inequality, which exists in the larger space of matrix tail bounds. This inequalty gives a probability bound for the relative error between a sum of random, mutually independent, symmetric, positive semidefinite matrices $P$ and its expected value $\mathbb{E}[P]$ by using the eigenspace of $P$.

#### **Defining $A_G$**

Begin by constructing the adjacency matrix of $G$ in a way that deliberately introduces random matrices. Traditionally, the adjacency matrix of graph $G$ is a square matrix representation that takes on value 1 in spot $uv$ if an edge exists between node $u$ and $v$, and 0 otherwise.

Given vertex set $V$, take vector space $\mathbb{R}^V$ to be set of all real-valued functions mapping $\mathbb{R} → V$. In the set of functions $\mathbb{R}^V$, there exists a function for each vertex $v ∈ V$ that maps 1 to $v$ and 0 to all other vertices in V. This function is called the standard basis of vertex $v$, notated as a vector $\textbf{e}_{v}$ which is homomorphic to the function mapping.

Using this notation, an edge $uv$ in G can be represented in the adjacency matrix by setting the value at $uv$ and $vu$ to 1. Therefore the adjacency matrix of $G$ with vertex set $V$ and edge set $E$ can be represented as a sum of matrices,

```math
\begin{equation}
A_{G} = ∑_{{\{u,v\}}∈E} \textbf{e}_{u}\textbf{e}_{v}^⊤ + \textbf{e}_{v}\textbf{e}_{u}^⊤
\end{equation}
```

\
Since $G$ is generated from a stochastic block model, the edge set $E$ is sampled at random from the probability matrix $P$, making elements of $A_G$  all random variables taking on values 0 or 1 depending on probabilities $P_{in}$ or $P_{out}$. Therefore, the terms of this sum become independent symmetric random matrices by construction.


#### **Define $L_G$**

Using a similar method define the Laplacian Matrix of G.

```math
\
\begin{equation}
L_{G} = ∑_{\{u,v\}∈E} (\textbf{e}_{u} - \textbf{e}_{v})(\textbf{e}_{v}-\textbf{e}_{u})^⊤
\end{equation}
```

\
The Laplacian Matrix has special properties. The diagonal is the negation of the Degree Matrix, and the rest is the Adjacency matrix. Conveniently, each term of $L_{G}$ is also a symmetric positive semidefinite matrix.

It is easy to compute the expectation of $L_{G}$, $\mathbb{E}[L_{G}]$, which is as follows,


```math
\
\begin{equation}
\mathbb{E}[L_{G}]_{u,v} =
\left\{
  \begin{array}{lr}
  \frac{n}{2}(p_{in}+p_{out})-p_{in} & \textrm{if} \; u = v\\
  -p_{in} & \textrm{if} \; u \neq v, σ_{u} = \sigma_{v}\\
  -p_{out} & σ_{u} \neq \sigma_{v}
  \end{array}
\right\}
\end{equation}
```


\
When $u = v$ which occurs on the diagonal of $L_{G}$, then the expectation is $\frac{n}{2}(p_{in}+p_{out})-p_{in}$, meaning that the expected degree of each vertex is a function of the number of vertices n and probabilities $p_{in}$ and $p_{out}$. Otherwise, the reset of $L_{G}$ matches the negation of the adjacency matrix.

\
If we set $p = \frac{1}{2}(p_{in}+p_{out})$ and $q = \frac{1}{2}(p_{in}-p_{out})$, then a matrix for of the Laplacian Matrix is,

```math
\begin{equation}
\mathbb{E}[L_{G}]_{u,v} = pn\mathbb{1}-p\mathbf{1}\mathbf{1}^\top-q\textbf{σ}\textbf{σ}^\top
\end{equation}
```


The crux of my case analysis on the Spectral Clustering algorithm will use a matrix extension of the Chernoff Bound called the Ahlswede-Winter Inequality, which exists in the larger space of tail bounds for random matrices.

The Ahlswede-Winter Inequality attempts to bound the probability that random scalar $\langle\textbf{x}, P\textbf{x}\rangle$ deviates to the maximum degree from its expected value. In this quantity, $\textbf{x}$ is a vector in $\mathbb{R}^d$ and $P$ is a sum of random, mutually indepedent, symmetric, positive semidefinite matrices.




### **Proposition 1**

Let $P$ be a random symmetric positive semidefinite matrix in $\mathbb{R}^{dxd}$, and let $Q = \mathbb{E}[P]$. Suppose there exists constants $α_0$, $\kappa$, $n$ such that for all $\alpha$ in the interval $(0, \alpha_{0})$ and all vectors $\textbf{x} \in \mathbb{R}^d$, the random scalar quantity $\langle\textbf{x},P\textbf{x}\rangle$ satisfies

```math
\begin{equation}
Pr(η(\langle\textbf{x}, P\textbf{x}\rangle, \langle\textbf{x}, Q\textbf{x}\rangle) \geq \alpha) ≤ 2e^{-\kappa\alpha^{2}n}.
\end{equation}
```

Then for all $β\in (0, 2\alpha_{0})$,

```math
\begin{equation}
Pr \biggl( \mathop{\text{sup}}_{\textbf{x}\in\mathbb{R}^d}\eta(\langle\textbf{x}, P\textbf{x}\rangle, \langle\textbf{x}, Q\textbf{x}\rangle) \ge β \biggr) < 2exp \left( 7d - \frac{\kappa}{9}\beta^2n \right)
\end{equation}
```


### **Lemma 1**

Suppose $A$ is a symmetric matrix with eigenvalues $λ_1, λ_2,\ldots,λ_k$ and corresponding eigenspaces $V_1, V_2,\ldots,V_k$. The spaces $V_1,\ldots,V_k$ are pairwise orthogonal (meaning each vector in $V_i$ is orthogonal to each other vector $V_j$ when $1≤i<j≤k$) and every $\textbf{x}∈\mathbb{R}^n$ can be written uniquely in the form $\textbf{x} = a_1\textbf{x}_1+a_2\textbf{x}_2+\cdots+a_k\textbf{x}_k$, where $\textbf{x}_i$ is an element of $V_i$ satisfying $\lVert{\textbf{x}_i}\rVert_2 = 1$, for $i = 1,\ldots,k$. Furthermore,

```math
\begin{equation}
\langle\textbf{x}, A\textbf{x}\rangle = λ_1a_1^2+λ_2a_2^2+\cdots+\lambda_ka_k^2.
\end{equation}
```


### **The Ahlswede-Winter Inequality**

An exponential tail bound for Random Matrices, with only a polynomial dependence on dimension, as opposed to the exponential dependence proposition 1.

Suppose $P_1, P_2,...,P_m$ are mutually independent random, symmetric, positive semidefinite $d$ x $d$ matrices, let $P=P_1+$ $...+P_m$, and let $Q=\mathbb{E}[P]$. If $r>0$ is a scalar such that for all $i$ and all $x∈\mathbb{R}^{d}$, $\langle\textbf{x}, P_i\textbf{x}\rangle ≤ \frac{1}{r} \langle\textbf{x}, Q\textbf{x}\rangle$ with probability 1, then for all $β∈(0,1)$,

```math
\
\begin{equation}
Pr \biggl(\underset{\textbf{x}\in\mathbb{R}^d}{\text{sup}}\eta(\langle\textbf{x}, P\textbf{x}\rangle, \langle\textbf{x}, Q\textbf{x}\rangle) \ge \textit{β} \biggl) ≤2d \cdot e^{-\frac{1}{4}\textit{β}^2r}.
\end{equation}
```

\



















