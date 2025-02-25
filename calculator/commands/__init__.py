"""
Start the calculator REPL (Read-Eval-Print Loop).

This function initializes the CommandHandler and registers available commands 
such as addition, subtraction, multiplication, division, and menu display.
"""

# Import necessary modules
import sys
from calculator.plugins.addition import AdditionCommand
from calculator.plugins.substraction import SubtractionCommand
from calculator.plugins.multiplication import MultiplicationCommand
from calculator.plugins.division import DivisionCommand
from calculator.plugins.menu_command import MenuCommand
from calculator.commands.command_handler import CommandHandler

def start():
    """Start the calculator REPL"""
    command_handler = CommandHandler()  # Use the imported CommandHandler

    # Register commands
    command_handler.register_command("add", AdditionCommand())
    command_handler.register_command("subtract", SubtractionCommand())
    command_handler.register_command("multiply", MultiplicationCommand())
    command_handler.register_command("divide", DivisionCommand())
    command_handler.register_command("menu", MenuCommand())

    print("\nWelcome to Calculator!")
    print("Type 'help' for available commands or 'exit' to quit.")
    MenuCommand().execute()

    while True:
        try:
            command = input("calculator> ").strip()
            command_handler.execute_command(command)
        except KeyboardInterrupt:
            print("\n >> Goodbye!")
            break
        except KeyError as e:
            print(f"Command not found: {e}")
        except (ImportError, AttributeError) as e:
            print(f"Module or command error: {e}")
