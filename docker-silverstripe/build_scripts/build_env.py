#!/usr/bin/env python
import os
from subprocess import call

os.chdir('../infra')
call(['docker-compose', 'up', '-d'])