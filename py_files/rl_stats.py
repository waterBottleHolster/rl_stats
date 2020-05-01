import ui
import drop_down_box
import json
import datetime
def_json_fp = '/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/rocket_league_jsons/def_json.json'

stats_json_fp = '/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/rocket_league_jsons/stats_json.json'


def ko_btn_click(sender):
	if sender.name == 'ko_whiff_btn':
		# increment whiff total by 1
		if v['scrollview1']['whiff_count_lbl'].text == "":
			v['scrollview1']['whiff_count_lbl'].text = "1"
		else:
			cnt = int(v['scrollview1']['whiff_count_lbl'].text)
			cnt = cnt+1
			v['scrollview1']['whiff_count_lbl'].text = str(cnt)
	elif sender.name == 'ko_loss_btn':
		# increment whiff total by 1
		if v['scrollview1']['loss_count_lbl'].text == "":
			v['scrollview1']['loss_count_lbl'].text = "1"
		else:
			cnt = int(v['scrollview1']['loss_count_lbl'].text)
			cnt = cnt+1
			v['scrollview1']['loss_count_lbl'].text = str(cnt)
	elif sender.name == 'ko_win_btn':
		# increment whiff total by 1
		if v['scrollview1']['win_count_lbl'].text == "":
			v['scrollview1']['win_count_lbl'].text = "1"
		else:
			cnt = int(v['scrollview1']['win_count_lbl'].text)
			cnt = cnt+1
			v['scrollview1']['win_count_lbl'].text = str(cnt)
			
def team_select(sender):
	print(sender.selected_index)
	if sender.background_color == (0.140449, 0.341092, 0.842697, 1.0):
		sender.background_color = (0.842697, 0.391252, 0.210674, 1.0)
		# This means team == BLUE
		active_team = "BLUE"
	else:
		sender.background_color = (0.140449, 0.341092, 0.842697, 1.0)
		active_team = "ORANGE"
		
def game_result_btn_click(sender):
	print(sender.name)
	json_dict = {}
	with open(stats_json_fp, 'r') as f:
		json_dict = json.load(f)
		
	# B/c stats_json is a bunch of nested dicts there are some intermediate steps here.
	curr_time = datetime.datetime.now()

	json_dict[curr_time]["kickoffs"]["whiffs"] = v["scrollview1"]["whiff_count_lbl"].text
	json_dict[curr_time]["kickoffs"]["lost"] = v["scrollview1"]["loss_count_lbl"].text
	json_dict[curr_time]["kickoffs"]["win"] = v["scrollview1"]["win_count_lbl"].text

	json_dict[curr_time]["game_type"]["mode"] = v["scrollview1"]["game_mode_ddb"].text
	json_dict[curr_time]["game_type"]["competitive"] = str(v["scrollview1"]["competitive_switch"].value)
	json_dict[curr_time]["game_type"]["party"] = str(tst["party_switch"].value)

	json_dict[curr_time]["car_body"]["body"] = v["scrollview1"]["vehicle_ddb"].text
	json_dict[curr_time]["car_body"]["topper"] = v["scrollview1"]["topper_switch"].value
	json_dict[curr_time]["car_body"]["antenna"] = v["scrollview1"]["antenna_switch"].value

	json_dict[curr_time]["notes"] = v["scrollview1"]["textview1"].text

	if v["scrollview1"]["sc1"].selected_index == 0:
		json_dict[curr_time]["team"] = "Orange"
	elif v["scrollview1"]["sc1"].selected_index == 1:
		json_dict[curr_time]["team"] = "Blue"

	json_dict[curr_time]["game_result"] = sender.name

def end_editing(sender):
	# minimize the keyboard once done typing.
	v["scrollview1"]["textview1"].end_editing()


# populate list of game modes from def_json
def_json_dict = {}
with open(def_json_fp, 'r') as f:
	def_json_dict = json.load(f)

game_mode_list = []
for item in def_json_dict["game_modes"]:
	game_mode_list.append(item)
vehicle_list = []
for item in def_json_dict["vehicles"]:
	vehicle_list.append(item)
	

v = ui.load_view()

game_mode_ddb = drop_down_box.DropdownView()
game_mode_ddb.frame = (15, 160, 150, 45)
game_mode_ddb.items = game_mode_list

vehicle_ddb = drop_down_box.DropdownView()
vehicle_ddb.frame = (15, 260, 150, 45)
vehicle_ddb.items = vehicle_list


# Change the btn fonts b/c I dont know how in the actual ui file.
v['scrollview1']['ko_whiff_btn'].font = ('Futura-CondensedExtraBold', 18)
v['scrollview1']['ko_loss_btn'].font = ('Futura-CondensedExtraBold', 18)
v['scrollview1']['ko_win_btn'].font = ('Futura-CondensedExtraBold', 18)

v['scrollview1'].add_subview(game_mode_ddb)
v['scrollview1'].add_subview(vehicle_ddb)

v.present('fullscreen')
