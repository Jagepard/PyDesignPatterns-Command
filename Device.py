"""
author  : Jagepard <jagepard@yandex.ru>
license https://mit-license.org/ MIT
"""

class Device:
    def setCommand(self, commandName, command):
        self.commands[commandName] = command

    def execute(self, commandName):
        self.commands[commandName].execute()
