Consider the following:
<ul>
    <li> A string, s, of length n where s=c0c1...cn-1.</li>
    <li> An integer, k, where k is a factor of n.</li>
</ul>
We can split s into n/k subsegments where each subsegment, ti, consists of a contiguous block of k characters in s. Then, use each ti to create string ui such that:
<ul>
    <li> The characters in ui are a subsequence of the characters in ti.</li>
    <li> Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. In other words, if the character at some index j in ti occurs at a previous index <j in ti, then do not include the character in string ui.</li>
</ul>
Given s and k, print n/k lines where each line i denotes string ui.

<h2> Input Format </h2>

The first line contains a single string denoting s.
The second line contains an integer, k, denoting the length of each subsegment.

<h2> Constraints </h2>
<ul>
  <li> 1 <= n <= 10^4 , where n is the length of s </li>
  <li>  1 <= k <= n </li>
  <li> It is guaranteed that n is a multiple of k. </li>
</ul>
<h2> Output Format </h2>

Print n/k lines where each line i contains string ui.

<h2> Sample Input </h2>

AABCAAADA <br>
3   

<h2> Sample Output </h2>

AB <br>
CA <br>
AD
