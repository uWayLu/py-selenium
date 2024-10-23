#!/bin/bash
export XDG_CONFIG_HOME=/tmp/.chrome
workdir=$(dirname $(readlink -f $0))
cd $workdir
. ./.venv/bin/activate

echo XDG_CONFIG_HOME=$XDG_CONFIG_HOME
echo PATH=$PATH
type chromium
type chromedriver
