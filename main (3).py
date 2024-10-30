#⬛
#🟨
#🟩
import random
from collections import Counter
from collections import defaultdict

words_list = [
    "space", "earth", "orbit", "galaxy", "comet", "asteroid", "astronaut",
    "nebula", "stars", "moon", "pluto", "constellation", "universe",
    "interstellar", "cosmos", "mars", "venus", "rocket", "jupiter", "planet"
]

chosen_word = random.choice(words_list)
print(
    f"Welcome to Space Wordle! Guess the {len(chosen_word)} letter word. You have six attempts."
)

lives = 6
while True:

  result = ["⬛"] * len(chosen_word)
  user_guess = input("Enter your guess: ")
  chosen_word_dict = Counter(chosen_word)

  # defaultdict(int)
  # for j in range(len(chosen_word)):
  #   chosen_word_dict[chosen_word[j]] += 1

  if len(user_guess) != len(chosen_word):
    print(f"Please enter a word that has {len(chosen_word)} letters.")
    continue

  elif user_guess == chosen_word:
    print("Congratulations! You won the game.")
    break

  for i in range(len(chosen_word)):

    if user_guess[i] == chosen_word[i]:
      result[i] = "🟩"
      chosen_word_dict[user_guess[i]] -= 1

  for k in range(len(chosen_word)):

    if result[k] == "⬛" and user_guess[k] in chosen_word and chosen_word_dict[
        user_guess[k]] > 0:
      result[k] = "🟨"

  lives -= 1

  # if user_guess[i] in chosen_word_dict and chosen_word_dict[user_guess[i]] > 0:
  #   chosen_word_dict[user_guess[i]] -= 1
  #   if chosen_word_dict[user_guess[i]] < 0:
  #     result += "⬛"

  # for k in range(len(chosen_word)):
  #   if user_guess[k] ==

  if lives == 0:
    print(f"You ran out of guesses. The correct word is {chosen_word}.")
    break
  print("".join(result))

# grid_columns = int(input("Enter the number of columns for the grid: "))
# grid_rows = int(input("Enter the number of rows for the grid: "))

# outer_grid = []

# for i in range(grid_rows):
#   inner_grid = []
#   for j in range(grid_columns):

#     element = int(input("Enter the number you want to insert in the grid: "))
#     inner_grid.append(element)
#   outer_grid.append(inner_grid)

# print(outer_grid)

# new_list = []
# for k in range(len(outer_grid)):
#   for m in range(len(outer_grid[0])):
#     new_list.append(outer_grid[k][m])

# print(new_list)

#     # i=0
# # while i < (grid_columns):
# #   inner_grid.append("_")
# #   i+=1

# # j=0
# # while j < (grid_rows):
# #   outer_grid.append(inner_grid)
# #   j+=1

# # print(outer_grid)

# # replacement_x_coordinate = int(input("What is the x-coordinate of the place you want to enter: "))
# # replacement_y_coordinate = int(input("What is the y-coordinate of the place you want to enter: "))

# # element = int(input("Enter the number you want to insert in the grid: "))

# # print(outer_grid)
# # print(replacement_x_coordinate)
# # print(outer_grid[replacement_x_coordinate])
# # outer_grid[replacement_x_coordinate][replacement_y_coordinate] = element
# # print(outer_grid[replacement_x_coordinate])
# # print(outer_grid)
