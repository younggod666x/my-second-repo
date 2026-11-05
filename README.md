# Simple Battle Simulator

This is a basic Python battle simulation in which a heroic Knight fights a Goblin and an Orc. The game demonstrates object-oriented programming principles such as classes, methods, and interaction between objects.

## File Structure

- `character.py`: Defines the `Character` class with attributes and methods for combat.
- `main.py`: Runs the battle simulation using three instances of `Character`.

## Character Class

Located in `character.py`, the `Character` class includes:

### Attributes
- `name` (str): The character's name.
- `hp` (int): Hit points (health).
- `attack_power` (int): Initial attack power. Each attack deals a random 30% to 90% of this value.

### Methods
- `attack(other)`: Reduces the `other` character's HP by a random amount between 30% and 90% of the attacker's initial attack power, then prints an attack message.
- `is_alive()`: Returns `True` if HP is greater than 0.
- `__str__()`: Returns a string representation of the character's current HP.

##  How the Battle Works

The battle logic in `main.py` follows these steps:

1. Create three characters: Knight, Goblin, and Orc.
2. Print their initial stats.
3. The Knight attacks each living enemy; each enemy that survives attacks back.
4. Repeat while the Knight and at least one enemy are alive, printing updated stats.
5. Declare the winner when the Knight or both enemies are defeated.

##  Running the Game

To run the simulation, execute `main.py`:

```bash
python main.py
```
