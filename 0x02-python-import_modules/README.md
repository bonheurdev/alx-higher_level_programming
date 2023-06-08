# **Python - Modules and Command Line Arguments**

This README.md file provides examples on concept of modules and command line arguments in Python.

## **Modules**

Modules in Python are files containing Python code that define functions, classes, and variables. They allow you to organize your code into reusable and manageable units. Here are a few key points about modules

## **Example: Importing and Using a Module**

```
import math

# Using the math module
print(math.sqrt(16))  # Output: 4.0
print(math.pi)        # Output: 3.141592653589793
```

## Command Line Arguments

Command line arguments allow users to pass information to a Python script directly from the command line. They are useful for customizing the behavior of a script without modifying the code.

## Example: Accessing Command Line Arguments

```
import sys

# Accessing command line arguments
print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])
```
