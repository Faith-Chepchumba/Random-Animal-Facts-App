import random

def get_random_animal_fact():

facts = [

"Cats sleep for 70% of their lives.",

"Dolphins have names for each other.",

"A group of flamingos is called a 'flamboyance'.",

"Elephants are the only mammals that can't jump.",

"Octopuses have three hearts."

]

return random.choice(facts)

def main():

print("Random Animal Facts Generator\n")

while True:

input("Press Enter to get a random animal fact (or type 'quit' to exit): ")

print(get_random_animal_fact(), "\n")

if input().

lower() == 'quit':

break

if __name__ == "__main__":

main()
