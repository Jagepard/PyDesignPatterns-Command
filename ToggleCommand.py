"""
author  : Jagepard <jagepard@yandex.ru>
license https://mit-license.org/ MIT
"""

from Command import Command
from TurnOnCommand import TurnOnCommand
from TurnOffCommand import TurnOffCommand

class ToggleCommand(Command):
    toggle = 1;
    def execute(self):
        command = TurnOnCommand() if self.toggle % 2 else TurnOffCommand()
        command.execute()
        self.toggle += 1
