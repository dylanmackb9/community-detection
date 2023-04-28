# Motivation

My goal is to investigate a community detection task on related spotify artist data in the form of an indirected graph <img src="https://rawgit.com/dylanmackb9/community-detection/main/svgs/5201385589993766eea584cd3aa6fa13.svg?invert_in_darkmode" align=middle width=12.92464304999999pt height=22.465723500000017pt/>. Probability distribution P is proposed over vertex set <img src="https://rawgit.com/dylanmackb9/community-detection/main/svgs/a9a3a4a202d80326bda413b5562d5cd1.svg?invert_in_darkmode" align=middle width=13.242037049999992pt height=22.465723500000017pt/>. Taking the existing edge set, I will try to estimate a labeling among more frequently conneted vertices. 

I will use a generative model to label <img src="https://rawgit.com/dylanmackb9/community-detection/main/svgs/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode" align=middle width=9.86687624999999pt height=14.15524440000002pt/> verticies into <img src="https://rawgit.com/dylanmackb9/community-detection/main/svgs/89f2e0d2d24bcf44db73aab8fc03252c.svg?invert_in_darkmode" align=middle width=7.87295519999999pt height=14.15524440000002pt/> disjoint subsets <img src="https://rawgit.com/dylanmackb9/community-detection/main/svgs/2ed534979faa8dd3cae47784da4ef1d6.svg?invert_in_darkmode" align=middle width=65.64004589999999pt height=22.465723500000017pt/> I will refer to as communities. The goal is to find a labeling of the vertices <img src="https://rawgit.com/dylanmackb9/community-detection/main/svgs/d800b932464eae1442cd69af62a8f019.svg?invert_in_darkmode" align=middle width=8.21920935pt height=14.15524440000002pt/> such that edges occur more frequently between vertices that share a label than differently-labeled vertices. The probability of an edge between nodes <img src="https://rawgit.com/dylanmackb9/community-detection/main/svgs/6dbb78540bd76da3f1625782d42d6d16.svg?invert_in_darkmode" align=middle width=9.41027339999999pt height=14.15524440000002pt/> and <img src="https://rawgit.com/dylanmackb9/community-detection/main/svgs/6c4adbc36120d62b98deef2a20d5d303.svg?invert_in_darkmode" align=middle width=8.55786029999999pt height=14.15524440000002pt/> with labels <img src="https://rawgit.com/dylanmackb9/community-detection/main/svgs/19950c4a3d72388a94aeb532028650b9.svg?invert_in_darkmode" align=middle width=17.16525854999999pt height=14.15524440000002pt/> and <img src="https://rawgit.com/dylanmackb9/community-detection/main/svgs/427cc947be21a51a1864c29ff4aea221.svg?invert_in_darkmode" align=middle width=16.381368299999988pt height=14.15524440000002pt/> is, 

<<<<<<< HEAD

\begin{equation}
P_{uv} = 
\left\{ 
  \begin{array}{rl}
   P_{in} & \textrm{if} \; σ_u = σ_v \\
   P_{out} & \textrm{if} \; σ_u \neq σ_v
\end{array}\right\}
\end{equation}
=======
<p align="center"><img src="https://rawgit.com/dylanmackb9/community-detection/main/svgs/65b2b245c736ad17f658179f2ac21edd.svg?invert_in_darkmode" align=middle width=442.1874533999999pt height=39.452455349999994pt/></p>
>>>>>>> 29b0568 (wtf)


\
In general, for symmetric <img src="https://rawgit.com/dylanmackb9/community-detection/main/svgs/89f2e0d2d24bcf44db73aab8fc03252c.svg?invert_in_darkmode" align=middle width=7.87295519999999pt height=14.15524440000002pt/> x <img src="https://rawgit.com/dylanmackb9/community-detection/main/svgs/89f2e0d2d24bcf44db73aab8fc03252c.svg?invert_in_darkmode" align=middle width=7.87295519999999pt height=14.15524440000002pt/> matrix <img src="https://rawgit.com/dylanmackb9/community-detection/main/svgs/df5a289587a2f0247a5b97c1e8ac58ca.svg?invert_in_darkmode" align=middle width=12.83677559999999pt height=22.465723500000017pt/>, the probability of an edge existing between node <img src="https://rawgit.com/dylanmackb9/community-detection/main/svgs/4cd3abe9b30e86075dee49d55169fe99.svg?invert_in_darkmode" align=middle width=25.81002104999999pt height=22.465723500000017pt/> and <img src="https://rawgit.com/dylanmackb9/community-detection/main/svgs/1f5bbeebcbe2dd028fbd26cf27e08562.svg?invert_in_darkmode" align=middle width=26.411200199999985pt height=22.465723500000017pt/> is <img src="https://rawgit.com/dylanmackb9/community-detection/main/svgs/ea2306a8d1b4985c89ba5be73a9c95d9.svg?invert_in_darkmode" align=middle width=21.309055349999994pt height=22.465723500000017pt/>. 


\
The labelings <img src="https://rawgit.com/dylanmackb9/community-detection/main/svgs/d800b932464eae1442cd69af62a8f019.svg?invert_in_darkmode" align=middle width=8.21920935pt height=14.15524440000002pt/> can be modeled as random or non-random, and in this case I will assume labelings as fixed and nonrandom. The input to the problem consists of the vertices and edges with probabilities. Labelings are not known as they must be (approximately) inferred from the given data. I assume a binary labeling of even distribution:

\\
<p align="center"><img src="https://rawgit.com/dylanmackb9/community-detection/main/svgs/5db34ce8dc6eac2ffd0d3ccbc25aa000.svg?invert_in_darkmode" align=middle width=389.8459026pt height=16.438356pt/></p>
and
<p align="center"><img src="https://rawgit.com/dylanmackb9/community-detection/main/svgs/943e1f4c89ba42156fac1a1678da574c.svg?invert_in_darkmode" align=middle width=388.5911535pt height=16.438356pt/></p>
