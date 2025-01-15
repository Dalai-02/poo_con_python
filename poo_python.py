class Character:
    #Constructor de la clase(Atributos)
    name = "Default"
    strength = 0
    intelligence = 0
    defense = 0
    life = 0
    
    #Constructor de la clase
    def __init__(self, name, strength, intelligence, defense, life):
        self.__name = name
        self.strength = strength
        self.intelligence = intelligence
        self.defense = defense 
        self.life = life

    def imprimir_atributos(self):
        print(self.__name)
        print("Strength: ",self.strength)
        print("Inteligence: ",self.intelligence)
        print("Defense: ",self.defense)
        print("Life: ",self.life)

    def level_up(self, strength, intelligence, defense):
        self.strength = self.strength + strength
        #self.strength += strength
        self.intelligence = self.intelligence + intelligence
        self.defense = self.defense + defense   

    def is_alive(self):
        return self.life > 0
    
    def die(self):
        self.life = 0
        print("self.__name has died")
        #return self.life <= 0

    def damage(self, enemy):
        return max(0, self.strength - enemy.defense)
    
    def attack(self, enemy):
        damage = self.damage(enemy)
        enemy.life = max(0, enemy.life - damage)
        #enemy.life -= damage
        print("------attack------")
        print(self.__name, "has made", damage, "damage to", enemy.__name)
        print("life of" , enemy.__name , "is", enemy.life)
    
#Variable del constructor vacio que almacena la clase
print("------------Character------------")
my_character = Character("Dante", 100, 3, 70, 100)
my_character.imprimir_atributos()

my_enemy = Character("Vergil", 70, 30, 70, 100)
# print(my_character.damage(my_enemy))

my_character.attack(my_enemy)
print("------------Enemy after attack------------")
my_enemy.imprimir_atributos()


    


#print(my_character.is_alive())

# print("------------Level up------------")
# my_character.level_up(10, 1, 5)
# my_character.imprimir_atributos()

# my_character.__name = "Pompompurin"
# my_character.strength = 10
# my_character.intelligence = 10
# my_character.defense = 10
# my_character.life = 100

#Imprimir la variable con su respectivo atributo
# print("The name of my character is:" ,my_character.__name)
# print("The strength of my character is:" ,my_character.strength)
# print("The intelligence of my character is:" ,my_character.intelligence)   
# print("The defense of my character is:" ,my_character.defense)
# print("The life of my character is:" ,my_character.life)    