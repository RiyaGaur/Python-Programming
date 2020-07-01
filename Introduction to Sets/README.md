A set is an unordered collection of elements without duplicate entries.
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

<h4>Example</h4>

>>> print set()
set([])

>>> print set('HackerRank')
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

>>> print set([1,2,1,2,3,4,5,6,0,9,12,22,3])
set([0, 1, 2, 3, 4, 5, 6, 9, 12, 22])

>>> print set((1,2,3,4,5,5))
set([1, 2, 3, 4, 5])

>>> print set(set(['H','a','c','k','e','r','r','a','n','k']))
set(['a', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print set({'Hacker' : 'DOSHI', 'Rank' : 616 })
set(['Hacker', 'Rank'])

>>> print set(enumerate(['H','a','c','k','e','r','r','a','n','k']))
set([(6, 'r'), (7, 'a'), (3, 'k'), (4, 'e'), (5, 'r'), (9, 'k'), (2, 'c'), (0, 'H'), (1, 'a'), (8, 'n')])
Basically, sets are used for membership testing and eliminating duplicate entries.

<h2> Task </h2>

Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Formula used:
<t>   Average = Sum of Distinct Heights / Totoal no or distinct Heights

<h2> Input Format </h2>

The first line contains the integer, N, the total number of plants.
The second line contains the N space separated heights of the plants.

<h2> Constraints </h2>

0 < N <= 100

<h2> Output Format </h2>

Output the average height value on a single line.

<h2> Sample Input </h2>

10<br>
161 182 161 154 176 170 167 171 170 174

<h2> Sample Output </h2>

169.375
