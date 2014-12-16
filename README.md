multicrane
==========

Superbly simple multi-host Docker orchestration via Crane.

Multicrane is a wrapper around the popular [Crane](https://github.com/michaelsauter/crane)
Docker orchestration tool that allows for performing lift, kill, rm, status, etc. actions
across several hosts simultaneously.

Getting Started
-----------

In order to use Multicrane, simply add a single Docker host address to your existing cranefiles:
```
docker_host: tcp://1.2.3.4:4243

containers:
    ...
```

And run a multicrane container with a directory of cranefiles mounted within:
```
/path/to/my/cranefiles/node1.yaml
/path/to/my/cranefiles/node2.yaml
/path/to/my/cranefiles/node3.yaml
```

```
docker run --rm=true -ti -v /path/to/my/cranefiles:/cranfiles bcicen/multicrane <command>
```

The given command will be executed for each file/host, exiting when all have completed

Usage
--------

Commands available are analogous to their crane counter parts(defaults to status if not provided):
``` 
  command        Crane command to run (lift,rm,kill,status)
```
