#!/usr/bin/env python
'''
Create on July 29, 2014

Created by: @shireenrao
'''

import optparse
import os
import sys


def list_callback(option, opt, value, parser):
    setattr(parser.values, option.dest, value.split(','))


print 'ARGV      :', sys.argv[1:]

parser = optparse.OptionParser()
parser.add_option('-s', action="store", dest="source")
parser.add_option('-t', action="store", dest="target")
parser.add_option('-l', type='string', action='callback',
                  callback=list_callback, dest='filelist')
parser.add_option('-f', action="store", dest="file_format")
parser.add_option('-d', action="store", dest="effective_date")

options, remainder = parser.parse_args()
print 'SOURCE    :', options.source
print 'TARGET    :', options.target
print 'LIST      :', options.filelist
print 'FORMAT    :', options.file_format
print 'DATE      :', options.effective_date
print 'REMAINING :', remainder
source_dir = options.source
target_dir = options.target

if not os.path.isdir(source_dir):
    print "%s is not a valid directory" % source_dir
    sys.exit(1)

if not os.path.isdir(target_dir):
    print "%s is not a valid directory" % source_dir
    sys.exit(1)


