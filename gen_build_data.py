#! /usr/bin/env python2

import os
import sys

from metadata import metadata

###############################################################################
class DataReader:

    def __init__(self, project_dir):
        self.__project_dir = project_dir

    def read(self, metadata_element):
        if isinstance(metadata_element, metadata.ReadFile):
            with open(os.path.join(self.__project_dir, metadata_element.filename())) as f:
                return f.read()
        elif isinstance(metadata_element, metadata.GetEnv):
            return os.environ.get(metadata_element.env_name())
        else:
            return metadata_element


###############################################################################
mfilename = sys.argv[1]

mlocals = dict()

if not os.path.isfile(mfilename):
    raise Exception("Can't find file: %s" % mfilename)

mpath = os.path.abspath(os.path.join(mfilename, os.pardir))

execfile(mfilename, globals(), mlocals)

print("** mlocals: %s" % repr(mlocals))

m = mlocals['get_metadata']()

print("** metadata: %s" % repr(m))

if 'properties' in m:
    for key, md in m['properties'].items():
        print("** %s: %s" % (key, md))
        print("** %s- %s" % (key, DataReader(mpath).read(md)))
