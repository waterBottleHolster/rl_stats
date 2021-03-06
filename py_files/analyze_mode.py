import ui
import rl_stats

class analyzeScreen(ui.View):
  def __init__(self, *args, **kwargs):
    self.present('sheet', hide_title_bar = True)
    
  def did_load(self):
    # assign an action to back btn
    self["scrollview1"]["back_btn"].action = self.back_btn_click
    
  def back_btn_click(self, sender):
    self.close()
    self.wait_modal()
    homeScreen = rl_stats.homeScreen
    v = ui.load_view("rl_stats.pyui")
    
  # I want a way to select an independant var and then return the win-loss record.
  # Then upgrade to be able to do n-number of independant vars, still returning the win-loss record.

if __name__ == "__main__":
  v = ui.load_view()
