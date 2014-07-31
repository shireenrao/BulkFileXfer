BulkFileXfer
============

A utility to transfer files from one location to another based on command line
arguments.

Usage: bulkfilexfer.py [options]

Options:
  -h, --help      show this help message and exit
  -c              Set Flag to copy file. Default is Move
  -s SOURCE       Source File or Directory
  -t TARGET       Target Directory
  -l FILELIST     Comma separated list of Base filenames
  -f FILE_FORMAT  File Format string where filelist will used

Example:

% python bulkfilexfer.py -c -s /some/directory/locationA/dirA \
-t /some/directory/locationB/dirB \
-l abc,def,ghi,jkl,mno -f %s_20140730.csv

The above command copies the following files from source
/some/directory/locationA/dirA/abc_20140730.csv,
/some/directory/locationA/dirA/def_20140730.csv,
/some/directory/locationA/dirA/ghi_20140730.csv,
/some/directory/locationA/dirA/jkl_20140730.csv,
/some/directory/locationA/dirA/mno_20140730.csv,

to target /some/directory/locationB/dirB

'-c' Sets copy mode. If ignored, it will default to move

'-s /some/directory/locationA/dirA' Sets the source to given directory. The
script will look for files in given directory to either move or copy to target.

'-t /some/directory/locationB/dirB' Sets the target to given directory. This is
the target to where files will be copied or moved.

'-l abc,def,ghi,jkl,mno' creates a list of names which are unique from the list
of files you are interested in.

'-f %s_20140730.csv' Sets the format of the file. The propgram will replace %s
with values from the list provided by -l flag to construct the actual file name
to be copied or moved.
