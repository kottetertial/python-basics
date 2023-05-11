import random
import time
import turtle


# UTILITY
def get_turtle(color, shape=None):
    """
    Creates a default turtle.Turtle object. Sets the maximum drawing speed,
    removes the pen, sets the provided color and shape, if any.

    Args:
        color (str) -- the color to set
        shape (str, default None) -- the shape to set, if any

    Returns:
        turtle.Turtle -- the created turtle.Turtle instance
    """
    local_turtle = turtle.Turtle()
    local_turtle.speed(0)
    local_turtle.penup()
    local_turtle.color(color)
    local_turtle.shape(shape)
    return local_turtle


def set_random_coordinates(turtle_object):
    """
    Moves a given turtle.Turtle object to a random place in the game field.

    Args:
        turtle_object (turtle.Turtle) -- the turtle.Turtle to move
    """
    x, y = random.randint(-380, 380), random.randint(-380, 320)
    if is_inside_inventory(x, y):
        set_random_coordinates(turtle_object)
    else:
        turtle_object.setposition(x, y)


def is_out_of_borders(turtle_object):
    """
    Checks whether a given turtle.Turtle object
    is within the allowed borders of the game field.

    Args:
        turtle_object (turtle.Turtle) -- the turtle.Turtle to check

    Returns:
        bool: True, if the turtle.Turtle is outside the allowed borders, False otherwise
    """
    x = turtle_object.xcor()
    y = turtle_object.ycor()
    return x > 400 or x < -400 or y > 335 or y < -400 or is_inside_inventory(x, y)


def is_inside_inventory(x, y):
    """
    Checks whether given coordinates are within the area
    allocated for the inventory.

    Args:
        x (int) -- the x coordinate
        y (int) -- the y coordinate

    Returns:
        bool: True, if the turtle.Turtle is within the inventory borders, False otherwise
    """
    return -400 <= x <= -145 and -400 <= y <= -185


# SETUP WINDOW
window = turtle.Screen()
window.title("Final Project")
window.bgcolor("black")
window.setup(800, 800)
window.tracer(0)

# DRAW HEADER
turtle.color("white")
turtle.penup()
turtle.goto(-400, 400)
turtle.pendown()
turtle.pencolor("white")
turtle.begin_fill()
for _ in range(2):
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
turtle.end_fill()

# DRAW INVENTORY BORDERS
layout_pen = get_turtle("white")
layout_pen.hideturtle()

layout_pen.goto(-400, -190)
layout_pen.pendown()
layout_pen.forward(250)
layout_pen.right(90)
layout_pen.forward(210)
layout_pen.penup()

# SET DIFFICULTY
DIFFICULTY = int(window.numinput("Difficulty", "Choose difficulty level (an integer from 1 to 5)",
                                 default=1, minval=1, maxval=5))

# CONSTANTS
ENEMY_ATTACK = 15 + DIFFICULTY * 5
ENEMY_DEFENSE = 15 + DIFFICULTY * 5
ENEMY_HEALTH = 80 + DIFFICULTY * 10

NUMBER_OF_ENEMIES = DIFFICULTY * 10
NUMBER_OF_LOOT_ITEMS = DIFFICULTY * 40

ALLOWED_CHARACTERISTICS_POINTS = 20 + DIFFICULTY * 4

DIFFICULTY_BUFFER = DIFFICULTY * .01
LOOT_TYPES_TO_CHANCES = {
    "Armor": 0.06 - DIFFICULTY_BUFFER,
    "Health Potions": 0.11 - DIFFICULTY_BUFFER,
    "Protein Shakes": 0.04 - DIFFICULTY_BUFFER,
    "Agility Potions": 0.03 - DIFFICULTY_BUFFER,
    "Lumps of Clay": 0.79 + DIFFICULTY_BUFFER
}

SPEED = .5 + .2 * DIFFICULTY

# GAME STATE
LIVES = 3
SCORE = 0
INVENTORY = {
    "Armor": [0, "orange"],
    "Health Potions": [0, "green"],
    "Protein Shakes": [0, "pink"],
    "Agility Potions": [0, "blue"],
    "Lumps of Clay": [0, "gray"]
}


# CUSTOMIZE THE HERO
def query_hero_characteristics(error_message=None):
    """
    Asks the user to distribute characteristics points. If there is an error in the input,
    then the function shows it description in the pop up and recursively asks the user again.
    This is repeated until the input satisfies the following conditions:
    * There are 4 numbers separated by spaces.
    * Their sum is equal to the number of ALLOWED_CHARACTERISTICS_POINTS, which is defined
      by the difficulty level.

    Args:
        error_message (str) -- the error message to append to the main prompt

    Returns:
        tuple: parsed characteristics values in the following order:
               Intelligence, Stamina, Strength, Agility
    """
    global ALLOWED_CHARACTERISTICS_POINTS
    prompt = (f"Please distribute {ALLOWED_CHARACTERISTICS_POINTS} stats across 4 characteristics: Intelligence, "
              "Stamina, Strength, Agility.\nYou must input your characteristic values as numbers separated by spaces.\n"
              "The numbers must come in the order given before.\nTheir sum must be equal "
              f"to {ALLOWED_CHARACTERISTICS_POINTS}.")
    if error_message:
        prompt += f"\n\nError: {error_message}!"
    raw_characteristics = window.textinput("Your characteristics", prompt)
    if not raw_characteristics:
        return query_hero_characteristics(error_message)
    validation_result, error_message = are_hero_characteristics_valid(raw_characteristics)
    if not validation_result:
        return query_hero_characteristics(error_message)
    characteristics_validated = raw_characteristics
    return parse_characteristics(characteristics_validated.split())


def are_hero_characteristics_valid(user_input):
    """
    Validates the characteristics values provided by the user.
    Checks whether the input satisfies the following conditions:
    * There are 4 numbers separated by spaces.
    * Their sum is equal to the number of ALLOWED_CHARACTERISTICS_POINTS, which is defined
      by the difficulty level.

    Args:
        user_input (str) -- the user input to validate

    Returns:
        tuple: the result of the validation (True or False) and an error message, if any
    """
    raw_characteristics = user_input.split()
    if len(raw_characteristics) != 4:
        return False, "4 numbers must be provided"
    if any([not x.isdigit() for x in raw_characteristics]):
        return False, "Your input must consist of 4 numbers separated by spaces"
    global ALLOWED_CHARACTERISTICS_POINTS
    characteristics = parse_characteristics(raw_characteristics)
    characteristics_sum = sum(characteristics)
    if characteristics_sum != ALLOWED_CHARACTERISTICS_POINTS:
        comparison_operator = 'less' if characteristics_sum < ALLOWED_CHARACTERISTICS_POINTS else 'greater'
        return False, f"The sum of the given values is {comparison_operator} than the allowed value"
    return True, None


def parse_characteristics(raw_characteristics):
    """
    Parses the characteristics values provided by the user
    into a list of integers.

    Args:
        raw_characteristics (str) -- the input to parse

    Returns:
        list[int]: the parsed characteristics values
    """
    return list(map(int, raw_characteristics))


INTELLIGENCE, STAMINA, STRENGTH, AGILITY = query_hero_characteristics()

DEFAULT_HEALTH = 100 + STAMINA * 10
HEALTH = DEFAULT_HEALTH

DEFAULT_ATTACK = 20 + STRENGTH * 2
ATTACK = DEFAULT_ATTACK

DEFAULT_DEFENSE = 20 + INTELLIGENCE * 2
DEFENSE = DEFAULT_DEFENSE

DEFAULT_CRITICAL_CHANCE = .1 + AGILITY * .05
CRITICAL_CHANCE = DEFAULT_CRITICAL_CHANCE

# DRAW PACMAN
pacman = get_turtle("yellow", "circle")
pacman.direction = "stop"


def move():
    """
    Updates the coordinates of the hero according to its direction.
    """
    x, y = pacman.xcor(), pacman.ycor()
    if pacman.direction == "up":
        y += SPEED
    if pacman.direction == "down":
        y -= SPEED
    if pacman.direction == "left":
        x -= SPEED
    if pacman.direction == "right":
        x += SPEED
    pacman.setposition(x, y)


def move_up():
    """
    Sets the direction of the hero to 'up'
    """
    pacman.direction = "up"


def move_down():
    """
    Sets the direction of the hero to 'down'
    """
    pacman.direction = "down"


def move_left():
    """
    Sets the direction of the hero to 'left'
    """
    pacman.direction = "left"


def move_right():
    """
    Sets the direction of the hero to 'right'
    """
    pacman.direction = "right"


def reset_characteristics():
    """
    Resets the hero characteristics to the initial values.
    Used when the hero dies.
    """
    global HEALTH, DEFAULT_HEALTH, ATTACK, DEFAULT_ATTACK
    global DEFENSE, DEFAULT_DEFENSE, CRITICAL_CHANCE, DEFAULT_CRITICAL_CHANCE
    HEALTH, ATTACK, DEFENSE, CRITICAL_CHANCE = DEFAULT_HEALTH, DEFAULT_ATTACK, DEFAULT_DEFENSE, DEFAULT_CRITICAL_CHANCE


def reset_inventory():
    """
    Empties the inventory. Used when the hero dies.
    """
    global INVENTORY
    INVENTORY = {item: [0, color] for item, [_, color] in INVENTORY.items()}


def die():
    """
    Updates the state of the game when the hero dies:
    * Decrements the number of lives
    * Resets the hero characteristics
    * Empties the inventory
    Moves the hero to its initial position and stops it.
    """
    global LIVES
    LIVES -= 1
    reset_characteristics()
    reset_inventory()
    time.sleep(0.5)
    pacman.goto(0, 0)
    pacman.direction = "stop"


# DRAW INVENTORY
inventory_pen = get_turtle("white")
inventory_pen.hideturtle()


def show_inventory():
    """
    Clears the current content of the inventory area, if any,
    and draws the up-to-date values
    """
    inventory_pen.clear()
    inventory_pen.goto(-395, -225)
    for item, (quantity, color) in INVENTORY.items():
        inventory_pen.color(color)
        inventory_pen.write(f"{item}: {quantity}", font=("Courier", 16, "normal"))
        inventory_pen.goto(inventory_pen.xcor(), inventory_pen.ycor() - 40)


show_inventory()

# DRAW LOOT ITEMS
loot_items = []
used_loot_items = []
for _ in range(NUMBER_OF_LOOT_ITEMS):
    loot_item = get_turtle("white")
    loot_item.hideturtle()
    set_random_coordinates(loot_item)
    loot_item.write("?", align="center", font=("Courier", 16, "normal"))
    loot_items.append(loot_item)


def pick(loot_item):
    """
    Chooses the type of the given loot item according to the chances
    depending on the difficulty level. Hides the question mark
    representing the item, updates the color of the turtle.Turtle,
    increments the quantity of such items in the inventory, and
    shows the hero's reaction to the item

    Args:
        loot_item (turtle.Turtle) -- the loot item to pick up
    """
    item_type = random.choices(list(LOOT_TYPES_TO_CHANCES.keys()),
                               weights=list(LOOT_TYPES_TO_CHANCES.values()))[0]
    loot_item.clear()
    loot_item.color(INVENTORY[item_type][1])
    INVENTORY[item_type][0] += 1
    react(item_type, loot_item)


def react(item_type, loot_item):
    """
    Updates the characteristics of the hero and writes their reaction to it
    in the screen, depending on the type of the given loot item

    Args:
        item_type (str) -- the type of the loot item
        loot_item (turtle.Turtle) -- the loot item itself
    """
    global DEFENSE, HEALTH, ATTACK, CRITICAL_CHANCE
    if item_type == "Armor":
        DEFENSE += 2
        loot_item.write(f"Armor! Defense +2 -> {DEFENSE}")
    elif item_type == "Health Potions":
        HEALTH += 10
        loot_item.write(f"Health Potion! Health +10 -> {HEALTH}")
    elif item_type == "Protein Shakes":
        ATTACK += 5
        loot_item.write(f"Protein Shake! Attack +5 -> {ATTACK}")
    elif item_type == "Agility Potions":
        CRITICAL_CHANCE += .05
        loot_item.write(f"Agility Potion! Critical Chance +0.05 -> {CRITICAL_CHANCE}")
    else:
        loot_item.write("Ugh... It's a Lump of Clay")


def clean_up_used_loot():
    """
    When a loot item is picked up, it is removed from the list of the active items
    and added to the list of the used ones. Used loot has a default lifetime of 500 window updates.
    At each update, lifetimes of the used items are decremented. When a lifetime reaches zero,
    the related loot item is cleaned up from the game field.
    """
    for used_loot_item_data in used_loot_items:
        used_loot_item_data[1] -= 1
        used_loot_item, lifetime = used_loot_item_data
        if lifetime == 0:
            used_loot_items.remove(used_loot_item_data)
            used_loot_item.clear()


# DRAW ENEMIES
enemies = []
for _ in range(NUMBER_OF_ENEMIES):
    enemy = get_turtle("red", "turtle")
    set_random_coordinates(enemy)
    x_dir, y_dir = random.sample((0, 1, -1), 2)  # This is required so that enemies move in different directions
    enemies.append([enemy, x_dir, y_dir, ENEMY_HEALTH])  # Contains the turtle itself, its direction, and health points


def enemy_move():
    """
    Moves all alive enemies in the game field according to their directions.
    """
    for enemy, x_dir, y_dir, _ in enemies:
        x, y = enemy.xcor(), enemy.ycor()
        x += SPEED * x_dir
        y += SPEED * y_dir
        enemy.setposition(x, y)


def fight(enemy_data):
    """
    Allows the hero to fight an encountered enemy. At every turn,
    the user is asked to choose whether to defend or to attack the enemy.
    Then, the program randomly chooses the action of the enemy.
    Depending on the results, the function decreases the health points of
    the hero and the enemy. If the user decides to defend and the hero's
    defense is greater than the enemy's attack, the hero gains the diff
    as additional health points.

    Args:
        enemy_data (tuple) -- the parameters of the current enemy
    """
    global HEALTH
    enemy, _, _, enemy_health = enemy_data
    hero_action = enemy_action = None
    while enemy_health > 0 and HEALTH > 0:
        hero_action = query_hero_action(enemy_health, hero_action, enemy_action)
        enemy_action = random.choice(["defend", "attack"])
        if hero_action == "defend" and enemy_action == "attack":
            HEALTH += ENEMY_ATTACK - DEFENSE  # If defense is greater than attack, then health increases
        if hero_action == "attack":
            critical = 2 if random.random() <= CRITICAL_CHANCE else 1
            enemy_health -= ATTACK * critical
            if enemy_action == "defend":
                enemy_health += ENEMY_DEFENSE
            elif enemy_action == "attack":
                HEALTH -= ENEMY_ATTACK
            enemy_data[3] = enemy_health
    window.listen()


def query_hero_action(enemy_health, prev_hero_action=None, prev_enemy_action=None):
    """
    Asks the user to choose whether to fight or to attack the enemy. The pop-up is shown
    until the user inputs a correct option. The allowed options are 'attack' and 'defend'.
    The input is case-insensitive.

    Args:
        enemy_health (int) -- the remaining health of the current enemy
        prev_hero_action (str, default None) -- the action performed by the hero in the previous round
        prev_enemy_action (str, default None) -- the action performed by the enemy the previous round

    Returns:
        str: the accepted and validated hero action
    """
    hero_action = None
    while not hero_action:
        prompt = f"Your health: {HEALTH}. Enemy health: {enemy_health}. Attack or defend?"
        if prev_hero_action and prev_enemy_action:
            prev_data = f"\n\nIn the previous round, you {prev_hero_action}ed and your enemy {prev_enemy_action}ed."
            prompt += prev_data
        user_action = window.textinput("Choose what to do!", prompt)
        if not user_action or user_action.lower() not in ["defend", "attack"]:
            continue
        hero_action = user_action.lower()
    return hero_action


# DRAW STATS
pen = get_turtle("blue")
pen.hideturtle()
pen.goto(-80, 345)


def write_stats():
    """
    Uses the 'pen' turtle.Turtle to update the stats dashboard
    """
    pen.clear()
    pen.write(f"Score: {SCORE}  Lives: {LIVES}", align="center", font=("Courier", 36, "normal"))


write_stats()


# DRAW EXIT BUTTON
def click_exit(x, y):
    """
    Checks whether the user clicked in the exit button area. If so, closes the game.
    """
    if 225 <= x <= 385 and 345 <= y <= 400:
        turtle.bye()


button = get_turtle("red")
button.hideturtle()
button.goto(300, 345)
button.write("Exit", align="center", font=("Courier", 36, "normal"))

window.listen()
window.onscreenclick(click_exit)
window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")

while loot_items and LIVES > 0:  # As long as there is something to collect and there are lives left
    window.update()  # Update the screen

    write_stats()  # Update the stats
    clean_up_used_loot()  # Remove used loot

    if is_out_of_borders(pacman):  # If the hero leaves the allowed area, they die
        die()

    for loot_item in loot_items:  # Check whether the hero is close to any of the loot items
        if pacman.distance(
                loot_item) < 10:  # If they are, increment the score, update the inventory, move the item to used
            SCORE += 1
            pick(loot_item)
            show_inventory()
            loot_items.remove(loot_item)
            used_loot_items.append([loot_item, 500])

    for enemy_data in enemies:
        enemy, x_dir, y_dir, enemy_health = enemy_data
        if is_out_of_borders(enemy):  # If an enemy leaves the allowed area, flip its direction
            enemy_data[1], enemy_data[2] = x_dir * -1, y_dir * -1
        if pacman.distance(enemy) < 10:  # If the hero is close to an enemy, start a fight
            fight(enemy_data)
            if HEALTH == 0:  # Depending on the result of the fight, either the hero dies
                die()
            else:
                SCORE += 5  # ...or the enemy
                enemy.hideturtle()
                enemies.remove(enemy_data)

    move()
    enemy_move()

# WHEN THE GAME IS FINISHED
window.clear()
window.bgcolor("white")
pen.goto(0, pen.ycor())
pen.pendown()
write_stats()
pen.penup()
pen.goto(-30, 0)
pen.pendown()
pen.write(f"You {'won' if not loot_items else 'lost'}!", align="center", font=("Courier", 60, "normal"))
window.onclick(lambda x, y: turtle.bye())  # Wait for a click to close the window
window.mainloop()
