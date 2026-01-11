#from Chef import Chef(gamitin mo lang to kapag nasa ibang file yung class mo)


class ChineseChef(Chef):#yung (Chef) dito is called inheritance, iniinherit mo yung functionality ng isang class para magamit ito
  
  def make_friend_rice(self):
    print("The chef makes friend rice")
  def make_friend_rice(self):
    print("The chef makes friend rice")

class Chef:
  def make_chicken(self):
    print("The chef makes a chicken")
  
  def make_salad(self):
    print("The chef makes a salad")

  def make_special_dish(self):
    print("The chef makes bbq ribs")


myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_chicken()