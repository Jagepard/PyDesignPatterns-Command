"""
author  : Jagepard <jagepard@yandex.ru>
license https://mit-license.org/ MIT
"""

from Lamp import Lamp
from TurnOnCommand import TurnOnCommand
from TurnOffCommand import TurnOffCommand
from ToggleCommand import ToggleCommand

device = Lamp()

try:
    device.setCommand('on', TurnOnCommand())
    device.setCommand('off', TurnOffCommand())
    device.setCommand('toggle', ToggleCommand())
    device.execute('on')
    device.execute('off')
    device.execute('toggle')
    device.execute('toggle')
except:
    print('An error occured.')
