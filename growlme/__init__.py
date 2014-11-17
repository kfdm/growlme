#!/usr/bin/env python
#
# usage:
#   growlme <command>
#
# Runs <command> in a subshell, and notifies growl of success or failure
# error codes on completion. The success/failure messages can be customized
# on the command line. The growl remote password can be supplied on the
# command line or provided in a '~/.growlpass' file.
#
# The first (largest) section of this code is Rui Carmo's netgrowl.py:
#   http://the.taoofmac.com/space/Projects/netgrowl
#
# Copyright 2004 Rui Carmo <http://the.taoofmac.com>
# Copyright 2010 Greg Brown <geb@pobox.com>
# Copyright 2010 Robey Pointer <robeypointer@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy
# of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import os
import optparse
import subprocess
import time
from gntp.config import mini

ICON_OK = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ok.png')
ICON_FAIL = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fail.png')


def format_time(seconds):
    """Simple text formating of time"""
    if seconds < 60:
        return '%ds' % seconds
    if seconds > 60 and seconds < 3600:
        minutes = seconds / 60
        seconds = seconds % 60
        return '%dm %02ds' % (minutes, seconds)
    if seconds > 3600:
        hours = seconds / 3600
        minutes = (seconds % 3600) / 60
        return '%dh %02dm' % (hours, minutes)


def main():
    host = os.environ.get('SSH_CONNECTION')
    hostname = host.split()[0] if host else 'localhost'

    parser = optparse.OptionParser(usage='usage: %prog [options] <command...>')
    parser.disable_interspersed_args()
    parser.add_option("-H", "--host", dest='host', default=hostname)
    parser.add_option("-P", "--password", dest='password', default=None)
    parser.add_option(
        "-m", "--message", dest='success_text', metavar='TEXT',
        default="Succeeded\nDuration {time}",
        help='message to display on success',)
    parser.add_option(
        "--fail", dest='fail_text', metavar='TEXT',
        default="FAILED\nDuration {time}",
        help='message to display on failure')
    parser.add_option("-t", "--title", dest='title', help='growl title')
    parser.add_option("-s", "--sticky", dest='sticky', action='store_true')

    (opts, args) = parser.parse_args()
    if not args:
        parser.error("must provide a command to execute")

    if opts.title is None:
        opts.title = ' '.join(args)[:30]

    start = time.time()
    try:
        proc = subprocess.Popen(args)
        proc.wait()
    except KeyboardInterrupt:
        proc.terminate()
        proc.wait()
    finally:
        result = proc.returncode
        stop = time.time()

    if result == 0:
        message = opts.success_text
        icon = file(ICON_OK).read()
    else:
        message = opts.fail_text
        icon = file(ICON_FAIL).read()

    message = message.replace('{time}', format_time(stop - start))

    mini(
        message,
        applicationName='growlme',
        title=opts.title,
        hostname=opts.host,
        password=opts.password,
        applicationIcon=icon,
        sticky=opts.sticky,
    )

    return result

if __name__ == '__main__':
    exit(main())
