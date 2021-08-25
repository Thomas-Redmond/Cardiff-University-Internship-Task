# Developement Readme

* *pip install -e .*
  * Install plugin as work-in-progress environment
  * Command will need to be run again if either setup.cfg is modified
  * Plugin can be used, but source file pathing will be different to full installation

* *flake8 filename.py*
  * Run flake8 on filename.py given absolute filename
  * Example : *flake8 E:\Thomas\Documents\#Python_Developement_Project\Code_reference\Squash\squash.py*

### Developement Tips

* When deciphering AST nodes, use *print(f"Node is: {ast.dump(node)}")* often
  * This prints out the text-based description of the node to identify type and attributes.
  * Further nodes can be looked at by referring to the original ie node.func
