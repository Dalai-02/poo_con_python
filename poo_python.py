class Character:
    #Constructor de la clase(Atributos)
    name = "Default"
    strength = 0
    intelligence = 0
    defense = 0
    life = 0
    #Indicar que no se haga nada
    pass

#Variable del constructor vacio que almacena la clase
my_character = Character()
my_character.name = "Pompompurin"
my_character.strength = 10
my_character.intelligence = 10
my_character.defense = 10
my_character.life = 100

#Imprimir la variable con su respectivo atributo
print("The name of my character is:" ,my_character.name)
print("The strength of my character is:" ,my_character.strength)
print("The intelligence of my character is:" ,my_character.intelligence)   
print("The defense of my character is:" ,my_character.defense)
print("The life of my character is:" ,my_character.life)    