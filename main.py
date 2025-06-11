from characters import Warrior, Mage, Archer, Paladin, EvilWizard
import time  

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    class_map = {
        '1': Warrior,
        '2': Mage,
        '3': Archer,
        '4': Paladin
    }

    while True:
        class_choice = input("Enter the number of your class choice: ").strip()
        if class_choice in class_map:
            selected_class = class_map[class_choice]
            character_name = selected_class.__name__
            print(f"✅ You have selected: {character_name}")
            return selected_class(character_name)
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")


def battle(player, wizard):
    turns = 0
    total_damage_dealt = 0
    total_damage_taken = 0

    while player.health > 0 and wizard.health > 0:
        print("\n" + "=" * 40)
        print(f"Turn {turns + 1}")
        print("=" * 40)
        turns += 1
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal / Defend / Evade")
        print("4. View Stats")

        print("\nYour Turn")
        choice = input("Choose an action: ").strip()
        print()

        if choice == '1':
            before = wizard.health
            player.attack(wizard)
            total_damage_dealt += max(0, before - wizard.health)
        elif choice == '2':
            before = wizard.health
            player.special_ability(wizard)
            total_damage_dealt += max(0, before - wizard.health)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
            wizard.display_stats()
            continue
        else:
            print("Invalid choice, you skip your turn!\n")

        # Wizard's turn: only attack if player still alive
        if wizard.health > 0 and player.health > 0:
            input("\nPress Enter for the Wizard's Turn...")
            print("\nWizard's Turn")
            wizard.regenerate()
            before = player.health
            wizard.attack(player)
            total_damage_taken += max(0, before - player.health)

    # Move victory/defeat message here after battle ends
    if player.health <= 0:
        print(f"\n{player.name} has been defeated! Game Over.\n")
    elif wizard.health <= 0:
        print(f"\nThe Evil Wizard has been defeated!")
        print(f"{player.name} is victorious!\n")

    print("- Battle Summary -")
    print(f"Character: {player.name}")
    print(f"Turns survived: {turns}")
    print(f"Total damage dealt to the wizard: {total_damage_dealt}")
    print(f"Total damage taken: {total_damage_taken}")


def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
