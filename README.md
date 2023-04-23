<h1 align="center">ALU-AirBnB clone</h1>


## Description

ALU-AirBnB is a full-stack Web application built from scratch which comprize a command interpreter, a web interface, API and database. The goal of the project is to build a replica of the [Airbnb Website](https://www.airbnb.com/) and deploy it on server. The project is built using Python, HTML, CSS, Javascript, MySQL and SQLAlchemy. The final version of this project will have:

- A command interpreter to manipulate data without a visual interface, like a shell (for development and debugging)
- A website (front-end) with static and dynamic functionalities
- A comprehensive database to manage the backend functionalities
- An API that provides a communication interface between the front and backend of the system.

## Installation
* Clone this repository: `git clone "https://github.com/alexaorrico/AirBnB_clone.git"`
* Access AirBnb directory: `cd AirBnB_clone`
* Run hbnb(interactively): `./console` and enter command
* Run hbnb(non-interactively): `echo "<command>" | ./console.py`

## Project Architecture

The project is divided into different pieces. Here is a diagram of the project architecture:

![Project Architecture](./project_architecture.png)

## File Descriptions
[console.py](console.py) - the console contains the entry point of the command interpreter. 
List of commands this console current supports:
* `EOF` - exits console 
* `quit` - exits console
* `<emptyline>` - overwrites default emptyline method and does nothing
* `create` - Creates a new instance of`BaseModel`, saves it (to the JSON file) and prints the id
* `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file). 
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name. 
* `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). 

## Description of the command interpreter
| Commands  | Description |
| ------------- | ------------- |
| ```quit```  | Quits the console  |
| ```Ctrl+D```  | Quits the console  |
| ```help``` or ```help <command>```  | Displays all commands or Displays instructions for a specific command
| ```create <class>```  | Creates an object of type , saves it to a JSON file, and prints the objects ID
| ```show <class> <ID>```  | Shows string representation of an object
| ```destroy <class> <ID>```  | Deletes an objects
| ```all or all <class>```  | Prints all string representations of all objects or Prints all string representations of all objects of a specific class
| ```update <class> <id> <attribute name> "<attribute value>"```  | Updates an object with a certain attribute (new or existing)
| ```<class>.all()```  | Same as all ```<class>```
| ```<class>.count()```  | Retrieves the number of objects of a certain class
| ```<class>.show(<ID>)```  | Same as show ```<class> <ID>```
| ```<class>.destroy(<ID>)```  | Same as destroy ```<class> <ID>```
| ```<class>.update(<ID>, <attribute name>, <attribute value>```  | Same as update ```<class> <ID> <attribute name> <attribute value>```
| ```<class>.update(<ID>, <dictionary representation>)```  | Updates an objects based on a dictionary representation of attribute names and values


### Interactive mode (example)

```bash
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  q  quit  show  update
(hbnb)
(hbnb)
(hbnb) quit
$
```

## Tests

Unittests for the this project are defined in the [tests](./tests)
directory. To run the entire test suite simultaneously, execute the following command:

```
$ python3 -m unittest discover tests
```

Alternatively, you can specify a single test file to run at a time:

```
$ python3 -m unittest tests/test_models/test_base_model.py
```

## Authors

* [**Wubeshet Yimam** ](https://github.com/wubeshetA)
* [**Moussa Kalam AMZAT** ](https://github.com/Moussa-Kalam)

## License
Public Domain. No copy write protection. 