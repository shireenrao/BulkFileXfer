#!/usr/bin/env python
'''
Create on July 29, 2014

Created by: @shireenrao

Usage: bulkfilexfer.py [options]

Options:
  -h, --help      show this help message and exit
  -c              Set Flag to copy file. Default is Move
  -s SOURCE       Source File or Directory
  -t TARGET       Target Directory
  -l FILELIST     Comma separated list of Base filenames
  -f FILE_FORMAT  File Format string where filelist will used

'''

import optparse
import os
import sys


def list_callback(option, opt, value, parser):
    setattr(parser.values, option.dest, value.split(','))


def processfile(copy_flag, src, dest):
    return_flag = False
    action = 'cp' if copy_flag else 'mv'
    if os.path.isfile(src):
        try:
            a_command = action + ' %s %s' % (src, dest)
            print a_command
            os.system(a_command)
            print 'done'
            return_flag = True
        except OSError as esc:
            print 'ERROR: %s %s %s' % (action, src, dest)
            print 'Error: %s:%s' % (esc.errno, esc.message)
    else:
        print 'File %s not found' % src

    return return_flag


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
source_file_or_dir = options.source
target_dir = options.target
filelist = options.filelist
file_format = options.file_format
copyfile = options.copyfile

if (options.source is None or options.target is None
   or options.filelist is None or options.file_format is None):
    parser.print_help()
    sys.exit(1)

if not os.path.exists(source_file_or_dir):
    print "ERROR: %s is not a valid file or directory" % source_file_or_dir
    sys.exit(1)

if not os.path.isdir(target_dir):
    print "ERROR: %s is not a valid directory" % target_dir
    sys.exit(1)

print 'COPY      :', options.copyfile
print 'SOURCE    :', options.source
print 'TARGET    :', options.target
print 'LIST      :', options.filelist
print 'FORMAT    :', options.file_format
print 'REMAINING :', remainder

if os.path.isdir(source_file_or_dir):
    source_list = [os.path.join(source_file_or_dir, file_format % a_file) for
                   a_file in filelist]

finalresult = True
for source in source_list:
    result = False
    result = processfile(copyfile, source, target_dir)
    finalresult = finalresult and result

if finalresult:
    print 'Success'
    sys.exit(0)
else:
    print 'Failure'
    sys.exit(1)
