from check50 import *


class Speller(Checks):

    @check()
    def exists(self):
        """dictionary.c and dictionary.h exist"""
        self.require("dictionary.c", "dictionary.h")

    @check("exists")
    def compiles(self):
        """speller compiles"""
        self.add("speller.c", "Makefile")
        self.spawn("make").exit(0)

    @check("compiles")
    def basic(self):
        """handles most basic words properly"""
        self.add("basic")
        self.spawn("./speller basic/dict basic/text").stdout(File("basic/out")).exit(0)

    @check("compiles")
    def min_length(self):
        """handles min length (1-char) words"""
        self.add("min_length")
        self.spawn("./speller min_length/dict min_length/text").stdout(File("min_length/out")).exit(0)

    @check("compiles")
    def max_length(self):
        """handles max length (45-char) words"""
        self.add("max_length")
        self.spawn("./speller max_length/dict max_length/text").stdout(File("max_length/out")).exit(0)

    @check("compiles")
    def apostrophe(self):
        """handles words with apostrophes properly"""
        self.add("apostrophe")
        self.spawn("./speller apostrophe/without/dict apostrophe/with/text").stdout(File("apostrophe/outs/without-with")).exit(0)
        self.spawn("./speller apostrophe/with/dict apostrophe/without/text").stdout(File("apostrophe/outs/with-without")).exit(0)
        self.spawn("./speller apostrophe/with/dict apostrophe/with/text").stdout(File("apostrophe/outs/with-with")).exit(0)

    @check("compiles")
    def case(self):
        """spell-checking is case-insensitive"""
        self.add("case")
        self.spawn("./speller case/dict case/text").stdout(File("case/out")).exit(0)

    @check("compiles")
    def substring(self):
        """handles substrings properly"""
        self.add("substring")
        self.spawn("./speller substring/dict substring/text").stdout(File("substring/out")).exit(0)

    @check("substring")
    @valgrind
    def memory(self):
        """program is free of memory errors"""
        self.spawn("./speller substring/dict substring/text").stdout(File("substring/out")).exit(0)
