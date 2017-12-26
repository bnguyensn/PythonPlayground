import sys, os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import ta.modules.dungeon as dungeon
import ta.modules.cli as cli


def program():
    d = dungeon.create_new_dungeon(10, 10)
    print('')
    cli.start_taking_input(d.player)


program()
