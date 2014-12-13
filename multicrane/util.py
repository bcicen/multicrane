#!/usr/bin/env python

import logging,random
from time import sleep

log = logging.getLogger()

def randomcolor():
    colors=["red", "green", "yellow", "blue", "magenta", "cyan"]
    return colors[random.randint(0,len(colors)-1)]

def check_running(cranes):
    """
    Takes a list of CraneConfig objects, returns when none have active
    processes
    """
    status = []
    for c in cranes:
        status.append(c.is_running())
    if True in status:
        log.debug('%d processes active' % status.count(True))
        sleep(2)
        check_running(cranes)
    return 'Done!'
