# PrettyCarnap
PrettyCarnap compiles natural deductions written in the format available in [carnap.io](https://carnap.io/)
into latex, utilizing the [following package](https://www.logicmatters.net/resources/fitch.sty).
# Example
```
Show: (PvS)->~(R^T)
 (PvQ)->~R :PR
 S->(~T^~U) :PR
 P :PR
 (PvS) :AS
 Show: P->~(R^T)
  P :AS
  PvQ :ADD6
  ~R :MP2,7
  Show: ~(R^T)
   R^T :AS
   R :S10
  :ID 8,11
 :CD9
 Show: S->~(R^T)
  S :AS
  ~T^~U :MP3,15
  ~T :S16
  Show: ~(R^T)
   R^T :AS
   T :S19
  :ID17,20
 :CD18
 ~(R^T) :D-AC4,5,14
:CD23
```
## Compiles into
```
\begin{fitch}
\fa (A\vee B)\rightarrow \neg C & PR  \\
\fa D\rightarrow (\neg E\wedge \neg F) & PR  \\
\fj A & PR  \\
\fh (A\vee D) & AS  \\
\fa\fh A & AS  \\
\fa\fa A\vee B & $\vee I$  12 \\
\fa\fa \neg C & MP  1,5 \\
\fa\fa\fh C\wedge E & AS  \\
\fa\fa\fa C & $\wedge E$  10 \\
\fa\fa \neg (C\wedge E) & $\neg I$ 6,8 \\
\fa A\rightarrow \neg (C\wedge E) & $\implies \!\!\!\! I$  7 \\
\fa\fh D & AS  \\
\fa\fa \neg E\wedge \neg F & MP  2,19 \\
\fa\fa \neg E & $\wedge E$  12 \\
\fa\fa\fh C\wedge E & AS  \\
\fa\fa\fa E & $\wedge E$  17 \\
\fa\fa \neg (C\wedge E) & $\neg I$ 13,15 \\
\fa D\rightarrow \neg (C\wedge E) & $\implies \!\!\!\! I$  14 \\
\fa \neg (C\wedge E) & AC  3,4,11 \\
 (A\vee D)\rightarrow \neg (C\wedge E) & $\implies \!\!\!\! I$  18 \\
\end{fitch}
```
## Which looks like
![image](https://github.com/mooddood235/PrettyCarnap/assets/62807754/a0a573b8-662b-4a0d-9e72-5c7263d2e714)


