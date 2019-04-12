#!/usr/bin/python
# this is a smith configuration file

# set the version control system for srcdist
VCS = 'git'

# set the font name, version, licensing and description
APPNAME="Surma"

DESC_SHORT = "Font for the Sylheti Nagri script"
DESC_LONG = """
The Surma family of fonts supports the Sylheti Nagri script. This is currently
a work-in-progress, so these fonts and related files are preliminary
and incomplete. They should not be used for creating derivatives until
a later release.
"""
DESC_NAME = "Surma"
BUILDLABEL = ""

getufoinfo('source/Surma-Regular.ufo')

fontfamily=APPNAME
designspace('source/' + fontfamily + '.designspace',
                target = "${DS:FILENAME_BASE}.ttf",
                pdf = fret(params="-r -oi")
    )
