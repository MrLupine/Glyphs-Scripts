# Spaces components out equally based on the position of the component in it's original glyph.
# Orientation of component matters! If they have been rotated this can do weird things.

def spacer():
	holes = []
	for count, component in enumerate(Layer.components):
		if Layer.components[count].selected:
			holes.append(Layer.components[count])
	holes.sort(key=lambda a:a.position.x + a.position.y	)
	move_distance_x = (holes[-1].position.x - holes[0].position.x) / (len(holes) - 1)
	move_distance_y = (holes[-1].position.y - holes[0].position.y) / (len(holes) - 1)
	base = [holes[0].position.x, holes[0].position.y]
	for value in range(1, len(holes)-1):
		holes[value].transform = ((
			0,
			0,
			0,
			0,
			int(base[0] + (value * move_distance_x)),
			int(base[1] + (value * move_distance_y))
		))

spacer()