We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

Let's try to understand this with an example.

You are given an immutable string, and you want to make changes to it.

Example

>>> string = "abracadabra"
You can access an index by:

>>> print string[5]
a
What if you would like to assign a value?

>>> string[5] = 'k' 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
How would you approach this?
<ul>
  <li>One solution is to convert the string to a list and then change the value.</li>
</ul>
<h2> Example </h2>

>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra
<ul>
    <li> Another approach is to slice the string and join it back.</li>
</ul>
<h2> Example </h2>

>>> string = string[:5] + "k" + string[6:]
>>> print string
abrackdabra
<h2> Task </h2>
Read a given string, change the character at a given index and then print the modified string.

<h2> Input Format </h2>
The first line contains a string, .
The next line contains an integer , denoting the index location and a character  separated by a space.

<h2> Output Format </h2>
Using any of the methods explained above, replace the character at index  with character .

<h2> Sample Input </h2>

abracadabra<br>
5 k

<h2> Sample Output </h2>

abrackdabra
