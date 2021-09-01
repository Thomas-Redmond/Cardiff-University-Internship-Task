# Development Readme

* *pip install -e .*
  * Install plugin as work-in-progress environment
  * Command will need to be run again if setup.cfg is modified

* *flake8 filename.py --enable-extension=P7*
  * Run flake8 on filename.py given absolute filename
  * Plugin disabled by default, needs to be enabled
  * Example : *flake8 E:\Thomas\Documents\#Python_Developement_Project\Code_reference\Squash\squash.py --enable-extension=P7*

### How does the system work ?

* Flake8 is started by the user with command *flake8 absolute/address/to/filename.py --enable-extension=P7*
* Flake8 starts and handles setup, this Program is activated by the Plugin Manager of Flake8
  * Therefore current working directory *cwd* command or similar WILL NOT work
  * Hence requirement for absolute system path from user
* Program is activated with the entry point of Linter.py's Plugin Class
  * Class is passed parameter of AST tree by flake8 of the file given by the user
  * Class saves parameter
  * Class creates instance of System Argument Parser to check given parameter and the address is absolute
    * if not, ends program with raised error

  * Class creates instance of Reporter class (saved to self.var)
    * Reporter Class is passed as parameter to the various error type handlers - making sure that only ONE reporter is used for the entire program
  * Class creates instance of AST_Router (handles [AST] errors)
  * Class creates instance of Unit_Testing (handles more traditional PyTest style errors)

* Flake8 then activates Plugin.run which returns a Generator error list [Flake8 requires it]
* Unit_Testing Controller object is run, with tests performed.
  * First test checks for functions used in throughout testing existence - if they are not there most of the test will not work and program will catch loads of errors
    * All good proceeds with other tests, otherwise raises error
  * Tests are [basic] type, with very similar code so are added to a list, and cycled through using a for loop 

  * AST_Router is called using imported Ast_NodeVisitor class (handles moving through an AST using special functions which can be overridden)
    * Class redirects to errors when specific function names are found (as often errors are only relevant to a specific function)
    * Specific error files also import Ast_NodeVisitor, and are setup using importing from sr/Errors/errorType
    * When errors are finished, any node traversal that is carried out inside the errors is not retained
  * AST_Router can be used for writing errors - if error should have global scope ie NO use of keyword global anywhere in the application
    * in which case for consistency Error class should still be created - and should report error in __init__ and NOTHING else
      * Example is P720.py






### Development Tips

* When deciphering AST nodes, use *print(f"Node is: {ast.dump(node)}")* often
  * This prints out the text-based description of the node to identify type and attributes.
  * Further nodes can be looked at by referring to the original ie node.func

* *.csv are included due to MANIFEST file when installing.
  * This is EVERY *.csv file in the entire system, should only be used for Errors/testData folder

* Errors should have a P7 prefix and follow P7xx convention
  * Flake8 config file specifies this, but only convention dictates its a 4 digit code.
  * For example, P789xYw is valid

* Errors can either be [basic] or [ast] type.
  * Classes are very similar with [ast] importing [basic] and overriding methods for maximum cohesion
    * Types are located in file "errorTypes" in src/Errors folder
  * failByDefault variables allow errors to be reported on start-up of test with a guilty-until-proven-innocent mentality
    * Some tests are easier to write this way
    * self.success() automatically handles removing these reports from the log presuming failByDefault var has been set to True
      * Otherwise self.success() does nothing - but helpful for legibility


#### Known Issues
* Program follows the src/ folder standard with exception of entry point file "Linter.py"
  * Flake8 entry points could not be made to access subfolder of compiled code, which required Linter.py (the main file) to be kept in project root
  * There should be a way to target subfolders, currently unknown

* Unit_Testing errors do not report location of where detected [line number, col offset] format
