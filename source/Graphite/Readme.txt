This file describes the process for producing Graphite files for the Surma font.

The source font may be the Surma.ttf file from the temp_ttf folder of the source repository, or a font which already contains OpenType tables. For simplicity, this document assumes Surma.ttf.

In Graide, configure the project as follows:
     Font file: Surma.ttf
     GDL file:  Surma-glyphs.gdl

Surma-glyphs.gdl contains the glyph definitions and glyph classes for the font.

Surma-rules.gdl contains the rules for implementing the smart font behaviour. It is #included at the end of the Surma-glyphs.gdl file. 

stddef.gdh is a definition header file to define standard abbreviations and constants. It is #included at the top of Surma-rules.gdl.

