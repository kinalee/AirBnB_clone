#!/usr/bin/python3
import sys
from unittest import testcase
from unittest.mock import create_autospec
import console
from io import StringIO
from console import Console


class TestConsole(unittest.TestCase):
    """"""
    def setUp(self):
        """setup method for Console Test Class"""
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create(self, server=None):
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_exit(self):
        """exit command"""
        cli = self.create()
        self.assertTrue(cli.onecmd("quit"))

    def test_EOF(self):
        """exit command"""
        cli = self.create()
        self.assertTrue(cli.onecmd("EOF"))

    def test_help(self):
        """test method for help output"""
        cli = self.create()
        expected = "BaseModel  EOF   Review  User   count  destroy  quit  update\n\n"
        self.assertFalse(cli.onecmd("help"))
        self.assertEqual(expected, self._last_write(2))

    def test_show(self):
        cli = self.create()
        self.assertFalse(cli.onecmd("show"))
        expected = "** instance id missing **\n"
        self.assertEqual(expected, self._last_write(1))

if __name__ == '__main__':
    unittest.main()
