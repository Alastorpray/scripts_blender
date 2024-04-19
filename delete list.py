old_list = ['Ant', 'BLOWFISH', 'Bacteria', 'Bad', 'Bull', 'Butterfly', 'Camel', 'Cat Head', 'Chick', 'Cow_s Head', 'Crab', 'Crickets', 'Dinosaur', 'Dog', 'Dolphin', 'Dragon', 'Fox', 'Giraffe', 'Gorilla', 'Hamster Head', 'Hippo', 'Horse', 'Horse_s Head', 'Little Pig', 'Lizard', 'Lobster', 'Monkeys', 'Mosquito', 'Octopus', 'Ox', 'Parihuana', 'Poodle Dog', 'Rabbit', 'Rat Head', 'Rat', 'Reindeer Head', 'Scorpion', 'Shrimp', 'Skunk', 'Spider', 'Tiger Head', 'Tiger', 'Toad Head', 'Tortoise', 'Turkey', 'Unicorn', 'Wasp', 'Whale', 'Wild Pig', 'Wolf']
animals = ["Alpaca", "Ant", "BLOWFISH", "Bacteria", "Bad", "Bear Head", "Bird", "Bull", "Butterfly", "Camel", "Cat", "Cat Head", "Caterpillar", "Chick 2", "Chick", "Chicken Head", "Chicken", "Conch", "Cow_s Head", "Crab", "Crickets", "Crocodile", "Dinosaur", "Dog Head", "Dog", "Dolphin", "Dragon Head", "Dragon", "Eagle Head", "Elephant", "Fish 1", "Fish 2", "Fox", "Giraffe", "Goat", "Gorilla", "Hamster Head", "Hippo", "Horse", "Horse_s Head", "Insect", "Koala Head", "Lion", "Little Pig", "Lizard", "Lobster", "Monkey Head", "Monkeys", "Mosquito", "Octopus", "Owl", "Ox", "Panda", "Parihuana", "Parrot", "Penguin", "Pig Head", "Poodle Dog", "Porcupine Head", "Rabbit Body", "Rabbit", "Raccoon", "Ram", "Rat Head", "Rat", "Reindeer Head", "Rhino Head", "Sauropod", "Scorpion", "Shark", "Sheep", "Shrimp", "Skunk", "Snake", "Spider", "Spiderweb", "Swan", "Tiger Head", "Tiger", "Toad Head", "Tortoise", "Turkey", "Unicorn", "Vache", "Wasp", "Whale Splashing Water", "Whale", "Wild Pig", "Wolf", "Zebra Head"]

# Convertir las dos listas a conjuntos
old_set = set(old_list)
animals_set = set(animals)

# Crear una nueva lista con todas las palabras que no se encuentran en ambas listas
new_list = list(old_set.symmetric_difference(animals_set))

counter = len(new_list)

# Imprimir la nueva lista
print(new_list, counter)