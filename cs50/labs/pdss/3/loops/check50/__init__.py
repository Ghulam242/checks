from check50 import *

class Loops(Checks):

    @check()
    def exists(self):
        """loops.py submitted"""
        self.require("loops.py")

    @check("exists")
    def one_question(self):
        """prints one question mark when input is 1"""
        self.spawn("python types.py").stdin("1").stdout("^\?\n", "?")

    @check("exists")
    def four_questions(self):
        """prints four question mark when input is 4"""
        self.spawn("python types.py").stdin("4").stdout("^\?\?\?\?\n", "????")

    @check("exists")
    def eight_questions(self):
        """prints eight question mark when input is 8"""
        self.spawn("python types.py").stdin("8").stdout("^\?\?\?\?\?\?\?\?\n", "????????")
