This challenge is only forPython 2.

<h2> input() </h2>
In <strong>Python 2</strong>, the expression input() is equivalent to eval(raw _input(prompt)).

Code

>>> input()  
1+2<br>
3
>>> company = 'HackerRank'
>>> website = 'www.hackerrank.com'
>>> input()
'The company name: '+company+' and website: '+website
'The company name: HackerRank and website: www.hackerrank.com'
<h2> Task </h2>

You are given a polynomial P of a single indeterminate (or variable), x.
You are also given the values of x and k. Your task is to verify if P(x) = k.

<h2> Constraints </h2>
All coefficients of polynomial P are integers.
x and y are also integers.

<h2> Input Format </h2>

The first line contains the space separated values of x and k.
The second line contains the polynomial P.

<h2> Output Format </h2>

Print True if P(x) = k. Otherwise, print False.

<h2> Sample Input </h2>

1 4<br>
x**3 + x**2 + x + 1

<h2> Sample Output </h2>

True
