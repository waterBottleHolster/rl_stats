import ui
import drop_down_box
import json
import datetime
import time
import Image
import sound
import analyze_mode

def_json_fp = '/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/json_files/def_json.json'

stats_json_fp = '/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/json_files/stats_json.json'

controller_json_fp = '/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/json_files/controller_settings.json'

camera_json_fp = '/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/json_files/camera_settings.json'

bg_img_fp = '/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/rocket_league_pics/RL_bg_2.JPG'


class homeScreen(ui.View):
	def __init__(self, *args, **kwargs):
		# Note this gets called before the UI file has fully loaded.
		self.present('sheet', hide_title_bar = True)
		
	def did_load(self):
		# This gets called once the UI file has fully loaded.
		# Four things happen: 
		#    - all the UI's drop down boxes are made.
		#    - background image gets added.
		#    - button fonts get changed to something more Rocket League-y.
		#    - lastly the function that assigns actions to each of the btns is called.
		
		# I can't add dropdownviews with the UI editor, so do it here.
		# Step 1: obtain the lists that'll populate the ddb's from def_json.json
		self.def_json_dict = {}
		with open(def_json_fp, 'r') as f:
			self.def_json_dict = json.load(f)

		self.game_mode_list = []
		for item in self.def_json_dict["game_modes"]:
			self.game_mode_list.append(item)
		self.vehicle_list = []
		for item in self.def_json_dict["vehicles"]:
			self.vehicle_list.append(item)
		self.camera_list = []
		for item in self.def_json_dict["camera_settings"]:
			self.camera_list.append(item)
		self.controller_list = []
		for item in self.def_json_dict["controller_settings"]:
			self.controller_list.append(item)
			
		# Create the comboboxes.
		self.game_mode_ddb = drop_down_box.DropdownView()
		self.game_mode_ddb.flex = 'whlrtb'
		self.game_mode_ddb.tint_color = 'black'
		self.game_mode_ddb.frame = (10, 160, 160, 45)
		self.game_mode_ddb.items = self.game_mode_list

		self.vehicle_ddb = drop_down_box.DropdownView()
		self.vehicle_ddb.flex = 'whlrtb'
		self.vehicle_ddb.tint_color = 'black'
		self.vehicle_ddb.frame = (10, 260, 160, 45)
		self.vehicle_ddb.items = self.vehicle_list

		self.camera_ddb = drop_down_box.DropdownView()
		self.camera_ddb.flex = 'whlrtb'
		self.camera_ddb.tint_color = 'black'
		self.camera_ddb.frame = (150, 710, 165, 45)
		self.camera_ddb.items = self.camera_list

		self.controller_ddb = drop_down_box.DropdownView()
		self.controller_ddb.flex = 'whlrtb'
		self.controller_ddb.tint_color = 'black'
		self.controller_ddb.frame = (150, 750, 165, 45)
		self.controller_ddb.items = self.controller_list

		# Add each of the ddb's as subviews.
		self['scrollview1'].add_subview(self.game_mode_ddb)
		self['scrollview1'].add_subview(self.vehicle_ddb)
		self['scrollview1'].add_subview(self.camera_ddb)
		self['scrollview1'].add_subview(self.controller_ddb)
		
		# The background image also gets done here.
		# create the background image (unsure how to do custom image in ui mode...)
		self['scrollview1']['iv1'].image = ui.Image.named(bg_img_fp)
		self['scrollview1']['iv1'].content_mode = ui.CONTENT_SCALE_ASPECT_FILL
		
		# Change the btn fonts.
		for item in self['scrollview1'].subviews:
			if isinstance(item, ui.Button):
				item.font = ('Futura-CondensedExtraBold', 22)

		# Finally, assign actions to each of the buttons.
		self.set_actions()
		
	def set_actions(self):
		for subview in self['scrollview1'].subviews:
			# Start with all the buttons.
			if isinstance(subview, ui.Button):
				if subview.name == "ko_whiff_btn":
					subview.action = self.ko_btn_click
				elif subview.name == "ko_loss_btn":
					subview.action = self.ko_btn_click
				elif subview.name == "ko_win_btn":
					subview.action = self.ko_btn_click
				elif subview.name == "win_game_btn":
					subview.action = self.game_result_btn_click
				elif subview.name == "lose_game_btn":
					subview.action = self.game_result_btn_click
				elif subview.name == "forfeit_btn":
					subview.action = self.game_result_btn_click
				elif subview.name == "disconnect_btn":
					subview.action = self.game_result_btn_click
				elif subview.name == "ot_loss_btn":
					subview.action = self.game_result_btn_click
				elif subview.name == "end_edit_btn":
					subview.action = self.end_editing
				elif subview.name == "analyze_btn":
					subview.action = self.analyze_btn_click
			# Next do the segment_control widget
			elif isinstance(subview, ui.SegmentedControl):
				if subview.name == "sc1":
					subview.action = self.team_select

	def will_close(self):
		# This gets called when the currently presented view is about to be dismissed.  It makes for a good place to save data...
		pass

	def layout(self):
        	# This will be called when a view is resized. You should typically set the
        	# frames of the view's subviews here, if your layout requirements cannot
        	# be fulfilled with the standard auto-resizing (flex) attribute.
        	pass
	
	def ko_btn_click(self, sender):
		if sender.name == 'ko_whiff_btn':
			# increment whiff total by 1
			if self['scrollview1']['whiff_count_lbl'].text == "":
				self['scrollview1']['whiff_count_lbl'].text = "1"
			else:
				cnt = int(self['scrollview1']['whiff_count_lbl'].text)
				cnt = cnt+1
				self['scrollview1']['whiff_count_lbl'].text = str(cnt)
		elif sender.name == 'ko_loss_btn':
			# increment whiff total by 1
			if self['scrollview1']['loss_count_lbl'].text == "":
				self['scrollview1']['loss_count_lbl'].text = "1"
			else:
				cnt = int(self['scrollview1']['loss_count_lbl'].text)
				cnt = cnt+1
				self['scrollview1']['loss_count_lbl'].text = str(cnt)
		elif sender.name == 'ko_win_btn':
			# increment whiff total by 1
			if self['scrollview1']['win_count_lbl'].text == "":
				self['scrollview1']['win_count_lbl'].text = "1"
			else:
				cnt = int(self['scrollview1']['win_count_lbl'].text)
				cnt = cnt+1
				self['scrollview1']['win_count_lbl'].text = str(cnt)
				
	def game_result_btn_click(self, sender):
		json_dict = {}
		with open(stats_json_fp, 'r') as f:
			json_dict = json.load(f)

		# B/c stats_json is a bunch of nested dicts there are some intermediate steps here.
		curr_time = str(datetime.datetime.now())
		curr_time = curr_time[:19]

		# Team is special because it yields 0 or 1 and I'd rather have strings ORANGE/BLUE.
		if self["scrollview1"]["sc1"].selected_index == 0:
			curr_team = "Orange"
		elif self["scrollview0.1"]["sc1"].selected_index == 1:
			curr_team = "Blue"

		# CATs is short for categories
		CATs = ["kickoffs", "game_type", "car_body", "notes", "team", "game_result", "camera_settings", "controller_settings"]

		act_data = [
				{"whiff" : self["scrollview1"]["whiff_count_lbl"].text, "lost" : self["scrollview1"]["loss_count_lbl"].text, "win" : self["scrollview1"]["win_count_lbl"].text},
				{"mode" : game_mode_ddb.text, "competitive" : str(self["scrollview1"]["competitive_switch"].value), "party" : str(self["scrollview1"]["party_switch"].value)},
				{"body" : vehicle_ddb.text, "topper" : self["scrollview1"]["topper_switch"].value, "antenna" : self["scrollview1"]["antenna_switch"].value},
				{"notes" : self["scrollview1"]["textview1"].text},
				curr_team,
				sender.title,
				camera_ddb.text,
				controller_ddb.text
		]

		json_dict[curr_time] = dict(zip(CATs, act_data))

		#with open(stats_json_fp, "w") as f:
			#json.dump(json_dict, f, indent = 2)

		sound.play_effect("Woosh_2")
		time.sleep(1)
		
	def analyze_btn_click(self, sender):
		# Navigate to the analyze_screen
		self.close()
		self.wait_modal()
		analyzeScreen = analyze_mode.analyzeScreen
		v = ui.load_view("analyze_mode.pyui")
	
	def team_select(self, sender):
		if sender.background_color == (0.140449, 0.341092, 0.842697, 1.0):
			sender.background_color = (0.842697, 0.391252, 0.210674, 1.0)
			# This means team == BLUE
		else:
			sender.background_color = (0.140449, 0.341092, 0.842697, 1.0)
			
	def end_editing(self, sender):
		# minimize the keyboard once done typing.
		self["scrollview1"]["textview1"].end_editing()

if __name__ == "__main__":
	view = ui.load_view()
