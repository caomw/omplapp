######################################################################
# Rice University Software Distribution License
#
# Copyright (c) 2010, Rice University
# All Rights Reserved.
#
# For a full description see the file named LICENSE.
#
######################################################################

# Author: Mark Moll

from os.path import abspath, dirname
from ompl import dll_loader
from ompl.geometric import *
dll_loader('ompl_app', dirname(abspath(__file__)))
from _app import *