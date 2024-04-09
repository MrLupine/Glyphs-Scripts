import random

preview_text = []
small_cap = False
styles = ["Cow"] #input the styles you want to display here with the correct case in the order you want them to display
letters = "abcdefghijklmnopqrstuvwxyz"
sample_text = "And now I have a very strange experience to tell you. I had, as you know, cut off my hair in London, and I had placed it in a great coil at the bottom of my trunk. One evening, after the child was in bed, I began to amuse myself by examining the furniture of my room and by rearranging my own little things. There was an old chest of drawers in the room, the two upper ones empty and open, the lower one locked. I had filled the first two with my linen, and as I had still much to pack away I was naturally annoyed at not having the use of the third drawer. It struck me that it might have been fastened by a mere oversight, so I took out my bunch of keys and tried to open it. The very first key fitted to perfection, and I drew the drawer open. There was only one thing in it, but I am sure that you would never guess what it was. It was my coil of hair. I took it up and examined it. It was of the same peculiar tint, and the same thickness."
		#and the letters you want to use here, each list item will display on its own line. 

def small_cap_decider(x):
	rand_int = random.randint(0, 10)
	if x:
		return not x
	elif rand_int > 8:
		return not x

for letter in letters:
	preview_text.append(Font.glyphs[(f"{letter}.sc")].layers[layer])
	
preview_text.append(GSControlLayer(10))
preview_text.append(GSControlLayer(10))
			
for letter in sample_text:
	if letter.isspace():
		small_cap = small_cap_decider(small_cap)
		preview_text.append(Font.glyphs[letter].layers[layer])
		continue
	for layer in styles:
		if small_cap and letter.islower():
			preview_text.append(Font.glyphs[(f"{letter}.sc")].layers[layer])
		else:
			preview_text.append(Font.glyphs[letter].layers[layer])
	
Font.newTab(preview_text)
