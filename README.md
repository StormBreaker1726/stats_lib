# stats_lib

## What is stats_lib?

Stats_lib is an open-source Python library designed to handle large amounts of data from optimization algorithms. It provides a set of tools and functions to generate statistical data from CSV files with cost and time information.

## How to use stats_lib
To use stats_lib, you will need to have Python3 installed along with the pandas, os, and sys libraries. Additionally, you will need to provide files formatted in the correct way.

The first file required is a text file containing the names of all your instances. The second file is a CSV file containing at least two columns: "Cost" and "Time". These CSV files are generated by your code and contain information for each round of tests.

To run the program, use the following command line:

`python3 stats_main.py names_instances folder_containing_the_csv_files`

In this command, "names_instances" is the name of the file containing the names of all your instances, and "folder_containing_the_csv_files" is the name of the folder containing the CSV files used to generate the statistical data.

Two examples of formatted CSV files can be found in the examples folder.

## Contributors

Stats_lib was developed by João Víctor Costa de Oliveira.