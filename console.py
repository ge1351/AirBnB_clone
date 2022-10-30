#!/usr/bin/python3
""" Console module """
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
import re


class HBNBCommand(cmd.Cmd):
    """ HBNB console """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit from the console prompt:
           (hbnb) quit"""
        return True

    def do_EOF(self, line):
        """EOF quit from the console prompt"""
        return True

    def emptyline(self):
        """emptyline from the console prompt"""
        pass

    def do_create(self, line):
        """Creates a new instance, saves it and print its id
           (hbnb) create <typeobject>"""
        list_class = ("BaseModel", "User", "State", "City",
                      "Amenity", "Place", "Review")
        if line in list_class:
            my_instance = globals()[str(line)]()
            print(my_instance.id)
            my_instance.save()
        elif len(line) == 0:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Show a instance:
           (hbnb) show <typeobject> <idobject>"""
        splitted = line.split()
        list_class = ("BaseModel", "User", "State", "City",
                      "Amenity", "Place", "Review")
        if len(splitted) == 2:
            if splitted[0] in list_class:
                try:
                    all_objs = models.storage.all()
                    print(all_objs[splitted[0] + "." + splitted[1]])
                except:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(splitted) == 0:
            print("** class name missing **")
        elif len(splitted) == 1:
            print("** instance id missing **")

    def do_all(self, line):
        """Prints all string representation of all
            instances based or not on the class name.
           (hbnb) all <typeobject>(optional)"""
        list_class = ("BaseModel", "User", "State", "City",
                      "Amenity", "Place", "Review")
        if line in list_class:
            all_objs = models.storage.all()
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                if obj.__class__.__name__ == line:
                    print(obj)
        elif len(line) == 0:
            all_objs = models.storage.all()
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                print(obj)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.
           (hbnb) destroy <typeobject> <idobject>"""

        splitted = line.split()
        list_class = ("BaseModel", "User", "State", "City",
                      "Amenity", "Place", "Review")
        if len(splitted) == 2:
            if splitted[0] in list_class:
                try:
                    all_objs = models.storage.all()
                    del all_objs[splitted[0] + "." + splitted[1]]
                    models.storage.save()
                except:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(splitted) == 0:
            print("** class name missing **")
        elif len(splitted) == 1:
            print("** instance id missing **")

    def do_update(self, line):
        """Updates an instance based on the class name
            and id by adding or updating attribute
           (hbnb) update <typeobject> <idobject> <attr name> <attr value>"""

        splitted = line.split()
        list_class = ("BaseModel", "User", "State", "City",
                      "Amenity", "Place", "Review")
        all_objs = models.storage.all()
        if len(splitted) == 0:
            print("** class name missing **")
        elif splitted[0] not in list_class:
            print("** class doesn't exist **")
        elif len(splitted) == 1:
            print("** instance id missing **")
        elif splitted[0] + "." + splitted[1] not in all_objs.keys():
            print("** no instance found **")
        elif len(splitted) == 2:
            print("** attribute name missing **")
        elif len(splitted) == 3:
            print("** value missing **")
        else:
            if splitted[0] + "." + splitted[1] in all_objs.keys():
                setattr(all_objs[splitted[0] + "." + splitted[1]],
                        splitted[2], splitted[3])
                models.storage.save()
            else:
                print("** no instance found **")

    def default(self, line):
        """ Default for excecute the commands in advanced tasks."""
        tmp = line.split(".")
        all_objs = models.storage.all()
        if tmp[1] == "all()":
            HBNBCommand.do_all(self, tmp[0])
        elif tmp[1] == "count()":
            print(HBNBCommand.count(self, tmp[0]))
        elif re.search("show", tmp[1]):
            arg = "".join(tmp).split('"')
            argument = tmp[0] + " " + arg[1]
            HBNBCommand.do_show(self, argument)
        elif re.search("destroy", tmp[1]):
            arg = "".join(tmp).split('"')
            argument = tmp[0] + " " + arg[1]
            HBNBCommand.do_destroy(self, argument)
        elif re.search("{.+}", tmp[1]):
            arg = tmp[1].split(",")
            obj_id = arg[0].split("\"")[1]

            for i in arg[1:]:
                aux = HBNBCommand.string_format(i)
                aux = [str(element) for element in aux]
                setattr(all_objs[tmp[0] + "." + obj_id], aux[0], aux[1])
        elif re.search("update", tmp[1]):
            arg = "".join(tmp).split('"')
            argument = " ".join([tmp[0], arg[1], arg[3], arg[5]])
            HBNBCommand.do_update(self, argument)

    @staticmethod
    def string_format(string):
        """ Method for format the string in last update"""
        result = string.replace("{", "").replace(")", "").replace("}", "")
        result = result.replace('"', "").replace("'", "").replace(" ", "")
        result = result.split(":")
        return result

    def count(self, line):
        """ Method for count the instances in objects. """
        counter = 0
        all_objs = models.storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            if obj.__class__.__name__ == line:
                    counter += 1
        return counter

if __name__ == '__main__':
    HBNBCommand().cmdloop()
