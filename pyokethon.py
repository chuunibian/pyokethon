import random

class player:
	number_of_pokemon = 3

	def __init__(self, pokemon_list):
		self.pokemon_list = pokemon_list

	def remove_pokemon(name):
		for pokemon in self.pokemon_list:
			if pokemon.name == name:
				self.pokemon_list.remove(pokemon)
				self.number_of_pokemon -= 1



class pokemon:
	pass

	def __init__(self, health, basic_defense, speed, type, name):
		self.health = health
		self.basic_defense = basic_defense
		self.speed = speed
		self.type = ""
		self.name = ""
	def get_name():
		return self.name



class serperior(pokemon):
	def __init__(self):
		super().__init__(health = 75, basic_defense = 10, speed = 113, type = "Grass", name = "Serperior")
		self.move_list = ["Tackle", "Vine Whip", "Leaf Blade", "Slam"]
		self.move_list_numerical = [[15, 100], [25, 90], [45, 65], [45, 45]]

class emboar(pokemon):
	def __init__(self):
		super().__init__(health = 110, basic_defense = 20, speed = 65, type = "Fire", name = "Emboar")
		move_list = ["Tackle", "Flame Charge", "Ember", "Flare Blitz"]
		self.tackle = (15, 100)
		self.flame_charge = (30, 80)
		self.ember = (35, 75)
		self.flare_blitz = (70, 30)

class samurott(pokemon):
	def __init__(self):
		super().__init__(health = 95, basic_defense = 20, speed = 70, type = "Water", name = "Samurott")
		move_list = ["Tackle", "Water Gun", "Water Pulse", "Aqua Tail"]
		self.tackle = (15, 100)
		self.water_gun = (35, 83)
		self.water_pulse = (45, 75)
		self.aqua_tail = (65, 40)

class luxray(pokemon):
	def __init__(self):
		super().__init__(health = 110, basic_defense = 20, speed = 65, type = "Fire", name = "Luxray") #need change
		move_list = ["Tackle", "Flame Charge", "Ember", "Flare Blitz"]
		self.tackle = (15, 100)
		self.flame_charge = (30, 80)
		self.ember = (35, 75)
		self.flare_blitz = (70, 30)

class alakazam(pokemon):
	def __init__(self):
		super().__init__(health = 110, basic_defense = 20, speed = 65, type = "Fire", name = "Alakazam") #need change
		move_list = ["Tackle", "Flame Charge", "Ember", "Flare Blitz"]
		self.tackle = (15, 100)
		self.flame_charge = (30, 80)
		self.ember = (35, 75)
		self.flare_blitz = (70, 30)

class lucario(pokemon):
	def __init__(self):
		super().__init__(health = 110, basic_defense = 20, speed = 65, type = "Fire", name = "Lucario") #need change
		move_list = ["Tackle", "Flame Charge", "Ember", "Flare Blitz"]
		self.tackle = (15, 100)
		self.flame_charge = (30, 80)
		self.ember = (35, 75)
		self.flare_blitz = (70, 30)

class game:

	game_state = ""
	serperior_1 = serperior()
	emboar_1 = emboar()
	samurott_1 = samurott()
	luxray_1 = luxray()
	alakazam_1 = alakazam()
	lucario_1 = lucario()

	player_1 = None
	enemy_1 = None

	player_pokemon = []
	computer_pokemon = []
	temp_list = []
	pokemon_list = [serperior_1, emboar_1, samurott_1, luxray_1, alakazam_1, lucario_1] #maybe dictionary
	type_list = [["Water", "Fire"], ["Grass", "Water"], ["Fire", "Grass"], ["Electric", "Water"], ["Psychic", "Fighting"]] #exclude fighting no cor

	def __init__(self):
		game.game_state = "run"

	@staticmethod
	def game_initialize():
		print("Pick 3 of your desired Pokemon")
		print("1 Serperior, 2 Emboar, 3 Samurott, 4 Luxray, 5 Alakazam, 6 Lucario")

		i = 0
		while i < 3:
			temp = input();
			int_temp = int(temp)
			game.temp_list.append(temp)
			game.player_pokemon.append(pokemon_list[int_temp])
			i += 1

		i = 0
		while i < 3:
			del game.pokemon_list[temp_list[i]] #chosen numbers for player

		print("You chose: ")
		print(game.player_pokemon)
		game.computer_pokemon = game.pokemon_list.copy() #copy over the remaining pok
		print("Enemy chose: ")
		print(game.computer_pokemon)

		game.player_1 = player(game.player_pokemon) #make 2 player object and make them have the pokemon lists as instance var
		game.enemy_1 = player(game.computer_pokemon)


	@staticmethod
	def check_state():
		if game.player_1.number_of_pokemon == 0 or game.enemy_1.number_of_pokemon == 0:
			game.game_state = "stop"

	@staticmethod
	def check_pokemon_state(player_pokemon, enemy_pokemon):
		if player_pokemon.health <= 0 or enemy_pokemon.health <= 0:
			return 1
		elif player_pokemon.speed < enemy_pokemon.speed:
			return 2
		elif player_pokemon.speed > enemy_pokemon.speed:
			return 3
		elif player_pokemon.speed == enemy_pokemon.speed:
			return 4


	@staticmethod
	def game_flow():
		print("Opponent will start with" + enemy_1.pokemon_list[0].get_name())
		print("Select your pokemon:")
		first_selection = input();
		temp_player_pokemon = game.player_1.pokemon_list[first_selection - 1] #ref to the list item
		temp_enemy_pokemon = game.enemy_1.pokemon_list[0]

		while game.game_state == "run":
			state_int = game.check_pokemon_state(temp_player_pokemon, temp_enemy_pokemon)

			if state_int == 1:
				if temp_player_pokemon.health <= 0:
					game.player_1.number_of_pokemon -= 1
					print("Your {} was defeated!".format(temp_player_pokemon.name))
					print("Select next pokemon")
					game.player_1.remove_pokemon(temp_player_pokemon.name)
					print(game.player_1.pokemon_list)
					temp_input = input()
					temp_player_pokemon = game.player_1.pokemon_list[int(temp_input - 1)] #must be integer idk if need cast
				else:
					game.enemy_1.number_of_pokemon -= 1
					print("Enemy {} was defeated!".format(temp_enemy_pokemon.name))
					game.enemy_1.remove_pokemon(temp_enemy_pokemon.name)
					temp_enemy_pokemon = game.enemy_1.pokemon_list[0]
					print("Enemy chooses {}".format(temp_enemy_pokemon.name))
			elif state_int == 2:
				rand_int = random.randint(0,3)
				rand_int_probability = random.randint(1,100)
				print("{} Attacks first. Uses {}".format(temp_enemy_pokemon.name, temp_enemy_pokemon.move_list[rand_int]))
				if temp_enemy_pokemon.move_list_numerical[rand_int][1] < rand_int_probability: #checking move hit probability
					print("Attack Missed!")
					print("Choose your attack: ")
					print(temp_player_pokemon.move_list)
					temp_player_attack = input()
					rand_int_probability = random.randint(1,100)
					if temp_enemy_pokemon.move_list_numerical[temp_player_attack][1] < rand_int_probability:
						player_attack_damage = calculate_damage(temp_player_pokemon, temp_enemy_pokemon, temp_enemy_pokemon.move_list_numerical[temp_player_attack][0]) #gets dmg
						print("{} attacks for {} damage".format(temp_player_pokemon.name, player_attack_damage))
						temp_enemy_pokemon.health -= player_attack_damage
						temp_enemy_pokemon.health += temp_enemy_pokemon.basic_defense #add back the defense
						print("Enemy {} health is {}", temp_enemy_pokemon.name, temp_enemy_pokemon.health)
					else:
						print("Attack Missed!")
				else:
					enemy_attack_damage = calculate_damage(temp_enemy_pokemon, temp_player_pokemon, temp_enemy_pokemon.move_list_numerical[random.randint(0,3)][0]) #gets dmg
					print("{} attacks for {} damage".format(temp_enemy_pokemon.name, enemy_attack_damage))
					temp_player_pokemon.health -= enemy_attack_damage
					temp_player_pokemon.health += temp_player_pokemon.basic_defense #add back the defense
					print("Your {} health is {}", temp_player_pokemon.name, temp_player_pokemon.health)

			elif state_int == 3:
				print("Choose your move:")
				print(temp_player_pokemon.move_list)
				player_input = input()
				rand_int_probability = random.randint(1,100)
				print("{} Attacks first. Uses {}".format(temp_player_pokemon.name, temp_player_pokemon.move_list[player_input]))
				if temp_player_pokemon.move_list_numerical[player_input][1] < rand_int_probability: #checking move hit probability

					print("Attack Missed!")
					rand_int_enemy = random.randint(0,3)
					print("Enemy {} chooses {} attack".format(temp_enemy_pokemon.name, temp_enemy_pokemon.move_list[rand_int_enemy]))
					rand_int_probability = random.randint(1,100)

					if temp_enemy_pokemon.move_list_numerical[rand_int_enemy][1] < rand_int_probability:
						enemy_attack_damage = calculate_damage(temp_enemy_pokemon, temp_player_pokemon, temp_enemy_pokemon.move_list_numerical[rand_int_enemy][0]) #gets dmg
						print("{} attacks for {} damage".format(temp_enemy_pokemon.name, enemy_attack_damage))
						temp_player_pokemon.health -= enemy_attack_damage
						temp_player_pokemon.health += temp_player_pokemon.basic_defense #add back the defense
						print("Your {} health is {}", temp_player_pokemon.name, temp_player_pokemon.health)
					else:
						print("Attack Missed!")
				else:
					player_attack_damage = calculate_damage(temp_player_pokemon, temp_enemy_pokemon, temp_player_pokemon.move_list_numerical[player_input][0]) #gets dmg
					print("{} attacks for {} damage".format(temp_enemy_pokemon.name, enemy_attack_damage))

					temp_enemy_pokemon.health -= player_attack_damage
					temp_enemy_pokemon.health += temp_enemy_pokemon.basic_defense #add back the defense
					print("Enemy's {} health is {}", temp_enemy_pokemon.name, temp_enemy_pokemon.health)

			elif state_int == 4:
				print("Skip")
				temp_enemy_pokemon.speed += 1

			game.check_state()
			


	@staticmethod #this does it by indep and dep order does matter 
	def calculate_damage(independent_type, dependent_type, move_damage): #for this no defensive typing debuff but can easily do with another function and check on defending end
		for type in game.type_list:
			if type[0] == independent_type and type[1] == dependent_type:
				return move_damage + 20
		return move_damage

def main():
	game_obj = game()
	game_obj.game_initialize()
	game_obj.game_flow()


if __name__ == "__main__":
	main()