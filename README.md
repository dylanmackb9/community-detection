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








