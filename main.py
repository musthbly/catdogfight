import art
from random import randint

def print_sidebyside(sprite1, sprite2, num_spaces = 1):
  spaces = ' ' * num_spaces
  for a, b in zip(sprite1.splitlines(), sprite2.splitlines()):
    print(f'{a}{spaces}{b}')

def main():
  num_lives = 12
  cat_lives = num_lives
  dog_lives = num_lives
  cat_sprite = 'ok'
  dog_sprite = 'ok'
  winner = ''
  game_over = False

  print(art.logo)

  while not game_over:
    print_sidebyside(art.cat[cat_sprite], art.dog[dog_sprite], 5)
    cat_healthbar = '|' * cat_lives + '-' * (num_lives - cat_lives)
    dog_healthbar = '|' * dog_lives + '-' * (num_lives - dog_lives)
    print('\n' + cat_healthbar + '       ' + dog_healthbar)

    input("\npress enter to roll the dice")
    cat_roll = randint(1, 6)
    dog_roll = randint(1, 6)
    print_sidebyside(art.die[cat_roll - 1], art.die[dog_roll - 1], 10)

    if cat_roll == dog_roll:
      cat_sprite = 'ok'
      dog_sprite = 'ok'
    elif cat_roll > dog_roll:
      dog_lives -= 1
      cat_sprite = 'yay'
      dog_sprite = 'hurt'
    elif dog_roll > cat_roll:
      cat_lives -= 1
      cat_sprite = 'hurt'
      dog_sprite = 'yay'

    if cat_lives == 0:
      game_over = True
      winner = 'dog'
      cat_sprite = 'dead'
      dog_sprite = 'yay'
    elif dog_lives == 0:
      game_over = True
      winner = 'cat'
      cat_sprite = 'yay'
      dog_sprite = 'dead'

  print_sidebyside(art.cat[cat_sprite], art.dog[dog_sprite], 5)
  input(f'\n{winner} won! press enter to play again')
  main()

main()