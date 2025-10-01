import random

print("Let's create a story! Please provide the following words:")

name = input("Write your name: ")
noun = input("Write a noun: ")
adj = input("Write an adjective(feeling): ")
verb = input("Write a verb: ")
adj2 = input("Write an adjective(feeling) again: ")
animal = input("Write an animal: ")
verb2 = input("Write a verb again: ")
color = input("Write a color: ")
verb_ing = input("Write a verb (ending in ing): ")
adverb = input("Write an adverb (ending in ly): ")
number = input("Write a number: ")
time_measure = random.choice(["days", "weeks", "months", "years"])
silly_word = input("Write a silly word: ")
noun2 = input("Write a noun again: ")

template = f"""
            This weekend I am going camping with {name}. I packed my lantern, sleeping bag, and {noun}. 
            I am so {adj} to {verb} in a tent. 
            I am {adj2} we might see a(n) {animal}, I hear they're kind of dangerous. 
            While we're camping, we are going to hike, fish, and {verb2}. 
            I have heard that the {color} lake is great for {verb_ing}. 
            Then we will {adverb} hike through the forest for {number} {time_measure}. 
            If I see a {color} {animal} while hiking, I am going to bring it home as a pet! 
            At night we will tell {number} {silly_word} stories and roast {noun2} around the campfire!!
            """

print("\nHere is your story:\n")
print(template)








