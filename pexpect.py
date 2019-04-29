#!/usr/bin/python
"""
Script to login to bastion host and login in to gcp machine
Usage Example:
python pexpect1.py -u C12345 -m 10.209.193.15

#Mon host
python pexpect1.py -u C12345 -m 10.209.193.3

-m machine to ssh into
- u username
"""

import pexpect
import logging
import sys
from optparse import OptionParser


logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')

parser = OptionParser()
parser.add_option("-m", "--machine", dest="machine",
                  help="gcp machine to ssh")

parser.add_option("-u", "--user", dest="user",
                  help="user name for machine")


(options, args) = parser.parse_args()


print options, args

print parser.parse_args()

if not options.machine or not options.user:
    print "ERR: Some parameters not passed  "
    print "Usage Example: python pexpect1.py -u C12345 -m 10.209.193.3"
    sys.exit(1)

child = pexpect.spawn('ssh ' +  options.user + '@machine.com')

p = raw_input('Enter machine password:')

# Append
p = init_p + p

def run_expect(command, expect):
    child.sendline (command)
    child.expect (expect)

print "Waiting"
print child.before    # Print the result of the ls command.

# Just press enter, as sometimes it takes long for prompt
child.sendline ("")
child.expect ('Enter PASSCODE:')
print "Found passcode string"
