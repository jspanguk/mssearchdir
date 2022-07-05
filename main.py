### This is a python app module for seaching files in all directories of a local ###

import os
fname = input("type file name that you are searching and press enter: ")
for (path, dir, files) in os.walk("c:/"):
    for filename in files:
        fn = os.path.splitext(filename)[0]
        # print()
        # input()
        if  fn == fname:
            print("%s/%s" % (path, filename))
      