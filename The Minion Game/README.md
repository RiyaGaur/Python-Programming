Kevin and Stuart want to play the <strong>'The Minion Game'</strong>.

<h2> Game Rules </h2>

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

<h2> Scoring </h2>

A player gets +1 point for each occurrence of the substring in the string S.

<h2> For Example: </h2>

String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.


Your task is to determine the winner of the game and their score.

<h2> Input Format </h2>

A single line of input containing the string S.
<strong>Note:</strong> The string S will contain only uppercase letters:[A-Z] .

<h2> Constraints </h2>

0 < len(S) <= 10^6

<h2> Output Format </h2>

Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.

<h2> Sample Input </h2>

BANANA

<h2> Sample Output </h2>

Stuart 12
