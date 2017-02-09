#!/usr/bin/python3
import json
import cmd
import sys
import os.path
from models.base_model import BaseModel

class MyPrompt(cmd.Cmd):
    intro = 'Welcome to hbnb!\n'
    prompt = '(hbtn) '

    def do_create(self, args):
        if not args:
            print('** class name missing **')
        else:
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)

    def do_show(self, args):
        arg_list = list(args.split())
        if len(arg_list) < 1:
            print('** class name missing **')
        elif len(arg_list) < 2:
            print('** instance id missing **')
        elif objects:
            found = None
            for key in objects.keys():
                if key == arg_list[1]:
                    for i in objects[key].split():
                        if i == '[' + arg_list[0] + ']':
                            print(objects[key])
                            break
                        else:
                            print('** class doesn\'t exit **')
                            break
                    found = 1
            if not found:
                print('** no instance found **')
        else:
            print('** no instance found **')

    def do_EOF(self, args):
        """ documented """
        raise SystemExit

    def do_quit(self, args):
        """ documented"""
        raise SystemExit

    def do_emptyline(self, args):
        """ documented """
        pass


if __name__ == '__main__':
    if os.path.isfile('file.json'):
        with open('file.json', 'r') as json_file:
            objects = json.load(json_file)
    else:
        objects = {}
    MyPrompt().cmdloop()
