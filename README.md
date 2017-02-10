# Holberton BnB

Holberton BnB, aka HBnB, is a clone of the AirBnB website. It gives the ability to create different locations, users, and reviews for the locations. Currently it only runs as a console. It can desplay all of the instances of all created objects, or display only the instances of a specific type of object (user, review, location, etc.). The user can also delete any of these created objects.

## Usage
Run the HBnB console.py file in your terminal:
```
$ ./console.py
```
The console has a series of available commands:
- <b>create</b>: Creates a new instance of given class. Prints the id of the new instance. Usage: create <class name>
```python3
(hbnb) create User
ec6c5aa4-ebd3-11e6-864c-08002745538c
```
- <b>all</b>: Displays all instances that currently exist. Optional class name will display all instances of a given class. Usage: all [<class name>].
```
(hbnb) all User
[User] (ec6c5aa4-ebd3-11e6-864c-08002745538c) {'id': 'ec6c5aa4-ebd3-11e6-864c-080027
45538c', 'email': 'airbnb@holbertonshool.com', '__class__': 'User', 'last_name': 'Ho
lberton', 'created_at': datetime.datetime(2017, 1, 15, 18, 50, 11, 853163), 'first_n
ame': 'Betty', 'updated_at': datetime.datetime(2017, 1, 15, 18, 50, 11, 853222), 'pa
ssword': 'root'}
```
- <b>show</b>: Displays an instance based on given class name and id. Usage: show <class name> <id>
```
(hbnb) show User ec6c5aa4-ebd3-11e6-864c-08002745538c
[User] (ec6c5aa4-ebd3-11e6-864c-08002745538c) {'id': 'ec6c5aa4-ebd3-11e6-864c-080027
45538c', 'email': 'airbnb@holbertonshool.com', '__class__': 'User', 'last_name':'Hol
berton', 'created_at': datetime.datetime(2017, 1, 15, 18, 50, 11, 853163), 'first_na
me': 'Betty', 'updated_at': datetime.datetime(2017, 1, 15, 18, 50, 11, 853222), 'pas
sword': 'root'}
```
- <b>destroy</b>: Destroys an instance based on given class name and id. Usage: destroy <class name> <id>
```
(hbnb) destroy User ec6c5aa4-ebd3-11e6-864c-08002745538c
(hbnb) show User ec6c5aa4-ebd3-11e6-864c-08002745538c
```
- <b>update</b>: Updates an instance based on class name and id by adding or updating the attribute given with the given value. Usage: update <class name> <id> <attribute name> <attribute value>
```
(hbnb) create User
edaab9ce-ebd3-11e6-a4af-08002745538c
(hbnb) show User edaab9ce-ebd3-11e6-a4af-08002745538c
[User] (edaab9ce-ebd3-11e6-a4af-08002745538c) {'id': 'edaab9ce-ebd3-11e6-a4af-080027
45538c', 'email': 'airbnb@holbertonshool.com', 'last_name': 'Holberton', 'created_at
': datetime.datetime(2017, 1, 15, 18, 50, 13, 939549), 'first_name': 'Betty', 'passw
ord': 'root', 'updated_at': datetime.datetime(2017, 1, 15, 18, 50, 13, 939585)}
(hbnb) update User edaab9ce-ebd3-11e6-a4af-08002745538c first_name Johnny
(hbnb) show User edaab9ce-ebd3-11e6-a4af-08002745538c
[User] (edaab9ce-ebd3-11e6-a4af-08002745538c) {'id': 'edaab9ce-ebd3-11e6-a4af-080027
45538c', 'email': 'airbnb@holbertonshool.com', 'last_name': 'Holberton', 'created_at
': datetime.datetime(2017, 1, 15, 18, 50, 13, 939549), 'first_name': 'Johnny', 'pass
word': 'root', 'updated_at': datetime.datetime(2017, 1, 15, 18, 50, 13, 939585)}
```

## Files & Directories
- <b>console.py</b>: The main HBnB code, runs the console
- <b>models/</b>: The models directory, holds all classes used in HBnB
### Directory: models/
This directory contains all classes used in the HBnB project.
- <b>__init__.py</b>: Initiates the modles package
- <b>amenity.py</b>: The Amenity class, inherits from BaseModel class
- <b>base_model.py</b<>: The BaseModel class, the super class for all other classes in models/. Contains methods for loading and save as JSON representation, as well as unique ids to keep track of different instances of classes.
- <b>city.py</b>: The City class, inherits from BaseModel class
- <b>place.py</b>: The Place class, inherits from BaseModel class
- <b>review.py</b>: The Review class, inherits from BaseModel class
- <b>state.py</b>: The State class, inherits from BaseModel class
- <b>user.py</b>: The User class, inheirts from BaseModel class
- <b>engine</b>: The engine directory, holds the files for loading/saving objects as JSON representations
### Directory: models/engine/
- <b>file_storage.py</b>: The FileStorage class, used to load/save classes based on BaseModel. Files are loaded/saved from a .json file as JSON representations of the class.