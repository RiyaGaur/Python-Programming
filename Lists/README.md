Consider a list (list = []). You can perform the following commands:
<ol>
    <li> insert i e: Insert integer e at position i. </li>
    <li> print: Print the list. </li>
    <li> remove e: Delete the first occurrence of integer e. </li>
    <li> append e: Insert integer e at the end of the list. </li>
    <li> sort: Sort the list. </li>
    <li> pop: Pop the last element from the list. </li>
    <li> reverse: Reverse the list. </li>
</ol>

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

<h2> Input Format </h2>

The first line contains an integer, n, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

<h2> Constraints </h2>
<ul>
    <li> The elements added to the list must be integers. </li>
</ul>

<h2> Output Format </h2>

For each command of type print, print the list on a new line.

<h2> Sample Input 0 </h2>

12 <br>
insert 0 5 <br>
insert 1 10 <br>
insert 0 6 <br>
print <br>
remove 6 <br>
append 9 <br>
append 1 <br>
sort <br>
print <br>
pop <br>
reverse <br>
print

<h2> Sample Output 0 </h2>

[6, 5, 10] <br>
[1, 5, 9, 10] <br>
[9, 5, 1]
