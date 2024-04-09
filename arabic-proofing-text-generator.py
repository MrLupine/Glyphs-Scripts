def arabic_proofing_text_generator():
	preview_text = []
	
	styles = ["Cow"]
	
	arabic = ["hamza-ar","alef-ar","alef-ar.fina","alefHamzaabove-ar","alefHamzaabove-ar.fina","alefHamzabelow-ar","alefHamzabelow-ar.fina","alefMadda-ar","alefMadda-ar.fina","alefWasla-ar","alefWasla-ar.fina","beh-ar","beh-ar.fina","beh-ar.medi","beh-ar.init","teh-ar","teh-ar.fina","teh-ar.medi","teh-ar.init","theh-ar","theh-ar.fina","theh-ar.medi","theh-ar.init","jeem-ar","jeem-ar.fina","jeem-ar.medi","jeem-ar.init","hah-ar","hah-ar.fina","hah-ar.medi","hah-ar.init","khah-ar","khah-ar.fina","khah-ar.medi","khah-ar.init","dal-ar","dal-ar.fina","thal-ar","thal-ar.fina","reh-ar","reh-ar.fina","zain-ar","zain-ar.fina","seen-ar","seen-ar.fina","seen-ar.medi","seen-ar.init","sheen-ar","sheen-ar.fina","sheen-ar.medi","sheen-ar.init","sad-ar","sad-ar.fina","sad-ar.medi","sad-ar.init","dad-ar","dad-ar.fina","dad-ar.medi","dad-ar.init","tah-ar","tah-ar.fina","tah-ar.medi","tah-ar.init","zah-ar","zah-ar.fina","zah-ar.medi","zah-ar.init","ain-ar","ain-ar.fina","ain-ar.medi","ain-ar.init","ghain-ar","ghain-ar.fina","ghain-ar.medi","ghain-ar.init","feh-ar","feh-ar.fina","feh-ar.medi","feh-ar.init","veh-ar","veh-ar.fina","veh-ar.medi","veh-ar.init","qaf-ar","qaf-ar.fina","qaf-ar.medi","qaf-ar.init","kaf-ar","kaf-ar.fina","kaf-ar.medi","kaf-ar.init","lam-ar","lam-ar.fina","lam-ar.medi","lam-ar.init","meem-ar","meem-ar.fina","meem-ar.medi","meem-ar.init","noon-ar","noon-ar.fina","noon-ar.medi","noon-ar.init","heh-ar","heh-ar.fina","heh-ar.medi","heh-ar.init","tehMarbuta-ar","tehMarbuta-ar.fina","waw-ar","waw-ar.fina","wawHamzaabove-ar","wawHamzaabove-ar.fina","alefMaksura-ar","alefMaksura-ar.fina","yeh-ar","yeh-ar.fina","yeh-ar.medi","yeh-ar.init","yehHamzaabove-ar","yehHamzaabove-ar.fina","yehHamzaabove-ar.medi","yehHamzaabove-ar.init","kashida-ar","lam_alef-ar","lam_alef-ar.fina","lam_alefHamzaabove-ar","lam_alefHamzaabove-ar.fina","lam_alefHamzabelow-ar","lam_alefHamzabelow-ar.fina","lam_alefMadda-ar","lam_alefMadda-ar.fina","lam_alefWasla-ar","lam_alefWasla-ar.fina"]
	
	arabic_marks = ["wasla-ar","alefabove-ar","alefbelow-ar","hamzaabove-ar","hamzabelow-ar","hamzaaboveDamma-ar","hamzaaboveDammatan-ar","hamzaaboveFatha-ar","hamzaaboveFathatan-ar","hamzaaboveSukun-ar","hamzabelowKasra-ar","hamzabelowKasratan-ar","fathatan-ar","dammatan-ar","kasratan-ar","fatha-ar","damma-ar","kasra-ar","shadda-ar","shaddaFathatan-ar","shaddaDammatan-ar","shaddaKasratan-ar","shaddaFatha-ar","shaddaDamma-ar","shaddaKasra-ar","shaddaAlefabove-ar","sukun-ar","madda-ar"]

	glyphs = Font.glyphs
	for style in styles:
		for mark in arabic_marks:
			for ara_char in arabic:
				for foll_ara_char in arabic:
					preview_text.append(glyphs[ara_char].layers[style])
					preview_text.append(glyphs[mark].layers[style])
					preview_text.append(glyphs[foll_ara_char].layers[style])
		preview_text.append(GSControlLayer(10))
		print(preview_text)
	return preview_text
		
arabic_proofing_text_generator()