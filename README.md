# JupyterCheck - answerchecker for Jupyter


The ```jupytercheck``` library is intended to provide students with immediate feedback to check answers inside of a Jupyter notebook.  This was written with a Linear Algebra class in mind so it tries to do a robust comparison and take into consideration different object types as well as round off errors.


It works by providing a function called ```answercheck``` that takes in a variable to be checked and a "hash" which is a one-way function encoding the answer. The program generates a new hash based on the input variable and compares the two hash values. An output is provided that the answer appears correct or incorrect. 

The program is also designed to run without installing anything in python. However, it does require the download of the correct file. 