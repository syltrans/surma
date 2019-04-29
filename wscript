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
        	script = ['DFLT', 'sylo'],
        	opentype = volt ('source/archive/VOLT/Surma-VOLT.vtp', no_make = (1)),
#        	graphite = gdl ('source/Graphite/Surma-glyphs.gdl',
#                        params = '-e gdlerr.txt',
#            		master = 'source/Graphite/Surma-rules.gdl'),
        	ap = 'source/Surma_anchors.xml',
                pdf = fret(params="-r -oi")
    )
