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


parser = optparse.OptionParser()
parser.add_option('-c',
                  action="store_true",
                  default=False,
                  dest="copyfile",
                  help="Set Flag to copy file. Default is Move")
parser.add_option('-s',
                  action="store",
                  dest="source",
                  help="Source File or Directory")
parser.add_option('-t',
                  action="store",
                  dest="target",
                  help="Target Directory")
parser.add_option('-l',
                  type="string",
                  action="callback",
                  callback=list_callback,
                  dest="filelist",
                  help="Comma separated list of Base filenames")
parser.add_option('-f',
                  action="store",
                  dest="file_format",
                  help="File Format string where filelist will used")

options, remainder = parser.parse_args()
print 'COPY      :', options.copyfile
print 'SOURCE    :', options.source
print 'TARGET    :', options.target
print 'LIST      :', options.filelist
print 'FORMAT    :', options.file_format
print 'REMAINING :', remainder
source_file_or_dir = options.source
target_dir = options.target

if not os.path.exists(source_file_or_dir):
    print "ERROR: %s is not a valid file or directory" % source_file_or_dir
    sys.exit(1)

if not os.path.isdir(target_dir):
    print "ERROR: %s is not a valid directory" % target_dir
    sys.exit(1)


