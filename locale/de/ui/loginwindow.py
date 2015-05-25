import uiScriptLocale

LOCALE_PATH = uiScriptLocale.LOGIN_PATH
SERVER_BOARD_HEIGHT = 220 + 180
SERVER_LIST_HEIGHT = 171 + 180

window = {
	"name" : "LoginWindow",
	"sytle" : ("movable",),

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(
		## Board
		{
			"name" : "bg1", "type" : "expanded_image", "x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 800.0, "y_scale" : float(SCREEN_HEIGHT) / 768.0,
			"image" : "locale/de/ui/serverlist.sub",
		},
		{
			"name" : "bg2", "type" : "expanded_image", "x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 600.0, "y_scale" : float(SCREEN_HEIGHT) / 768.0,
			"image" : "locale/de/ui/login.sub",
		},

		## VirtualKeyboard
		{
			'name' : 'VirtualKeyboard',
			'type' : 'thinboard',
			'x' : (SCREEN_WIDTH - 9999) / 2,
			'y' : SCREEN_HEIGHT - 9999,
			'width' : 564,
			'height' : 254,
			'children' : 
			(
				{
					'name' : 'key_at',
					'type' : 'toggle_button',
					'x' : 40,
					'y' : 186,
				},
				{
					'name' : 'key_backspace',
					'type' : 'button',
					'x' : 498,
					'y' : 186,
				},
				{
					'name' : 'key_enter',
					'type' : 'button',
					'x' : 439,
					'y' : 186,
				},
				{
					'name' : 'key_shift',
					'type' : 'toggle_button',
					'x' : 86,
					'y' : 186,
				},
				{
					'name' : 'key_space',
					'type' : 'button',
					'x' : 145,
					'y' : 186,
				},
				{
					'name' : 'key_1',
					'type' : 'button',
					'x' : 40,
					'y' : 24,
				},
				{
					'name' : 'key_2',
					'type' : 'button',
					'x' : 80,
					'y' : 24,
				},
				{
					'name' : 'key_3',
					'type' : 'button',
					'x' : 120,
					'y' : 24,
				},
				{
					'name' : 'key_4',
					'type' : 'button',
					'x' : 160,
					'y' : 24,
				},
				{
					'name' : 'key_5',
					'type' : 'button',
					'x' : 200,
					'y' : 24,
				},
				{
					'name' : 'key_6',
					'type' : 'button',
					'x' : 240,
					'y' : 24,
				},
				{
					'name' : 'key_7',
					'type' : 'button',
					'x' : 280,
					'y' : 24,
				},
				{
					'name' : 'key_8',
					'type' : 'button',
					'x' : 320,
					'y' : 24,
				},
				{
					'name' : 'key_9',
					'type' : 'button',
					'x' : 360,
					'y' : 24,
				},
				{
					'name' : 'key_10',
					'type' : 'button',
					'x' : 400,
					'y' : 24,
				},
				{
					'name' : 'key_11',
					'type' : 'button',
					'x' : 440,
					'y' : 24,
				},
				{
					'name' : 'key_12',
					'type' : 'button',
					'x' : 480,
					'y' : 24,
				},
				{
					'name' : 'key_13',
					'type' : 'button',
					'x' : 40,
					'y' : 63,
				},
				{
					'name' : 'key_14',
					'type' : 'button',
					'x' : 80,
					'y' : 63,
				},
				{
					'name' : 'key_15',
					'type' : 'button',
					'x' : 120,
					'y' : 63,
				},
				{
					'name' : 'key_16',
					'type' : 'button',
					'x' : 160,
					'y' : 63,
				},
				{
					'name' : 'key_17',
					'type' : 'button',
					'x' : 200,
					'y' : 63,
				},
				{
					'name' : 'key_18',
					'type' : 'button',
					'x' : 240,
					'y' : 63,
				},
				{
					'name' : 'key_19',
					'type' : 'button',
					'x' : 280,
					'y' : 63,
				},
				{
					'name' : 'key_20',
					'type' : 'button',
					'x' : 320,
					'y' : 63,
				},
				{
					'name' : 'key_21',
					'type' : 'button',
					'x' : 360,
					'y' : 63,
				},
				{
					'name' : 'key_22',
					'type' : 'button',
					'x' : 400,
					'y' : 63,
				},
				{
					'name' : 'key_23',
					'type' : 'button',
					'x' : 440,
					'y' : 63,
				},
				{
					'name' : 'key_24',
					'type' : 'button',
					'x' : 480,
					'y' : 63,
				},
				{
					'name' : 'key_25',
					'type' : 'button',
					'x' : 60,
					'y' : 104,
				},
				{
					'name' : 'key_26',
					'type' : 'button',
					'x' : 100,
					'y' : 104,
				},
				{
					'name' : 'key_27',
					'type' : 'button',
					'x' : 140,
					'y' : 104,
				},
				{
					'name' : 'key_28',
					'type' : 'button',
					'x' : 180,
					'y' : 104,
				},
				{
					'name' : 'key_29',
					'type' : 'button',
					'x' : 220,
					'y' : 104,
				},
				{
					'name' : 'key_30',
					'type' : 'button',
					'x' : 260,
					'y' : 104,
				},
				{
					'name' : 'key_31',
					'type' : 'button',
					'x' : 300,
					'y' : 104,
				},
				{
					'name' : 'key_32',
					'type' : 'button',
					'x' : 340,
					'y' : 104,
				},
				{
					'name' : 'key_33',
					'type' : 'button',
					'x' : 380,
					'y' : 104,
				},
				{
					'name' : 'key_34',
					'type' : 'button',
					'x' : 420,
					'y' : 104,
				},
				{
					'name' : 'key_35',
					'type' : 'button',
					'x' : 460,
					'y' : 104,
				},
				{
					'name' : 'key_36',
					'type' : 'button',
					'x' : 60,
					'y' : 144,
				},
				{
					'name' : 'key_37',
					'type' : 'button',
					'x' : 100,
					'y' : 144,
				},
				{
					'name' : 'key_38',
					'type' : 'button',
					'x' : 140,
					'y' : 144,
				},
				{
					'name' : 'key_39',
					'type' : 'button',
					'x' : 180,
					'y' : 144,
				},
				{
					'name' : 'key_40',
					'type' : 'button',
					'x' : 220,
					'y' : 144,
				},
				{
					'name' : 'key_41',
					'type' : 'button',
					'x' : 260,
					'y' : 144,
				},
				{
					'name' : 'key_42',
					'type' : 'button',
					'x' : 300,
					'y' : 144,
				},
				{
					'name' : 'key_43',
					'type' : 'button',
					'x' : 340,
					'y' : 144,
				},
				{
					'name' : 'key_44',
					'type' : 'button',
					'x' : 380,
					'y' : 144,
				},
				{
					'name' : 'key_45',
					'type' : 'button',
					'x' : 420,
					'y' : 144,
				},
				{
					'name' : 'key_46',
					'type' : 'button',
					'x' : 460,
					'y' : 144,
				},
			)
		},

		## ConnectBoard
		{
			"name" : "ConnectBoard",
			"type" : "thinboard",

			"x" : (SCREEN_WIDTH - 9999) / 2,
			"y" : (SCREEN_HEIGHT - 9999 - 35),
			"width" : 208,
			"height" : 30,

			"children" :
			(
			),
		},
		## Logo
		{
			"name" : "logo",
			"type" : "image",

			"x" : 85,
			"y" : SCREEN_HEIGHT - SERVER_BOARD_HEIGHT + - 245,
			"width" : 308,
			"height" : 143,
			"image" : 'locale/de/ui/j0kerdev/j0ker_dev_logo.tga',
			"children" :
			(
			),
		},
		
		## Render
		{
			"name" : "render",
			"type" : "image",

			"x" : 600,
			"y" : SCREEN_HEIGHT - SERVER_BOARD_HEIGHT + - 125,
			"width" : 308,
			"height" : 143,
			"image" : 'locale/de/ui/j0kerdev/j0ker_dev_render.tga',
			"children" :
			(
			),
		},
		## LoginBoard
		{
			"name" : "LoginBoard",
			"type" : "image",

			"x" : 98.5 + 20 ,
			"y" : SCREEN_HEIGHT - SERVER_BOARD_HEIGHT - -20,
			"width" : 375,
			"height" : SERVER_BOARD_HEIGHT,

			"image" : 'locale/de/ui/j0kerdev/j0ker_dev_mail_login.tga',

			"children" :
			(
				{
					"name" : "ID_EditLine",
					"type" : "editline",

					"x" : 20,
					"y" : 66,

					"width" : 120,
					"height" : 18,

					"input_limit" : 24,
					"enable_codepage" : 0,

					"r" : 1.0,
					"g" : 1.0,
					"b" : 1.0,
					"a" : 1.0,
				},
				{
					"name" : "Password_EditLine",
					"type" : "editline",

					"x" : 20,
					"y" : 107,

					"width" : 120,
					"height" : 18,

					"input_limit" : 24,
					"secret_flag" : 1,
					"enable_codepage" : 0,

					"r" : 1.0,
					"g" : 1.0,
					"b" : 1.0,
					"a" : 1.0,
				},
				{
					"name" : "LoginButton",
					"type" : "button",

					"x" : 9,
					"y" : 202,

					"default_image" : 'locale/de/ui/j0kerdev/j0ker_dev_join.tga',
					"over_image" : 'locale/de/ui/j0kerdev/j0ker_dev_join_h.tga',
					"down_image" : 'locale/de/ui/j0kerdev/j0ker_dev_join.tga',

				},
				{
					"name" : "LoginExitButton",
					"type" : "button",

					"x" : 15,
					"y" : 155,

					"default_image" : 'locale/de/ui/j0kerdev/j0ker_dev_beenden.tga',
					"over_image" : 'locale/de/ui/j0kerdev/j0ker_dev_beenden_h.tga',
					"down_image" : 'locale/de/ui/j0kerdev/j0ker_dev_beenden_3.tga',

				},
				{
					"name" : "ConnectName",
					"type" : "text",

					"x" : 80,
					"y" : 0,
					"vertical_align" : "center",
					"text_vertical_align" : "center",

				},
				{
					"name" : "SelectConnectButton",
					"type" : "button",

					"x" : 150,
					"y" : 35,
					"vertical_align" : "center",

					"default_image" : 'locale/de/ui/j0kerdev/j0ker_dev_channel.tga',
					"over_image" : 'locale/de/ui/j0kerdev/j0ker_dev_channel_h.tga',
					"down_image" : 'locale/de/ui/j0kerdev/j0ker_dev_channel_3.tga',

				},
			),
		},

		## ServerBoard
		{
			"name" : "ServerBoard",
			"type" : "image",

			"x" : -256.5,
			"y" : SCREEN_HEIGHT - SERVER_BOARD_HEIGHT - - 20,
			"width" : 375,
			"height" : SERVER_BOARD_HEIGHT,
			"horizontal_align" : "center",
			"image" : 'locale/de/ui/j0kerdev/j0ker_dev_mail1.tga',

			"children" :
			(

				## Title
				{
					"name" : "Title",
					"type" : "text",

					"x" : 15,
					"y" : 12,
					"horizontal_align" : "center",
					"text_horizontal_align" : "center",
					
				},
				## ListBox
				{
					"name" : "ServerList",
					"type" : "listbox2",

					"x" : 15,
					"y" : 47,
					"width" : 109,
					"height" : SERVER_LIST_HEIGHT,
					"row_count" : 18,
					"item_align" : 0,
				},
				{
					"name" : "ChannelList",
					"type" : "listbox",

					"x" : 146,
					"y" : 46,
					"width" : 109,
					"height" : SERVER_LIST_HEIGHT,

					"item_align" : 0,
				},

				## Buttons
				{
					"name" : "ServerSelectButton",
					"type" : "button",

					"x" : 10,
					"y" : 215,

					"default_image" : 'locale/de/ui/j0kerdev/j0ker_dev_weiter.tga',
					"over_image" : 'locale/de/ui/j0kerdev/j0ker_dev_weiter_h.tga',
					"down_image" : 'locale/de/ui/j0kerdev/j0ker_dev_weiter_3.tga',

				},
				{
					"name" : "ServerExitButton",
					"type" : "button",

					"x" : 160,
					"y" : 215,

					"default_image" : 'locale/de/ui/j0kerdev/j0ker_dev_beenden.tga',
					"over_image" : 'locale/de/ui/j0kerdev/j0ker_dev_beenden_h.tga',
					"down_image" : 'locale/de/ui/j0kerdev/j0ker_dev_beenden_3.tga',
				},

			),

		},
	),
}
