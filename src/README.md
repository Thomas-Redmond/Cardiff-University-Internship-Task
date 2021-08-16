# Installing Plugin for development environment
*.\env\Scripts\activate*  

*pip install -e .*  

*flake8 E:\Thomas\Documents\#Python_Developement_Project\Code_reference\Squash\squash.py*

This will need to be redone with changes to setup.cfg
The plugin can be used at this stage.

# Installation Guide
This guides presumes a venv virtual environment has already been created, and Python is called by the command line using "Python3". This may be different depending on your specific installation [try "py" or "Python"].

# Virtual Environment
Please install a virtual environment to use this Program. This will create an consist environment for the program to run in, without interfering with your main system.

## Venv
A virtual environment included with Python 3.

* *Python3 -m venv env* Create a virtual environment in current working directory called "env".
* *.\env\Scripts\activate* Begin venv session
  * Please note, with non-Windows OS the command is: *./env/Scripts/activate*
* *deactivate* End virtual environment session


## Windows
Starting in directory containing sub-folder created by virtual environment. We will call this folder env.  

* *.\env\Scripts\activate* Activate the virtual environment
* *Python3 -m pip install -r requirements.txt* Install all Python modules required to run in virtual environment. This step is only needed on the first installation.
* *Python3 setup.py install* Install the plugin
