You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the Kth attribute and print the final resulting table. Follow the example given below for better understanding.

image

Note that K is indexed from 0 to M-1, where M is the number of attributes.

<h2> Note: </h2> If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.

<h2> Input Format </h2>

The first line contains N and M separated by a space.
The next N lines each contain M elements.
The last line contains K.

<h2> Constraints </h2>

1 <= N,M <= 1000 <br>
0 <= K < M <br>
Each element <= 1000

<h2> Output Format </h2>

Print the N lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

<h2> Sample Input </h2>

5 3 <br>
10 2 5 <br>
7 1 0 <br>
9 9 9 <br>
1 23 12 <br>
6 5 9 <br>
1

<h2> Sample Output </h2>

7 1 0 <br>
10 2 5 <br>
6 5 9 <br>
9 9 9 <br>
1 23 12
