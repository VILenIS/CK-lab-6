# CK-lab-6
## 26. Условный экстремум.
**Определение**. Условным экстремумом функции $z=f(x,y)$ в точке $M0(x0;y0)$ называется экстремум этой функции, достигнутый при условии, что переменные $x$ и $y$ в окрестности данной точки удовлетворяют уравнению связи $\phi (x,y)=0$. <br/>
Название «условный» экстремум связано с тем, что на переменные наложено дополнительное условие $\phi (x,y) = 0$ <br/>

**Метод множителей Лагранжа для функций двух переменных.** <br/>
**Функция Лагранжа**: $F(x,y) = f(x,y) + \lambda \phi (x,y)$ (параметр $\lambda$ называют множителем Лагранжа) <br/>
Необходимые условия экстремума задаются системой уравнений, из которой определяются стационарные точки: <br/>
$\frac{\delta F}{\delta x} = 0$ <br/>
$\frac{\delta F}{\delta y} = 0$ <br/>
$\phi (x,y) = 0$ <br/>
Достаточным условием, из которого можно выяснить характер экстремума, служит знак: <br/>
$d^2F = F_(xx)''$ <br/>
Если в стационарной точке $d^2F > 0$, то функция $z = f(x,y)$ имеет в данной точке условный минимум, если же $d^2F < 0$, то условный максимум.<br/>

**Метод множителей Лагранжа для функций n переменных.** <br/>
'	'Допустим, мы имеем функцию n переменных z=f( \x1,x2,…,xn) \ и m уравнений связи ( \n>m) \:
	\phi 1( \x1,x2,…,xn) \=0; \phi 2( \x1,x2,…,xn) \=0, …, \phi m( \x1,x2,…,xn) \=0.
Обозначив множители Лагранжа как λ1,λ2,…,λm, составим функцию Лагранжа:
	F(x_1,x_2,…,x_n,λ1,λ2,…,λm)=f+ λ1\phi 1+ λ2\phi 2+ … + λn\phi m
Необходимые условия наличия условного экстремума задаются системой уравнений, из которой находятся координаты стационарных точек и значения множителей Лагранжа:
((\delta F)/(\delta xi)=0 ; ( \ i \in [ \1,n] \) \@\phi j=0; ( \ j\in [ \1,m] \) \)

