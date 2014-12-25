#!/usr/bin/env python

import os, yaml, urllib2, logging, termcolor
from sh import crane
from util import randomcolor

log = logging.getLogger()

class CraneConfig(object):
    def __init__(self, cranefile):
        """
        CraneConfig object 
        """
        self.txtcolor = randomcolor()
        self.cranefile = cranefile 
        self.docker_host = self._gethost()
        self.docker_host_short = self.docker_host.strip('tcp://').split(':')[0]
        self.env = os.environ.copy() 
        self.env['DOCKER_HOST'] = self.docker_host

    def is_running(self):
        try:
            os.kill(self.pid, 0)
        except OSError:
            return False
        return True

    def __getattr__(self, name):
       p = crane(name, '-c', self.cranefile, 
                 _env=self.env,
                 _out=self._process_out,
                 _err=self._process_out,
                 _out_bufsize=1,
                 _bg=True)
       self.pid = p.pid
       log.info('running %s' % p.cmd)
       log.debug('call args: %s' % p.call_args)

    def _process_out(self,line):
        termcolor.cprint(self.docker_host_short + ": " + line.strip('\n'), 
                self.txtcolor)

    def _gethost(self):
        cf = yaml.load(open(self.cranefile, 'r'))
        #simple validation before returning the docker_host
        if not cf.has_key('docker_host'):
            raise Exception('docker_host section not found in cranefile %s' %
                            self.cranefile)
        r = urllib2.Request(cf['docker_host'].replace('tcp', 'http') + "/version")
        try:
            urllib2.urlopen(r).read()
        except Exception, e:
            log.fatal('unable to reach docker host %s' % 
                    cf['docker_host'])
            raise Exception(e)

        return cf['docker_host']
