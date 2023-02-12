# Mad Libs game in Python

# Helper function to get user input and return the modified string
def get_user_input(prompt):
  user_input = input(prompt)
  return user_input

# Define the mad libs story as a string
story = "Once upon a time, deep in an ancient jungle, there lived a __noun__. This __noun__ was very __adjective__ and loved to __verb__ all day long. One day, while the __noun__ was __verb__ing, it stumbled upon a __adjective__ looking __noun__. The __noun__ was startled and quickly __verb__ed away, but not before the __adjective__ __noun__ had a chance to __verb__ it."

# Prompt the user for words to fill in the blanks
noun1 = get_user_input("Enter a noun: ")
noun2 = get_user_input("Enter another noun: ")
adjective1 = get_user_input("Enter an adjective: ")
verb1 = get_user_input("Enter a verb: ")
verb2 = get_user_input("Enter another verb: ")
adjective2 = get_user_input("Enter another adjective: ")
verb3 = get_user_input("Enter one last verb: ")

# Insert the user's words into the story string
story = story.replace("__noun__", noun1)
story = story.replace("__noun__", noun2, 1)
story = story.replace("__adjective__", adjective1)
story = story.replace("__verb__", verb1)
story = story.replace("__verb__", verb2, 1)
story = story.replace("__adjective__", adjective2, 1)
story = story.replace("__verb__", verb3, 1)

# Print the resulting mad libs story
print(story)
