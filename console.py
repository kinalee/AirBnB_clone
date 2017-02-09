#!/usr/bin/python3
import json
import cmd
import sys
import os.path
from models.base_model import BaseModel
from models.__init__ import storage

class MyPrompt(cmd.Cmd):
    intro = 'Welcome to hbnb!\n'
    prompt = '(hbtn) '

    def do_create(self, args):
        """ Usage: create ClassName """
        if not args:
            print('** class name missing **')
        else:
            arg_list = list(args.split())
            if arg_list[0] in classes:
                new_model = BaseModel()
                new_model.save()
                print(new_model.id)
            else:
                print('** class doesn\'t exist **')

    def do_show(self, args):
        """ Usage: show ClassName ID """
        arg_list = list(args.split())
        if len(arg_list) < 1:
            print('** class name missing **')
        elif len(arg_list) < 2:
            print('** instance id missing **')
        elif arg_list[0] not in classes:
            print('** class doesn\'t exist **')
        elif storage.all():
            found = None
            for key in storage.all().keys():
                if key == arg_list[1]:
                    print(storage.all()[key])
                    found = 1
            if not found:
                print('** no instance found **')
        else:
            print('** no instance found **')

    def do_all(self, args):
        """ Usage: all [ClassName] """
        for key in storage.all().keys():
            arg_list = ""
            if args:
                arg_list = list(args.split())
                if arg_list[0] not in classes:
                    print('** class doesn\'t exist **')
                    break
            if arg_list:
                if storage.all()[key].__dict__['__class__'] == arg_list[0]:
                    print(storage.all()[key])
            else:
                print(storage.all()[key])

    def do_destroy(self, args):
        """ Usage: destroy ClassName ID """
        arg_list = list(args.split())
        if len(arg_list) < 1:
            print('** class name missing **')
        elif len(arg_list) < 2:
            print('** instance id missing **')
        elif arg_list[0] not in classes:
            print('** class doesn\'t exist **')
        elif storage.all():
            found = None
            for key in storage.all().keys():
                if key == arg_list[1]:
                    del storage.all()[key]
                    storage.save()
                    found = 1
            if not found:
                print('** no instance found **')
        else:
            print('** no instance found **')

    def do_update(self, args):
        """ Usage: update ClassName ID AttributeName AttributeValue """
        arg_list = list(args.split())
        if len(arg_list) < 1:
            print('** class name missing **')
        elif len(arg_list) < 2:
            print('** instance id missing **')
        elif len(arg_list) < 3:
            print('** attribute name missing **')
        elif len(arg_list) < 4:
            print('** value missing **')
        elif arg_list[0] not in classes:
            print('** class doesn\'t exist **')
        elif storage.all():
            found = None
            for key in storage.all().keys():
                if key == arg_list[1]:
                    my_model = storage.all()[key]
                    setattr(my_model, arg_list[2], arg_list[3])
                    my_model.save()
                    found = 1
            if not found:
                print('** no instance found **')
        else:
            print('** no instance found **')


    def do_EOF(self, args):
        """ exit on Ctrl-D and EOF """
        raise SystemExit

    def do_quit(self, args):
        """ exit on quit"""
        raise SystemExit

    def emptyline(self):
        return False

if __name__ == '__main__':
    classes = ['BaseModel']
    MyPrompt().cmdloop()
