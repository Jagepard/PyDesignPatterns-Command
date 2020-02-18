"""
author  : Jagepard <jagepard@yandex.ru>
license https://mit-license.org/ MIT
"""

class Device:
    def setCommand(self, commandName, command):
        if commandName in self.commands:
            raise Exception("Command already exists")
        self.commands[commandName] = command

    def execute(self, commandName):
        if commandName in self.commands:
            self.commands[commandName].execute()
