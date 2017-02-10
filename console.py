#!/usr/bin/python3

from cmd import Cmd
import sys
import json
import uuid


class MyPrompt(Cmd):
    intro = 'Welcome to hbnb!\n'
    prompt = '(hbtn) '

    @classmethod
    def do_create(cls, args):
        """ documented  """
        return json.dumps(cls)

    def do_EOF(self, args):
        """ documented """
        raise SystemExit

    def do_emptyline(self, args):
        """ documented """
        return self.exit()

    def do_quit(self, args):
        """ documented"""
        raise SystemExit

    def do_show(self, args):
        """ documented """
        """ print(str(self.)) """


if __name__ == '__main__':
    MyPrompt().cmdloop()
