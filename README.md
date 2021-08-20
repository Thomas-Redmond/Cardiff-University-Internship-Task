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
P700 | Random.seed() used inside the function game
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
P715 | X - axis should be ra / rb
P716 | Should be r_a / r_b for this match
P717 | Should be the probability for winning the game
P718 | Plot independant variable on x - axis
P719 | Don't use global variables
P720 | Use CSV module
