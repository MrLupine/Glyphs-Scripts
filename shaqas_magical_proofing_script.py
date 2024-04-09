	# case = "All Caps" #can be "Caps to Small Caps" for otf small caps or "Small Caps" for basic small caps.
	#character_colour : changing character style colour is possible with <cColor:{character_color}
	# comp_type = "MAC"
	# font = "Saudi Sans"
	# font_colour = "COLOR\\:CMYK\\:Process\\:0\\,0\\,0\\,1" #numbers refer to CMYK values as floats
	# indesign_version = "19.2"
	# language = "English\\: USA"
	# leading_headers = "21.000000"
	# leading = "16.000000"
	# ligatures = "0" #0 = off 1 = on
	# paragraph_spacing = "5.669291" #in points (2mm)
	# text_alignment = "right"
	# text_size_headers = "16.000000"
	# text_size = "12.000000"
	# otf_cont_alt = "0" #0 = off 1 = on
		# All of this may be useful at some point to make more specific tagged text files but I found it was much easier to do with just para/character styles, see testfiles within "Tagged Text Test" folder for how to use this ^

# values = ['<0x0627>', '<0x0623>', '<0x0625>', '<0x0622>', '<0x0671>', '<0x066E>', '<0x0628>', '<0x067E>', '<0x062A>', '<0x062B>', '<0x0679>', '<0x062C>', '<0x0686>', '<0x062D>', '<0x062E>', '<0x062F>', '<0x0630>', '<0x0688>', '<0x0631>', '<0x0632>', '<0x0691>', '<0x0698>', '<0x0633>', '<0x0634>', '<0x0635>', '<0x0636>', '<0x0637>', '<0x0638>', '<0x0639>', '<0x063A>', '<0x0641>', '<0x06A4>', '<0x06A1>', '<0x066F>', '<0x0642>', '<0x0643>', '<0x06A9>', '<0x06AF>', '<0x06AD>', '<0x0644>', '<0x0645>', '<0x0646>', '<0x06BA>', '<0x0647>', '<0x06C1>', '<0x06C2>', '<0x06BE>', '<0x0629>', '<0x06C3>', '<0x0648>', '<0x0624>', '<0x06C7>', '<0x06CB>', '<0x0649>', '<0x064A>', '<0x0626>', '<0x06CC>', '<0x06D2>', '<0x06D3>', '<0x06D5>']
# marks = ['<0x0615>', '<0x0670>', '<0x0656>', '<0x0654>', '<0x0655>', '<0x064B>', '<0x064C>', '<0x064D>', '<0x064E>', '<0x064F>', '<0x0650>', '<0x0651>', '<0x0652>', '<0x0653>']
values = ['<0x0627>', '<0x0623>', '<0x0628>', '<0x0646>', '<0x06D2>']
marks = ['<0x0615>', '<0x0670>']

def text_generator(x, y, z):
	indesign_string = ""
	for mark in marks:
		for prev_value in x:
			for value in y:
				for next_val in z:
					indesign_string += value + mark + next_val + "	"
	return indesign_string

def file_generator():
	with open("/Users/jpickard/Desktop/indesign_proofing_file.txt", "w") as file:
		file.write(
				f"""<ASCII-MAC>
<Version:19.2><FeatureSet:InDesign-Roman><DefineParaStyle:Title=<Nextstyle:Title>>
<DefineParaStyle:Combinations=<Nextstyle:Combinations>>
<ParaStyle:Title>INITIAL FORMS
<ParaStyle:Combinations>{text_generator(values, values, values)}
<ParaStyle:Title>MEDIAL FORMS
<ParaStyle:Combinations>{text_generator(values, values, values)}
<ParaStyle:Title>FINAL FORMS
<ParaStyle:Combinations>{text_generator(values, values, values)}
<ParaStyle:Title>ISOLATED FORMS
<ParaStyle:Combinations>{text_generator(values, values, values)}"""
			)
		print("File Generated, Wooohooo!")

file_generator()
