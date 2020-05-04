import ui
import rl_stats

class cameraControlsScreen(ui.View):
  def __init__(self, *args, **kwargs):
    pass
  
  def did_load(self):
    # this won't 
    pass


if __name__ == "__main__":
  view = cameraControlsScreen
  view.present("fullscreen", hide_title_bar = True)
