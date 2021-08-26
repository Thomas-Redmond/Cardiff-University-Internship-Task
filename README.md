# Cardiff_Coursework_Support

Provides feedback to first-year students for the module "Problem Solving With Python" in CS, during development.  
Examples such as "no need for global keyword", "return answer from function as a number not a string"

# Installation Guide
This guides presumes a venv virtual environment has already been created, and Python is called by the command line using "Python3". This may be different depending on your specific installation [try "py" or "Python"].

# Virtual Environment
Please install a virtual environment to use this Program. This will stop module requirements from interfering with your main system.

### Venv
A virtual environment included with Python 3. Recommended to use with this program.

* *Python3 -m venv env*
  * Create a virtual environment in current working directory called "env".
* *.\env\Scripts\activate*
  * Begin venv session
  * Please note, for Linux OS the command is: *source ./bin/activate*
* *deactivate*
  * End virtual environment session

### Conda
A virtual environment for MacOS, and Linux terminal(s). Alternative option to use.
* *conda create --clone base --name ccs*
  * Create virtual environment
* *conda activate ccs*
  * Begin virtual environment session

## Windows
Starting in directory containing sub-folder created by virtual environment. We will call this folder env.  

* *.\env\Scripts\activate*
  * Activate the virtual environment
* *Python3 -m pip install -r requirements.txt*
  * Install all Python modules required to run in virtual environment. This step is only needed on the first installation.
* *Python3 setup.py install*
  * Install the plugin

# Using Plugin

* *flake8 filename.py*
  * Filename should be the absolute path to the file
  * Example: *flake8 E:\Thomas\Documents\#Python_Developement_Project\Code_reference\Squash\squash.py*

# Error List
Error Name | Description
--------------|----------------
P690 | Recommended function names are not detected.
P700 | Only use the seed for debugging / testing OUTSIDE the function
P701 | For loop is more appropriate in this function
P702 | Call the function game for 1a
P703 | Return answer from winProbability as a number
P704 | Returned answer should not be rounded
P705 | Pass filename as argument, do not hardcode
P709 | Question asked for a different function name
P710 | Skip the header row in data.csv
P711 | Convert tuples to numbers
P712 | Handle the extra column
P713 | Data should be sorted OR only plot points to avoid an untidy graph
P714 | Sorting values seperately loses connection between x and y
P716 | Should be r_a / r_b for this match
P717 | Should be the probability for winning the game
P718 | Plot independant variable on x - axis
P719 | Don't use global variables
P720 | Use CSV module

## Error Details
For a more detailed description of the specific error.

#### P690
Recommended Function names are not detected.
Test searches dir() of Squash namespace for function names: fails if any not found.

#### P700
Only use the seed for debugging / testing OUTSIDE the function.
If random.seed called inside function

#### P701
A For loop is more appropriate for this function.
Test searches for a for loop in use inside function "winProbability", fails if not found.

#### P702
Call the function game for 1a.
Test whether function game is called from function q1a.

#### P703
Return the answer from winProbability as a number.
Tests winProbability returns either an integer, float, or complex number

#### P704
Returned answer should not be rounded
Checks by calling 10 times with various parameter, if at least one a "float" pass.

#### P705
Pass filename as an argument, do not hardcode address
Tests that at least one parameter passed to function readCSV

#### P709
Question asked for different function name
Tests that the function game exists

#### P710
Skip the header row from data.csv
Using test.csv runs readCSV and compares output row length with desired row length

#### P711
Convert Tuples to numbers
Using test.csv runs readCSV and test that each value returned is either int / float / complex

#### P712
Handle the extra column in data.csv
Using test.csv runs readCSV and compares output column length with desired column length

#### P713
Data should be sorted OR only plot points to avoid an untidy graph
Checks uses plot is used with setting "o" or sorted function used.

#### P714
Sorting values seperately loses connection between x and y
If sorted function used more than once inside function fail.
