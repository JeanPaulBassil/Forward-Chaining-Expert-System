# Forward Inference Expert System for Animal Identification

## Overview

This project implements a forward inference expert system for animal identification using the `pyknow` library in Python. Forward inference expert systems apply a set of rules to a known set of facts to infer new facts. They are widely used in fields like medical diagnosis, animal classification, and decision-making processes.

### What is a Forward Inference Expert System?

A forward inference expert system uses a collection of conditional rules to process data and deduce new information. It starts with a known set of facts and applies these rules to infer new facts, often used for classification or decision-making tasks.

### Project Description

This project's expert system classifies animals based on their characteristics, such as color, pattern, and physical features like teeth, claws, and wings. It is implemented in Python using the `pyknow` library, which is a Python implementation of the CLIPS expert system shell.

## Setup and Installation

### Prerequisites

- Python 3.6 or newer
- Pip (Python package manager)

### Installing Dependencies

1. **Install `pyknow`**:
   - Run `pip install pyknow` to install the `pyknow` library.

2. **Fixing the `pyknow` Library Issue**:
   - In Python 3.10, you might encounter an issue with the `frozendict` package used by `pyknow`.
   - To resolve this, modify the `frozendict` package's `__init__.py` file:
     - Locate the file in your Python's site-packages directory (commonly found at `~/.local/lib/python3.10/site-packages` or a similar path).
     - Change `from collections import Mapping` to `from collections.abc import Mapping`.

### Importing the Project

- Clone or download this project's repository to your local machine.

## Project Structure

- `animals.py`: Defines the `Animals` class, inheriting from `KnowledgeEngine`. Contains rules for animal identification.
- `main.py`: The entry point of the program. It creates an instance of `Animals`, declares facts, and runs the inference engine.


## How It Works

The system defines a set of rules in the `Animals` class. Each rule corresponds to an animal or a category (e.g., mammals, birds) and specifies the conditions under which the rule triggers. When facts are declared (e.g., an animal has sharp teeth, dark stripes), the system applies these rules to infer what animal it is.

## Running the Program

1. Navigate to the project directory.
2. Run `python3 main.py`.
3. The program will execute the defined rules based on the declared facts and output the classification results.


### Customization

Feel free to customize this template to better suit your project's specifics, including any additional setup steps, usage instructions, or contribution guidelines.