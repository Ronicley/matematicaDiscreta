## Idempotência
### É definida como: 
Em matemática e ciência da computação, a **idempotência** é a propriedade que algumas operações têm de poderem ser aplicadas várias vezes sem que o valor do resultado se altere após a aplicação inicial
 ### Provar que $A=A\cup A$ (idempotência)
Deve-se mostrar que: (a) $A\subset(A\cup A)$ e (b) $(A\cup A)\subset A$.
- Como $A\subset (A\cup B)$, tomando $B=A$ segue que $A\subset(A\cup A)$.

- Seja $x\in A\cup A$. Segue que $x \in A$ ou $x\in A$

- Pela implicação lógica $p\lor p \rightarrow p$ segue que $x\in A$. Logo, $(A\cup A)\subset A$.

- Como $A\subset (A\cup A)$ e $(A\cup A)\subset A$, então pela definição de igualdade de conjuntos, conclui-se que $A=A\cup A$

## Comutativa
### É definida como:
É uma propriedade de operações binárias, ou de ordem mais alta, em que a ordem dos operandos não altera o resultado final. Ou popularmente, onde a *dos fatores não altera o produto*. 
- Seja $x\in (A\cap B)$. Então $x\in A$ e $x\in B$. Pela equivalência lógica $p\land q \Leftrightarrow q\land p$ segue que $x\in B$ e $x\in A$. Logo $x\in B\cap A$. Conclui-se que $A\cap B = B$
  

#### *1* Provar que $A\cup B=B \cup A$:

Seja $y \in (A \cup B)$. Então $y\in A$ ou $y \in B$. Pela equivalência lógica $p \lor q \Leftrightarrow q \lor p$ segue que $y \in B$ ou $y \in A$. Logo $y \in B \cup A$. Conclui-se que $A\cup B=B \cup A$.

#### *2* Provar que $A \cap B=B \cap A$:
Seja $x \in (A \cap B)$. Então $x \in A$ e $x \in B$. Pela equivalência lógica $p \land q \Leftrightarrow q \land p$ segue que $x \in B$ e $x \in A$. Logo $x \in B \cap  A$. Conclui-se que $A \cap B=B \cap A$.


## Associativa
### É definida como:
Em propriedade binária permite que expressões do tipo *r s t* possam ser escritas sem ambiguidades, ou seja, uma expressão *r s t* dá o mesmo resultado caso a operação que seja, em primeiro lugar, computada seja *r s* ou *s t*.

A associatividade é uma das três propriedades que definem um grupo, as demais sendo a lei do cancelamento (ou seja, se _r s = t s_ ou se _s r = s t_, então _r = t_), e a propriedade de que se na equação _x y = z_ dois elementos são fixos, então existe um terceiro que a satisfaz.

Seja *S* um conjunto e *f* uma operação binária neste conjunto. Dizemos que *f* é uma operação associativa se:
$$
\forall x, z \in S 
$$
$$
f(x, f(y,z))= f(f(x, y), z)
$$
Note que é importante que *f* seja uma operação binária, para que o resultado de *f(x, y)* ainda pertença a *S*.
 ### Provar que $A=A\cup A$ (idempotência)

## Distributiva

## Negação

## DeMorgan

## Elemento absorvente

## Absorção

## Referências
http://www.uel.br/projetos/matessencial/superior/analise/conjuntos.htm
http://www.uel.br/projetos/matessencial/superior/analise/conjuntos.htm
https://pt.wikipedia.org/wiki/Comutatividade
https://pt.wikipedia.org/wiki/Idempotência
