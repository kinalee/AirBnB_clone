#!/usr/bin/python3

import cmd
import sys


class MyPrompt(cmd.Cmd):
    intro = 'Welcome to hbnb!\n'
    prompt = '(hbtn) '

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
    MyPrompt().cmdloop()
