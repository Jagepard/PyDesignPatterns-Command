"""
author  : Jagepard <jagepard@yandex.ru>
license https://mit-license.org/ MIT
"""

from Command import Command

class TurnOffCommand(Command):
    def execute(self):
        print('The Light turns off\n')
