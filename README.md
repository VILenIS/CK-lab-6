# CK-lab-6
## 26. Условный экстремум.
$\tab$**Определение**. Условным экстремумом функции $z=f(x,y)$ в точке $M0(x0;y0)$ называется экстремум этой функции, достигнутый при условии, что переменные $x$ и $y$ в окрестности данной точки удовлетворяют уравнению связи $\phi (x,y)=0$. <br/>
Название «условный» экстремум связано с тем, что на переменные наложено дополнительное условие $\phi (x,y) = 0$ <br/>

**Метод множителей Лагранжа для функций двух переменных.** <br/>
**Функция Лагранжа**: $F(x,y) = f(x,y) + \lambda \phi (x,y)$ (параметр $\lambda$ называют множителем Лагранжа) <br/>
Необходимые условия экстремума задаются системой уравнений, из которой определяются стационарные точки: <br/>
$\tab$$\frac{\delta F}{\delta x} = 0$ <br/>
$\tab$$\frac{\delta F}{\delta y} = 0$ <br/>
$\tab$$\phi (x,y) = 0$ <br/>
Достаточным условием, из которого можно выяснить характер экстремума, служит знак: <br/>
$\tab$$d^2F = F_{xx}''dx^2 + 2F_{xy}''dx^2dy^2 + F_{yy}''dy^2$ <br/>
Если в стационарной точке $d^2F > 0$, то функция $z = f(x,y)$ имеет в данной точке условный _минимум_, если же $d^2F < 0$, то условный _максимум_.<br/>

**Метод множителей Лагранжа для функций n переменных.** <br/>
Допустим, мы имеем функцию $n$ переменных $z=f(x_1,x_2,…,x_n)$ и $m$ уравнений связи $(n>m)$: <br/>
$\tab$$\phi_1(x_1,x_2,…,x_n) = 0$; $\phi_2(x_1,x_2,…,x_n) = 0$, $…,$ $\phi_m(x_1,x_2,…,x_n) = 0$. <br/>
Обозначив множители Лагранжа как $\lambda_1,\lambda_2,…,\lambda_m$ составим функцию Лагранжа: <br/>
$\tab$$F(x_1,x_2,…,x_n,\lambda_1,\lambda_2,…,\lambda_m) = f+ \lambda_1\phi_1 + \lambda_2\phi_2 + … + \lambda_n\phi_m$ <br/>
Необходимые условия наличия условного экстремума задаются системой уравнений, из которой находятся координаты стационарных точек и значения множителей Лагранжа: <br/>
$\tab$$\frac{\delta F}{\delta x_i} = 0$ ; $i \in [1,n]$<br/>
$\tab$$\phi j=0$ ; $j \in [1,m]$ <br/>


