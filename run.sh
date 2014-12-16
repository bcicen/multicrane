#!/bin/bash

[ ! -z $1 ] && {
    $CRANE_COMMAND = $1
}

[ -z $CRANE_COMMAND ] && {
  echo "CRANE_COMMAND not set and no arguments provided, defaulting to 'status'"
  CRANE_COMMAND="status"
}

[ ! -d /cranefiles ] && {
  echo "/cranefiles not found, exiting"
  exit 1
}

[ $(find /cranefiles -maxdepth 1 -iname "*yaml" -or -iname "*yml" | wc -l) == 0 ] && {
  echo "no yaml files found in /cranefiles, exiting"
  exit 1
}

multicrane -c /cranefiles $CRANE_COMMAND
