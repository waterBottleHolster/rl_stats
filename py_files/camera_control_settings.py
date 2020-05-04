import ui
import rl_stats
import json
from objc_util import *

def_json_fp = '/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/json_files/def_json.json'

bd = 2
xl_lbl_font = ("Futura-CondensedExtraBold", 30)
sm_lbl_font = ("Futura-CondensedExtraBold", 18)

class cameraControlsScreen(ui.View):
  def __init__(self, *args, **kwargs):
    self.frame = (0, 20, 375, 580)
    # The big banner labels aren't created from the json so do them first.
    self.banner1_lbl = ui.Label(self, text = "CAMERA SETTINGS", font = xl_lbl_font, alignment = ui.ALIGN_CENTER, border_width = bd)
    self.banner2_lbl = ui.Label(self, text = "CONTROLLER SETTINGS", font = xl_lbl_font, alignment = ui.ALIGN_CENTER, border_width = bd)

    # The save and back btns are also not reliant on the json.
    self.save_btn = ui.Button(self, title = "SAVE", font = xl_lbl_font, border_width = bd, background_color = "")
    self.back_btn = ui.Button(self, title = "BACK", font = xl_lbl_font, border_width = bd, background_color = "")

    self.banner1_lbl.frame = (0, 20, 375, 32)
    self.banner2_lbl.frame = (0, 268, 375, 32)
    self.save_btn.frame = (0, 568, 160, 32)
    self.back_btn.frame = (160, 568, 160, 32)
    
    # Now to create the bulk of the labels, look to the def_json.json file.
    # def_json_dict has the json file's info while widget_dict contains the created widgets.d
    # Do all the camera-related widgets, then move onto the controller-related widgets.
    with open(def_json_fp, 'r') as f:
      self.def_json_dict = json.load(f)

    self.widget_dict = {}
    x = 0; y = 60; width = 187.5; height = 20

    for key in self.def_json_dict["camera_settings"]:
      # do LHS first
      self.hdr_lbl = ui.Label(self, text = key, font = sm_lbl_font, alignment = ui.ALIGN_RIGHT, border_width = bd)
      self.hdr_lbl.frame = (x, y, width, height)
      self.widget_dict[key] = self.hdr_lbl
      
      # now do RHS second
      if self.def_json_dict["camera_settings"][key] == "textfield":
        #self.subv = ui.View(self)
        #self.subv.frame = (x + width, y, width, height)
        self.tf = ui.TextField(self)
        self.tf.frame = (x + width, y, width, height)
        self.tf.tint_color = 'white'
        self.tf.text_color = 'white'
        self.tf.border_width = 2
        self.tf.border_color = 'black'
        #self.subv.add_subview(self.tf)
        
        self.tfo = ObjCInstance(self.tf).textField()
        self.tfo.backgroundColor = ObjCClass('UIColor').colorWithRed_green_blue_alpha_(0, 0, 0, 0)
        
        self.widget_dict[key+"_txt"] = self.tf
        
      elif self.def_json_dict["camera_settings"][key] == "checkbox":
        pass
      
      y = y + height
    
    self.add_subview(self.banner1_lbl)
    self.add_subview(self.banner2_lbl)
    for item in self.widget_dict:
      self.add_subview(self.widget_dict[item])
    

if __name__ == "__main__":
  view = cameraControlsScreen()
  view.present("fullscreen", hide_title_bar = True)
