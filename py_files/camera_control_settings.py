# no associated .pyui file b/c one was never needed.
import ui
import rl_stats
import json

def_json_fp = ""


bd = 2
xl_lbl_font = ("Futura-CondensedExtraBold", 30)
sm_lbl_font = ("Futura-CondensedExtraBold", 18)

class cameraControlsScreen(ui.View):
  def __init__(self, *args, **kwargs):
    # The big banner labels aren't created from the json so do them first.
    self.banner1_lbl = ui.Label(self, text = "CAMERA SETTINGS", font = xl_lbl_font, ui.ALIGN_CENTER, border_width = bd)
    self.banner2_lbl = ui.Label(self, text = "CAMERA SETTINGS", font = xl_lbl_font, ui.ALIGN_CENTER, border_width = bd)

    # The save and back btns are also not reliant on the json.
    self.save_btn = ui.Button(self, title = "SAVE", font = xl_lbl_font, border_widget = bd, background_color = "")
    self.back_btn = ui.Button(self, title = "BACK", font = xl_lbl_font, border_widget = bd, background_color = "")

    self.banner1_lbl.frame = (0, 0, 320, 32)
    self.banner1_lbl.frame = (0, 248, 320, 32)
    self.save_btn.frame = (0, 568, 160, 32)
    self.back_btn.frame = (160, 568, 160, 32)
    
    # Now to create the bulk of the labels, look to the def_json.json file.
    with open(def_json_fp, 'r') as f:
      self.def_json_dict = json.load(f)
      
    
    
    
    self.add_subview(self.banner1_lbl)
    self.add_subview(self.banner2_lbl)
    

if __name__ == "__main__":
  view = cameraControlsScreen
  view.present("fullscreen", hide_title_bar = True)
