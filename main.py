from character import Character

def main():
    hero = Character("Knight", 30, 5)
    enemies = [
        Character("Goblin", 20, 3),
        Character("Orc", 25, 4),
    ]

    print(hero)
    for enemy in enemies:
        print(enemy)
    print()

    while hero.is_alive() and any(enemy.is_alive() for enemy in enemies):
        for enemy in enemies:
            if not hero.is_alive():
                break
            if enemy.is_alive():
                hero.attack(enemy)
                if enemy.is_alive():
                    enemy.attack(hero)
        print(hero)
        for enemy in enemies:
            print(enemy)
        print()

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        surviving_enemies = [enemy.name for enemy in enemies if enemy.is_alive()]
        winner_label = ", ".join(surviving_enemies)
        print(f"{winner_label} {'win' if len(surviving_enemies) > 1 else 'wins'}!")

if __name__ == "__main__":
    main()
