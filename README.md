# Motivation

  My objective is to investigate the behavior of random graphs with an underlying latent community structure. I will explore a random graph assumed to be produced from a generative model over some unknown probability distribution, and will analyze the performance of community detection and partial recovery techniques on the average case. I will then apply these methods to real-life data: a graphical representation of related artists through digital music service Spotify's Web API.
  
  
# Set up

  Begin with undirected graph $G$ with vertex set $V$ and edge set $E$. We investigate the possibility that $G$ has a latent community structure, meaning that vertices are connected via edges with varying densities. In this case, communities are groups of vertices where edges occur more frequently between each other than others. 
  
  To discover a latent community structure within graph $G$, we begin by assuming that $G$ was generated from a Stochastic Block Model. This model takes a vertex set $V$ with n nodes, a partition of the n vertices into r disjoint subsets $C_1,..,C_r$ that we call **communities**, and symmetric $r$ x $r$ matrix $P$ of edge probabilites, 

\
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

\
The edge set is then sampled at random so that two vertices $u$ and $v$ are connected by an edge with a probability dependent on whether they belong to the same community or not. Specifically, given $u∈C_i$ and $v∈C_j$, an edge exists between $u$ and $v$ with probability $P_{ij}$. 

In the case where there are two distinct communities, so $r=2$, $P$ becomes a symmetric $2$ x $2$ matrix with two distinct probabilities. The probability of an edge between $u∈C_i$ and $v∈C_j$ becomes,

\
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


  Given this structure, we define partial recovery as producing a labeling of nodes $\hat{\textbf{σ}}$ that is significantly more correlated with true labeling $\textbf{σ}$ than a random labeling. I will explore Spectral Clustering as a partial recovery technique, including an algorithmic nalysis of the performance in the worst and average case. 




