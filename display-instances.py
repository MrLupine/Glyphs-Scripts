#script for displaying instances/masters next to one another. Useful when dealing with weight.

preview_text = []
styles = [ "Bold", "Regular", "Light"] #input the styles you want to display here with the correct case in the order you want them to display
cases = ["abcdefghijklm", "nopqrstuvwxyz", "ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"]
		#and the letters you want to use here, each list item will display on its own line. 

for case in cases:
	temp_layer = []		
	for letter in case:
		for layer in styles:
			print(Font.glyphs[letter].layers[layer])
			temp_layer.append(Font.glyphs[letter].layers[layer])
	temp_layer.append(GSControlLayer(10))
	preview_text += temp_layer

print(preview_text)