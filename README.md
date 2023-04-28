# Motivation

My goal is to investigate a community detection task on related spotify artist data in the form of an indirected graph $G$. Probability distribution P is proposed over vertex set $V$. Taking the existing edge set, I will try to estimate a labeling among more frequently conneted vertices. 

I will use a generative model to label $n$ verticies into $r$ disjoint subsets $C_{1},...,C_{r}$ I will refer to as communities. The goal is to find a labeling of the vertices $\textbf{σ}$ such that edges occur more frequently between vertices that share a label than differently-labeled vertices. The probability of an edge between nodes $u$ and $v$ with labels $\sigma_u$ and $\sigma_v$ is, 

$$
\begin{equation}
P_{uv} = 
\left\{ 
  \begin{array}{rl}
   P_{in} & \textrm{if} \; σ_u = σ_v \\
   P_{out} & \textrm{if} \; σ_u \neq σ_v
\end{array}\right\}
\end{equation}
$$

\
In general, for symmetric $r$ x $r$ matrix $P$, the probability of an edge existing between node $u∈C_{i}$ and $v∈C_{j}$ is $P_{ij}$. 


\
The labelings $\textbf{σ}$ can be modeled as random or non-random, and in this case I will assume labelings as fixed and nonrandom. The input to the problem consists of the vertices and edges with probabilities. Labelings are not known as they must be (approximately) inferred from the given data. I assume a binary labeling of even distribution:

\\
\begin{equation}
σ_{u}σ_{v} = 1 ,-1, 
\end{equation}
and
\begin{equation}
𝚺σ_{u} = 0  \quad  ∀ \:u∈V 
\end{equation}
