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




