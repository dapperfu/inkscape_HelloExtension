#!/usr/bin/env python
"""
Created by Jed Frey 2018.

MIT License

Copyright (c) 2018 Jed Frey

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import inkex
import sys
import datetime

fid = open("/tmp/hello.txt", "w")
fid.write("#"*20)
fid.write("\n# ")
fid.write(str(datetime.datetime.now()))
fid.write("\n")
fid.write("#"*20)

fid.write("\nExecutable: \n\t")
fid.write(sys.executable)

fid.write("\nPaths:\n")
for path in sys.path:
    fid.write("\t")
    fid.write(path)
    fid.write("\n")

fid.write("\nArgs:\n")
for arg in sys.argv:
    fid.write("\t")
    fid.write(arg)
    fid.write("\n")

fid.close()

import shutil
shutil.copy2(sys.argv[-1], "/tmp/inkscape.svg")
