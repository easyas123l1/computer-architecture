#!/usr/bin/env python3

"""Main."""

import sys
import re
from cpu import *
characters = '\r | a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | v | w | x | y | z | # | . | ! | ? | ,'
cpu = CPU()
filename = sys.argv[1]
program = []
with open(filename) as f:
    for line in f:
        line = line.split('#')
        line = ','.join(line).lower()
        line = re.sub(characters, '', line)
        line = line.replace('\r', '').replace('\n', '')
        line = re.sub(characters, '', line)
        if len(line) > 1:
            if line[0] == '1' or line[0] == '0':
                program.append(line[:8])

cpu.load(program)
cpu.run()
