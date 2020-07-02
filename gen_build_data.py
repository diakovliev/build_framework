#! /usr/bin/env python2

import os
import sys

from metadata import metadata

###############################################################################
class GitInfo:
    def __init__(self, project_dir, metadata_element):
        self.__project_dir  = project_dir
        self.__metadata     = metadata_element

        self.__fill_info()

    def __fill_info(self):
        # TODO: read local repository copy state
        pass


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

        elif isinstance(metadata_element, metadata.GitInfo):
            return GitInfo(os.path.join(self.__project_dir, metadata_element.path_to_local_coy()))

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
        print("** %s- %s" % (key, repr(DataReader(mpath).read(md))))
