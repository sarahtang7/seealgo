# seealgo
A Python library to visualize a data structure as it changes throughout a function

[![](https://img.shields.io/badge/License-Apache_2.0-pink.svg)](./LICENSE) 
![](https://img.shields.io/github/issues/sarahtang7/seealgo)
![](https://img.shields.io/codecov/c/github/sarahtang7/see-algo/main?color=lightgreen)
[![CI](https://github.com/sarahtang7/seealgo/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/sarahtang7/seealgo/actions/workflows/main.yml)

## Overview
When writing algorithms, I often find that visualizing the data structures are necessary, but it can be difficult and time-consuming to do so. The goal of the seealgo library is to allow users to visualize a given data structure as it changes in a given function.

## Installation
This library requires you to have `graphviz` installed on your system using the [instructions](https://graphviz.org/download/) appropriate for your system, or by using the following command if you are on a macOS device: 
```
brew install graphviz
```
Then, install `seealgo` using the following command:
```
pip install seealgo
```

## Using seealgo
```python
from seealgo import List

visual_list = List()
test_list = [1, 2, 3, 4]

def append_to_list(input_list):
  input_list.append(5)
  return input_list

visual_list.see(append_to_list, test_list)
```
<img src="./outputFiles/eg_appendlist_before.png" width="400">
<img src="./outputFiles/eg_appendlist_after.png" width="500">
