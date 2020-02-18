"""
author  : Jagepard <jagepard@yandex.ru>
license https://mit-license.org/ MIT
"""

from Command import Command

class TurnOnCommand(Command):
    def execute(self):
        print('The Light turns on\n')
