class Menu:
  #all available menus with items and times
  def __init__(self,name,items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  #constructor to give the available times
  def __repr__(self):
    return self.name + ' is available from: ' +str(self.start_time) + ' till ' +str(self.end_time)
  #method to calculate the bill. First create a variable. Loop through all the items and if they are in the list items, add them to the total
  def calculate_bill(self, purchased_items):
    bill_total = 0
    for item in purchased_items:
      if item in self.items:
        bill_total += self.items[item]
    return bill_total
#lists of all items
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
#adds soms menus
brunch_menu = Menu('Brunch menu', brunch_items, 1100, 1600)
#print(brunch_menu.name)
early_bird_menu = Menu('Early Bird menu', early_bird_items, 1500, 1800)

diner_menu = Menu('Diner menu', dinner_items, 1700, 2300)

kids_menu = Menu('Kids menu', kids_items, 1100, 2100)

arepas_menu = Menu("Take a' Arepa", arepas_items, 1000, 2000)
#print(brunch_menu)

#print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))

#print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
#class for franchises
class Franchise:

  def __init__(self, adress, menus):
    self.adress = adress
    self.menus = menus

  def __repr__(self):
    return 'located on ' + self.adress
  #loops through all menus when they are available.
  def available_menus(self, time):
      #first an empty array
    available_menu = []
    #then loop through all menus, watch the self
    for menu in self.menus:
        #check if the menus are available, watch the menu.dot
      if time >= menu.start_time and time <= menu.end_time:
        available_menu.append(menu)
    return available_menu
#adds soms data
flagship_store = Franchise("1232 West End Road", [brunch_menu, early_bird_menu, diner_menu, kids_menu])

new_installment = Franchise("12 East Mulberry Street", [brunch_menu, early_bird_menu, diner_menu, kids_menu])

arepas_place = Franchise("189 Fitzgerald Avenue", [brunch_menu, early_bird_menu, diner_menu, kids_menu, arepas_menu])

#print (flagship_store)
print(flagship_store.available_menus(1400))
print(flagship_store.available_menus(1700))
print(arepas_place.available_menus(1700))
#adds some business and add franchises to them.
class Business:

  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

  def __repr__(self):
    return self.name

business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment, arepas_place])

print (business)
