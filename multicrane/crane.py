#!/usr/bin/env python

import os, yaml, urllib2, logging, termcolor
from sh import crane
from .util import randomcolor

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

    def lift(self):
       p = crane.lift('-c', self.cranefile, 
                   _env=self.env,
                   _out=self._process_out,
                   _bg=True)
       self.pid = p.pid
       log.debug('running %s' % p.cmd)

    def pull(self):
       p = crane.pull('-c', self.cranefile, 
                   _env=self.env,
                   _out=self._process_out,
                   _bg=True)
       self.pid = p.pid
       log.debug('running %s' % p.cmd)

    def run(self):
       p = crane.run('-c', self.cranefile,
                   _env=self.env,
                   _out=self._process_out,
                   _bg=True)
       self.pid = p.pid
       log.debug('running %s' % p.cmd)

    def rm(self):
       p = crane.rm('-c', self.cranefile,
                   _env=self.env,
                   _out=self._process_out,
                   _bg=True)
       self.pid = p.pid
       log.debug('running %s' % p.cmd)

    def kill(self):
       p = crane.kill('-c', self.cranefile,
                   _env=self.env,
                   _out=self._process_out,
                   _bg=True)
       self.pid = p.pid
       log.debug('running %s' % p.cmd)

    def status(self):
       p = crane.status('-c', self.cranefile,
                   _env=self.env,
                   _out=self._process_out,
                   _bg=True)
       self.pid = p.pid
       log.debug('running %s' % p.cmd)

    def _process_out(self,line):
        termcolor.cprint(self.docker_host_short + ": " + line, self.txtcolor)

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
