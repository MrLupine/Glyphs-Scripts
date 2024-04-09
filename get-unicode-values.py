values = []
for glyph in Font.glyphs:
	if glyph.script == "arabic" and glyph.unicode and glyph.selected:
		values.append(glyph.unicode)
		
print(f"values = {values}")	