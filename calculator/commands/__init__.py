"""
Calculator REPL Module

This module implements a simple calculator with a Read-Eval-Print Loop (REPL) interface.
It supports basic arithmetic operations, including addition, subtraction, multiplication,
and division. Commands are handled dynamically through a command handler system """

import os
import sys
import logging
from dotenv import load_dotenv, dotenv_values
from calculator.plugins.addition import AdditionCommand
from calculator.plugins.substraction import SubtractionCommand
from calculator.plugins.multiplication import MultiplicationCommand
from calculator.plugins.division import DivisionCommand
from calculator.plugins.menu_command import MenuCommand
from calculator.commands.command_handler import CommandHandler

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Load environment variables
load_dotenv()
env_vars = dotenv_values(".env")  # Loads all variables as a dictionary

# Debugging environment variables
logging.basicConfig(
    level=logging.DEBUG,  # Set to DEBUG for detailed logs
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/calculator.log"),
        logging.StreamHandler()
    ]
)

logging.info("Loaded environment variables.")
logging.debug("Environment Variables: %s", env_vars)
logging.info("my_secret_key: %s", os.getenv('my_secret_key'))
logging.info("Host: %s, Port: %s", os.getenv('Host'), os.getenv('Port'))

def start():
    """Start the calculator REPL with logging and error handling."""
    command_handler = CommandHandler()

    # Register commands with validation to avoid duplicates
    commands = {
        "add": AdditionCommand(),
        "subtract": SubtractionCommand(),
        "multiply": MultiplicationCommand(),
        "divide": DivisionCommand(),
        "menu": MenuCommand()
    }

    for name, cmd in commands.items():
        if name not in command_handler.commands:
            command_handler.register_command(name, cmd)
            logging.info("Registered command: %s", name)
        else:
            logging.warning("Command '%s' is already registered.", name)

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

            logging.info("Executing command: %s", command)
            command_handler.execute_command(command)

        except KeyboardInterrupt:
            logging.info("Calculator exited via keyboard interrupt.")
            print("\n >> Goodbye!")
            break
        except KeyError:
            logging.warning("Unknown command: %s", command)
            print(f"Command not found: {command}")
        except ImportError as e:
            logging.error("Module import error: %s", e, exc_info=True)
            print(f"Module import error: {e}")
        except Exception as e: # pylint: disable=broad-exception-caught
            logging.critical("Unexpected error: %s", e, exc_info=True)
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    start()
