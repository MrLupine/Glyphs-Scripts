for glyph in Font.glyphs:
	if glyph.script == "arabic":
		for layer in glyph.layers:
			print(layer.name)
			if layer.name == "Combined":
				for colour in range(3, -1, -1):
					new_layer = layer.copy()
					new_layer.attributes["colorPalette"] = colour
					glyph.layers.append(new_layer)