# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Launch_Control/ButtonSysexControl.py
# Compiled at: 2018-04-23 20:27:04
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.SysexValueControl import SysexValueControl

class ButtonSysexControl(SysexValueControl):
    u"""
    A SysexValueControl that behaves like a button so it can be used as a mode button of
    the ModesComponent.
    """

    def set_light(self, value):
        pass

    def is_momentary(self):
        return False
