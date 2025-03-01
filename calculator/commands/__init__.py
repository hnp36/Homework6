import sys
import logging
import os
from calculator.plugins.addition import AdditionCommand
from calculator.plugins.substraction import SubtractionCommand
from calculator.plugins.multiplication import MultiplicationCommand
from calculator.plugins.division import DivisionCommand
from calculator.plugins.menu_command import MenuCommand
from calculator.commands.command_handler import CommandHandler

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Change to DEBUG for more details
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/calculator.log"),
        logging.StreamHandler()
    ]
)

def start():
    """Start the calculator REPL with logging"""
    command_handler = CommandHandler()  # Use the imported CommandHandler

    # Register commands
    command_handler.register_command("add", AdditionCommand())
    command_handler.register_command("subtract", SubtractionCommand())
    command_handler.register_command("multiply", MultiplicationCommand())
    command_handler.register_command("divide", DivisionCommand())
    command_handler.register_command("menu", MenuCommand())

    logging.info("Calculator REPL started.")
    print("\nWelcome to Calculator!")
    print("Type 'help' for available commands or 'exit' to quit.")
    MenuCommand().execute()

    while True:
        try:
            command = input("calculator> ").strip()
            if command.lower() == "exit":
                logging.info("User exited the calculator.")
                print("\n >> Goodbye!")
                break

            logging.info(f"Executing command: {command}")
            command_handler.execute_command(command)

        except KeyboardInterrupt:
            logging.info("Calculator exited via keyboard interrupt.")
            print("\n >> Goodbye!")
            break
        except KeyError as e:
            logging.warning(f"Unknown command: {command}")
            print(f"Command not found: {e}")
        except (ImportError, AttributeError) as e:
            logging.error(f"Module or command error: {e}", exc_info=True)
            print(f"Module or command error: {e}")
