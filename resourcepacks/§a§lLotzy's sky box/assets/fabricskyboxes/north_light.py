import os
import json
import random

# assign directory
directory = 'sky'
pattern = {
		"blend": {
			"type": "screen"
		},
		"conditions": {
			"weather": [
				"clear"
			],
			"worlds": [
				"minecraft:overworld"
			]
		},
		"decorations": {
			"showMoon": True,
			"showStars": False,
			"showSun": True
		},
		"properties": {
			"fade": {
				"endFadeIn": 0,
				"endFadeOut": 0,
				"startFadeIn": 24000,
				"startFadeOut": 24000
			},
			"rotation": {
				"axis": [
					0.0,
					0.0,
					0.0
				],
				"rotationSpeed": 1.0,
				"static": [
					0.0,
					90.0,
					30.0
				]
			},
			"shouldRotate": False
		},
		"schemaVersion": 2,
		"textures": {
			"bottom": "fabricskyboxes:sky/black.png",
			"east": "fabricskyboxes:sky/black.png",
			"north": "fabricskyboxes:sky/black.png",
			"south": "fabricskyboxes:sky/black.png",
			"top": "",
			"west": "fabricskyboxes:sky/black.png"
		},
		"type": "square-textured"
	}

colors = ['north_light1.png','north_light2.png','north_light3.png','north_light4.png','north_light5.png','north_light6.png']
amount_colors = len(colors)
for i in range(3):
	
	duration = random.randint(1000,2500)
	start = random.randint(13000,22000-duration)
	j = 0
	c = 0
	while (duration > 0):
		if c >= amount_colors:
			c = 0
		pattern['textures']['top'] = 'fabricskyboxes:sky/'+colors[c]
		pattern['properties']['rotation']['static'][2] = float(random.randint(-30,30))
		pause = random.randint(20,60)
		delay = random.randint(100,400)
		
		startFadeIn = start
		fade = delay/6
		endFadeIn = startFadeIn+fade
		endFadeOut = startFadeIn+delay
		startFadeOut = endFadeOut-fade
		pattern['properties']['fade']['startFadeIn'] = int(startFadeIn)
		pattern['properties']['fade']['endFadeIn'] = int(endFadeIn)
		pattern['properties']['fade']['startFadeOut'] = int(startFadeOut)
		pattern['properties']['fade']['endFadeOut'] = int(endFadeOut)
		start+=pause
		duration-=delay-pause
		with open(os.path.join(directory, 'north_light_'+str(i)+'_'+str(j)+'.json'), 'w') as outfile:
			json.dump(pattern, outfile,indent='\t')
		c+=1
		j+=1

