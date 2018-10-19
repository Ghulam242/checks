import re

from check50 import *

class Hello(Checks):

    @check()
    def exists(self):
        """hello.py exists."""
        self.require("hello.py")

    @check("compiles")
    def david(self):
        """responds to name Veronica."""
        self.spawn("python hello.py").stdin("Veronica").stdout("hello, Veronica\n")

    @check("compiles")
    def brian(self):
        """responds to name Brian."""
        self.spawn("python hello.py").stdin("Brian").stdout("hello, Brian\n")
