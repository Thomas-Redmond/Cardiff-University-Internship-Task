# Cardiff_Coursework_Support

Provides feedback to first-year students for the module "Problem Solving With Python" in CS, during development.  
Examples such as "no need for global keyword", "return answer from function as a number not a string"


# Installing Plugin for use
Creates virtual environment  
*py -m venv env*  

Activates Virtual Environment
*.\env\Scripts\activate*  

Install Plugin Requirements  
*py -m pip install -r local/path/to/plugin/requirements.txt*  

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

# Installing Plugin for development environment
*pip install -e .*  

This will need to be redone with changes to setup.cfg
The plugin can be used at this stage.
