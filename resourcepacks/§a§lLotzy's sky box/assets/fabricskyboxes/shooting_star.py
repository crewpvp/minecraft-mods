import os
import json
import random
vectors = [
	{ 
		"axis": [
			0.0,
			0.0,
			90.0
		],
		"static": [
			0.0,
			90.0,
			90.0
		]
	},
	{ 
		"axis": [
			0.0,
			0.0,
			-90.0
		],
		"static": [
			0.0,
			-90.0,
			90.0
		]
	},
	{ 
		"axis": [
			-90.0,
			0.0,
			0.0
		],
		"static": [
			0.0,
			0.0,
			0.0
		]
	},
	{ 
		"axis": [
			90.0,
			0.0,
			0.0
		],
		"static": [
			180.0,
			0.0,
			0.0
		]
	},
	{
		"axis": [
			90.0,
			0.0,
			45.0
		],
		"static": [
			90.0,
			45.0,
			0.0
		]
	},
	{
		"axis": [
			-90.0,
			0.0,
			45.0
		],
		"static": [
			-90.0,
			45.0,
			0.0
		]
	},
	{
		"axis": [
			-90.0,
			0.0,
			-45.0
		],
		"static": [
			90.0,
			-45.0,
			0.0
		]
	},
	{
		"axis": [
			90.0,
			0.0,
			-45.0
		],
		"static": [
			-90.0,
			-45.0,
			0.0
		]
	}
]

# assign directory
directory = 'sky'
pattern = {
		"blend": {
			"type": "add"
		},
		"conditions": {
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
				"startFadeIn": 0,
				"endFadeIn": 0,
				"startFadeOut": 24000,
				"endFadeOut": 24000
			},
			"rotation": {
				"axis": [
					90.0,
					0.0,
					-45.0
				],
				"rotationSpeed": 250,
				"static": [
					-90.0,
					-45.0,
					0.0
				]
			},
			"shouldRotate": True
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

colors = ['shootingstar_magnesium.png','shootingstar_calcium.png','shootingstar_nitrogen.png','shootingstar_iron.png','shootingstar_sodium.png','shootingstar_uranium.png']
for i in range(100):
	pattern['textures']['top'] = 'fabricskyboxes:sky/'+random.choice(colors)
	speed = random.randint(150,280)
	pattern['properties']['rotation']['rotationSpeed'] = speed
	cycles = 24000/speed
	startFadeIn = 10000
	while startFadeIn < 13000 or startFadeIn > 22000:
		start_cycle = random.randint(1,int(cycles))
		startFadeIn = (start_cycle*speed)-(speed/8)
	fade = cycles/12
	endFadeIn = startFadeIn+fade
	endFadeOut = startFadeIn+cycles
	startFadeOut = endFadeOut-fade
	pattern['properties']['fade']['startFadeIn'] = int(startFadeIn)
	pattern['properties']['fade']['endFadeIn'] = int(endFadeIn)
	pattern['properties']['fade']['startFadeOut'] = int(startFadeOut)
	pattern['properties']['fade']['endFadeOut'] = int(endFadeOut)

	vals = random.choice(vectors)
	pattern['properties']['rotation']['axis'] = vals['axis']
	pattern['properties']['rotation']['static'] = vals['static']
	with open(os.path.join(directory, 'shootingstar_'+str(i)+'.json'), 'w') as outfile:
		json.dump(pattern, outfile,indent='\t')

