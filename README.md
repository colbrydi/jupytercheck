# JupyterCheck - answerchecker for Jupyter


The ```jupytercheck``` library is intended to provide students with immediate feedback to check answers inside of a Jupyter notebook.  This was written with a Linear Algebra class in mind so it tries to do a robust comparison and take into consideration different object types as well as round off errors.


It works by providing a function called ```answercheck``` that takes in a variable to be checked and a "hash" which is a one-way function encoding the answer. The program generates a new hash based on the input variable and compares the two hash values. An output is provided that the answer appears correct or incorrect. 

The program is also designed to run without installing anything in python. However, it does require the download of the correct file. 

To install, include the following cell in all student jupyter notebooks (should work on any system regardless of installation permissions):

```python
import os.path
from urllib.request import urlretrieve
 if not os.path.isfile("answercheck.py"):
     urlretrieve('https://raw.githubusercontent.com/colbrydi/jupytercheck/master/answercheck.py', 'answercheck.py');
```

Once ```answercheck.py``` is included in the instructors/student's working directory the following code should work:

```python
from answercheck import checkanswer
checkanswer("Check Answer",'bd8337cd5327e54b2b4b15c6ec3703ed');
```

The second input to ```answercheck``` is the one-way "hash" and will change for every answer.  Getting the correct hash is easy as it will be printed out with the error message if the the input variable and the hash do not meet. An instructor only needs to run the function to get the correct has and copy and paste it into the second field.


In addition to the basic ```checkanswer``` function the following type dependent functions can be used:

* ```basic``` - Try to check any type of input variable.
* ```eq_matrix``` - Check for equivalent matrices (Same Reduced Row Echelon form)
* ```eq_vector``` - Check for equivalent vector (Any vector along the same direction)
* ```float``` - Check a float
* ```matrix``` - Compare two 2D matrices (element wise comparison)
* ```vector``` - Compare a single 1D vector of numbers (element wise comparison)

For example:

```python
f = 0.0110001
checkanswer.float(f, '9720dc655924528b17bcda523c3e5d48');
```

```python
import numpy as np

A = np.matrix([[1.0, 0.0], [0.0, 2.0]])
checkanswer.matrix(A, '943d90b283d21136da008160e002a5ce')
A2 = np.matrix(2*A)

checkanswer.eq_matrix(A, '16cc361c71445fb9d404292301b0a3fb')

A = np.matrix([[0.0, 2.0],[1.0, 0.0]])
checkanswer.eq_matrix(A, '16cc361c71445fb9d404292301b0a3fb')

A = np.matrix([[2.0, 0.0],[0.0, 1.0]])
checkanswer.eq_matrix(A, '16cc361c71445fb9d404292301b0a3fb')

A = np.matrix([[4,0],[0,100]])*A
checkanswer.eq_matrix(A, '16cc361c71445fb9d404292301b0a3fb')

A = np.matrix([[1.0, 0.0, 2], [0.0, 2.0, 1]])
checkanswer.eq_matrix(A, 'b975df4d16100051030dab90f432b14b')

A = np.matrix([[4,0],[0,100]])*A
checkanswer.eq_matrix(A, 'b975df4d16100051030dab90f432b14b')

```