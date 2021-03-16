#!/usr/bin/python3
# this is a smith configuration file

APPNAME="Surma"

DESC_SHORT = "Font for the Sylheti Nagri script"

getufoinfo('source/Surma-Regular.ufo')

fontfamily=APPNAME

designspace('source/' + fontfamily + '.designspace',
            target = "${DS:FILENAME_BASE}.ttf",
        	script = ['DFLT', 'sylo'],
     		opentype = fea('source/fea/Surma.fea', no_make = True),
        	graphite = gdl ('generated/Surma-glyphs.gdl', master = 'source/Graphite/Surma-master.gdl', 
                        params = '-e gdlerr.txt'),
	       	ap = 'source/Surma_anchors.xml',
         	pdf = fret(params="-r -oi"),
			woff = woff()
	    )
