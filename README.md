# HW4 – Building Stable Columns

## Description
This project solves **Homework 4: Building Stable Columns** for the *Data Structure and Database* course.

Given a set of blocks with three dimensions each, the goal is to build the most stable column using **either one block or two blocks**, such that the column's diameter (stability) is maximized.

The solution considers:
- Using a single block
- Stacking two compatible blocks
- Choosing the option with the maximum achievable diameter

---

## Student Information
- **Name:** Reza Salehinezhad  
- **Student ID:** 40434063  
- **Course:** Data Structure and Database  

---

## Project Structure
ds-hw4-column-optimization/
│── solution.py
│── input.txt
│── output.txt
│── README.md

---

## Requirements
- Python **3.6** or higher
- No external libraries required

---

## How to Run

### Method 1: Default Input
Make sure the input file exists at:
data/input.txt

Then run:
```bash
python solution.py

The output will be written to:
output.txt

Method 2: Custom Input and Output Paths
You can specify custom input and output files using command-line arguments:
python solution.py --input path/to/input.txt --output path/to/output.txt

Input Format
The first number is an integer n, the number of blocks
The next 3 × n integers represent the dimensions of each block

Example:
3
4 3 2
5 3 1
6 2 2

Output Format
First line: number of blocks used (1 or 2)
Second line: index (or indices) of selected block(s)
Third line: maximum achievable diameter

Example:
2
1 3
3


The solution automatically handles missing or empty input files.
File paths are relative, so the code works on any system.
The algorithm efficiently compares single-block and two-block configurations.

Author
Reza Salehinezhad


