growlme
=======

Growlme is a simple command-line tool to execute a command in a subshell and notify growl of success
or failure:

    $ growlme ant clean package

To make growl receive remote notifications, you need to turn on "Allow remote application
registration" in the "Network" tab of growl's preferences panel. Set a password, and put that
password in `~/.growlpass` or pass it via the `-P` parameter. You'll need to go back to General tab,
hit Stop Growl, then start it back up and allow it to accept network connections.

In the simplest case, growlme runs locally on a machine that is running growl, and sends the
notification over a local UDP port. But it can also work over a LAN if the `SSHCLIENT` environment
variable is set, or you pass a hostname explicitly via the `-H` parameter.

By default, the notification's title is "(hostname): (command)" and the message is either
"Succeeded" or "FAILED". You can change any of these on the command line (see `--help`).

Credits
-------

Most of the code is Rui Carmo's "netgrowl", included inline and edited down a bit. You can find the
original [on his web site](http://the.taoofmac.com/space/Projects/netgrowl). Greg added the CLI
wrapper and Robey generalized it into a something that executes other programs.

License
-------

Licensed under the Apache License, Version 2.0 (the "License"); you may not
use this file except in compliance with the License. You may obtain a copy
of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations
under the License.

