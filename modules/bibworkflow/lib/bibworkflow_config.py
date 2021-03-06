## This file is part of Invenio.
## Copyright (C) 2012, 2013 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Invenio BibWorkflow config."""

import os
import logging
from invenio.config import CFG_LOGDIR

CFG_BIBWORKFLOW_WORKFLOWS_LOGDIR = os.path.join(CFG_LOGDIR, 'bibworkflow', 'workflows')
CFG_BIBWORKFLOW_WORKERS_LOGDIR = os.path.join(CFG_LOGDIR, 'bibworkflow', 'workers')
CFG_BIBWORKFLOW_OBJECTS_LOGDIR = os.path.join(CFG_LOGDIR, 'bibworkflow', 'objects')

if not os.path.exists(CFG_BIBWORKFLOW_WORKFLOWS_LOGDIR):
    os.makedirs(CFG_BIBWORKFLOW_WORKFLOWS_LOGDIR)
if not os.path.exists(CFG_BIBWORKFLOW_WORKERS_LOGDIR):
    os.makedirs(CFG_BIBWORKFLOW_WORKERS_LOGDIR)
if not os.path.exists(CFG_BIBWORKFLOW_OBJECTS_LOGDIR):
    os.makedirs(CFG_BIBWORKFLOW_OBJECTS_LOGDIR)

def add_log(path, logger):
    logger = logging.getLogger(logger)
    handler = logging.FileHandler(path)
    formatter = logging.Formatter(logging.BASIC_FORMAT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
    
def enum(**enums):
    return type('Enum', (), enums)

CFG_WORKFLOW_STATUS = enum(NEW=0, RUNNING=1, HALTED=2, ERROR=3, FINISHED=4)
CFG_OBJECT_VERSION = enum(INITIAL=0, FINAL=1, HALTED=2)
CFG_OBJECT_STATUS = enum(
                        ERROR="ERROR - Something went wrong!", 
                        RUNNING="RUNNING - Workflow in process",
                        FINISHED="FINISHED - Workflow was finished for this object"
                        )
