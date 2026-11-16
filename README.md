# Python-Libraries-Implemented-in-C-Exploration
Exploring how to achieve high performance in Python by writing intensive programs in C.

https://canva.link/yk48o5pz9m4rdqx

I used AI as a learning tool to explore how C programs can be imported into Python programs, improving efficiency of computationally intensive operations. I wanted to explore how programs can integrate multiple languages to combine their best parts.

What I explored:

1. I practiced writing a simple C program which I then compiled into a shared library for a Python program to use.
  
2. I learned what ctypes is and is used for, and how it handles conversions between integers represented in Python and C, etc. To explore this, I wrote a function in C that takes two integers, adds them, and returns the result. I imported it into a main Python program. As part of this, I learned about the differences between how C and Python store integers, such as how Python has to store more information such as variable type and reference data.

3. I learned what NumPy is and how it supports efficient mathematical operations on entire arrays. To explore this library I ran small sample code pieces, such as matrix multiplication and tracking daily changes in a simulated stock price array.

4. I compared the performance of a C and Python program, squaring numbers from 1 to 1-million as a hands on way to learn why performance-critical operations are sometimes programmed in C rather than Python.

The versatility of NumPy was really intriguing to me and I'd like to use it in future programs.

Instructions for running code:

First compile the C code by running gcc -shared -o math_functions.dll math_functions.c
Then run either of the Python programs, and the result will be printed in the terminal
