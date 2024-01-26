# Similar to display-instances but a step further, used to show characters in the text window that use (a) chosen diacritic(s). Will allot each selected diacritic a line containing any character that includes the diacritic

preview_text = []
styles = ["Cow Light", "Cow", "Cow Bold", "Cow Extrabold", "Bull", "Bull Extrabold"]
#input the styles you want to display here (with the correct case) in the order you want them to display

diacritics = ["acute", "breve", "caron", "cedilla", "circumflex", "commaaccent", "commaturnedabove", "dieresis", "dotaccent", "grave", "hookabove", "hungarumlaut", "macron", "ogonek", "ring", "tilde"]
#and the letters you want to use here, each list item will display on its own line. 

glyphs = Font.glyphs

for style in styles:
	style_text = []
	for diacritic in diacritics:
		case_layer = []
		layer = []
		small_caps = []
		for glyph in glyphs:
			if diacritic in glyph.name and "comb" not in glyph.name:
				if glyph.name[0].isupper():
					case_layer.append(glyphs[f"{glyph.name}"].layers[f"{style}"])
				elif ".sc" in glyph.name:
					small_caps.append(glyphs[f"{glyph.name}"].layers[f"{style}"])
				else:
					layer.append(glyphs[f"{glyph.name}"].layers[f"{style}"])
		if f"{diacritic}comb.case" in glyphs:
			case_layer.append(glyphs[f"{diacritic}comb.case"].layers[f"{style}"])
		case_layer.append(GSControlLayer(10))
		layer.append(glyphs[f"{diacritic}comb"].layers[f"{style}"])
		layer.append(GSControlLayer(10))
		if f"{diacritic}comb.sc" in glyphs:
			small_caps.append(glyphs[f"{diacritic}comb.sc"].layers[f"{style}"])
		else:
			small_caps.append(glyphs[f"{diacritic}comb"].layers[f"{style}"])
		small_caps.append(GSControlLayer(10))
		style_text += case_layer + layer + small_caps
	style_text.append(GSControlLayer(10))
	preview_text += style_text
Font.newTab(preview_text)