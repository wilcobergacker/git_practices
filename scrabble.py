letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#combine two list in one dict
letter_to_points = {
  key: value
  for key, value
  in zip(letters, points)
}

#add extra space with value 0
letter_to_points[" "] = 0
#print (letter_to_points)

#counts all values in a word and adds them to point_total
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total
#test the function
brownie_points = score_word("BRWONIE")
#print(brownie_points)

#added dict with keys and values
player_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT"],
	"wordNerd": ["EARTH", "EYES", "MACHINE"],
	"Lexi Con": ["ERASER", "BELLY", "HUSKY"],
	"Prof Reader": ["ZAP", "COMA", "PERIOD"]}

#print(player_to_words)
player_to_points = {}

#loops through the dict and adds all values of letters
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
    #adds the total on a player
    player_to_points[player] = player_points

print(player_to_points)
