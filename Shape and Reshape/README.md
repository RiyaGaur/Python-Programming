<h2> shape </h2>

The shape tool gives a tuple of array dimensions and can be used to change the dimensions of an array.

<h5>(a). Using shape to get array dimensions </h5>

import numpy

my__1D_array = numpy.array([1, 2, 3, 4, 5])<br>
print my_1D_array.shape     #(5,) -> 5 rows and 0 columns<br>

my__2D_array = numpy.array([[1, 2],[3, 4],[6,5]])<br>
print my_2D_array.shape     #(3, 2) -> 3 rows and 2 columns <br>
<h5>(b). Using shape to change array dimensions </h5>

import numpy

change_array = numpy.array([1,2,3,4,5,6])<br>
change_array.shape = (3, 2)<br>
print change_array <br>

#Output
[[1 2]<br>
[3 4]<br>
[5 6]]<br>

<h2>reshape</h2>

The reshape tool gives a new shape to an array without changing its data. It creates a new array and does not modify the original array itself.

import numpy

my_array = numpy.array([1,2,3,4,5,6])<br>
print numpy.reshape(my_array,(3,2))<br>

#Output
[[1 2]<br>
[3 4]<br>
[5 6]]

<h2> Task </h2>

You are given a space separated list of nine integers. Your task is to convert this list into a 3 X 3 NumPy array.

<h2> Input Format </h2>

A single line of input containing 9 space separated integers.

<h2> Output Format </h2>

Print the 3 X 3 NumPy array.

<h2> Sample Input </h2>

1 2 3 4 5 6 7 8 9

<h2> Sample Output </h2>

[[1 2 3] <br>
 [4 5 6] <br>
 [7 8 9]]
