# AirBnB Clone
This repository contains the code for a basic version of the AirBnB clone. The main component is a command-line interpreter that allows users to manage different objects related to the platform. The system is designed to handle various entities that are essential for a platform like AirBnB, such as:
+ `BaseModel`: The base class for all other classes, containing common attributes and methods.
+ `FileStorage`: Handles the storage of all instances in a JSON format file.
+ `User`: Represents a user on the platform with attributes like `username`, `password`, and `email`.
+ `State`: Represents a state or region.
+ `City`: Represents a city within a state.
+ `Place`: Represents an accommodation or listing on the platform.
+ `Amenity`: Represents amenities or facilities available at a place.
+ `Review`: Represents a review given by a user for a place.
## How to Start
+ clone the repository and navigate to the repository directory.
+ Start the command-line interpreter:
```
./console.py
```
## How to Use
Once the command-line interpreter is started, you'll be presented with a prompt `(hbnb)`. Here are some of the commands you can use:
+ `create <class_name>`: Creates an instance of the specified class and stores it in a file in JSON format.
+ `show <class_name> <instance_id>`: Displays the string representation of an instance based on the class name and id.
+ `destroy <class_name> <instance_id>`: Deletes an instance based on the class name and id.
+ `all <class_name>`: Displays the string representation of all instances of the specified class. If no class is specified, it displays all instances.
+ `update <class_name> <instance_id> <attribute_name> <value>`: Updates the attributes of a given instance of a class.
## Examples
1. Create a `User`:
```
(hbnb) create User
```
2. Display `User` information:
```
(hbnb) show User <user_id>
```
3. Update the name attribute of a `User`:
```
(hbnb) update User <user_id> name "foo bar"
```



