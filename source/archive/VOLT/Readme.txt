This file describes the process for building OpenType tables for the Surma font using VOLT.

The process makes use of two perl scripts, voltImportAnchors.pl and voltFixup.pl. These are included in the font-ttf-scripts package (https://github.com/silnrsi/font-ttf-scripts) and can be found in the Examples folder (https://github.com/silnrsi/font-ttf-scripts/tree/master/Examples). Those utilities require installation of the font-ttf package (https://github.com/silnrsi/font-ttf).

Instructions on installing and using these packages can be found at: http://scripts.sil.org/FontUtils

To produce OpenType tables for the Surma font:

1. Open the source file /temp_ttf/Surma.ttf in VOLT and add the <sylo> script, with <dflt> language. (This makes it a VOLT project, needed for Step 2). Save the file as Surma-VOLT.ttf.

2. Import the anchors from the attachment point database using the voltImportAnchors perl script:
voltImportAnchors.pl Surma-VOLT.ttf Surma_anchors.xml Surma-VOLT-AP.ttf.

3. Open Surma-VOLT-AP.ttf in VOLT and import the VOLT project Surma-VOLT.vtp. Save the font.

4. Because VOLT may have rearranged the font's glyph palette, we need to run the voltFixup utility to make sure that the lookups still produce the correct substitutions.
voltFixup.pl Surma-VOLT-AP.ttf Surma-VOLT.vtp Surma-VOLT-AP-fixed.ttf Surma-VOLT-fixed.vtp

5. Open the output of voltFixup in VOLT and make desired changes to glyph groups, lookups or features.

6. Ship the font.
