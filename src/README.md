# Installing Plugin for development environment
*.\env\Scripts\activate*  

*pip install -e .*  

*flake8 E:\Thomas\Documents\#Python_Developement_Project\Code_reference\Squash\squash.py*

This will need to be redone with changes to setup.cfg
The plugin can be used at this stage.

# Installing Plugin for use
Note: python3 and py are interchangeable depending how your Python is set up

Creates virtual environment  
*py -m venv env*  

or

*conda create --clone base --name ccs*

Activates Virtual Environment
*.\env\Scripts\activate*  

or

*conda activate ccs*

Install Plugin Requirements  
*py -m pip install -r local/path/to/plugin/requirements.txt*  

or

*python -m pip install -r requirements.txt*

Install Plugin  
*python local/path/to/plugin/setup.py install*    

# Using Plugin
*flake8 filename.py*  
Runs flake8 on the designated file, performing all Flake8 and Plugin checks.

# Development Virtual Environment Reminder

Creates environment in local directory folder called "env", this variable can be changed  
*py -m venv env*  

Starts venv
*.\env\Scripts\activate*  

Outputs current module requirements being used  
*py -m pip freeze*  

Installs requirements in file "requirements.txt"  
*py -m pip install -r requirements.txt*

Stops venv  
*deactivate*  
