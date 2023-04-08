.. seealgo documentation master file, created by
   sphinx-quickstart on Fri Apr  7 23:39:39 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to seealgo's documentation!
===================================

seealgo is a Python library designed to help you visualize a data structure as it
changes throughout a function. Currently, seealgo provides functionality for lists
and binary search trees.


.. toctree::
   :maxdepth: 2
   :caption: Contents:



Installation
------------

This library requires you to have graphviz installed on your system using the instructions
appropriate for your system, or by using the following command if you are on a macOS device:

.. code-block:: rst

   brew install graphviz

Then, install seealgo using the following command:

.. code-block:: rst

   pip install seealgo


Using seealgo
-------------
The following is an example of using the seealgo library to
visualize appending a value to a list.

.. code-block:: python

   from seealgo import List

   visual_list = List()
   test_list = [1, 2, 3, 4]

   def append_to_list(input_list):
   input_list.append(5)
   return input_list

   visual_list.see(append_to_list, test_list)

.. image:: ./../outputFiles/eg_appendlist_before.png
   :width: 500
   :alt: Initial list data structure

.. image:: ./../outputFiles/eg_appendlist_after.png
   :width: 500
   :alt: List data structure with value of '5' appended


.. toctree::
   :maxdepth: 1
   :caption: Documentation:

   list
   tree
