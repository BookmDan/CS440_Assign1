# CS440_Assign1
Vacuum_world

# Vacuum World 2x2 Environment

This project extends the classic Vacuum World problem to a 2x2 grid environment. The environment and agent models have been updated to accommodate this new setup, and four different types of agents have been implemented and tested: Random Agent, Table-Driven Agent, Simple Reflex Agent, and Model-Based Reflex Agent.

# Setup
Prerequisites (for Mac)

Ensure that Python is installed on your machine. You may also need to install some dependencies. All required packages are listed in the requirements.txt file.
Installation

1. Fork and Clone the repository:
```
https://github.com/aimacode/aima-python.git
cd aima-python
```
2. Set up a virtual environment and install dependencies:
*note: running these commands in terminal rather than vscode terminal seems to work better. 
Also, restart VScode if certain packages like ipykernel or numpy don't seem to be installed even though already installed. 
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
*note: make sure running the python environment in this virtual
It should like this in the upper right corner of the vscode: 
<img width="389" alt="Screenshot 2024-08-28 at 12 20 59 PM" src="https://github.com/user-attachments/assets/d09fc2f4-6b06-4661-b382-dd3303737569">

3. Also install ipykernel:
```
python3 -m pip install ipykernel -U --force-reinstall
python3 -m ipykernel --version
```

note: 
- Run commands in terminal outside of VSCode.
- Check to make sure that you are in the correct environment.
- Restart VSCode if needed to update installed packages. 

# Project Structure
The **agents.py** file contains the AI agent implementations, while the **vacuum_world.py** file models the 2x2 grid environment via Jupyter notebook. 

# Environment Description
The environment is now a 2x2 grid, represented as follows:

## 2x2 grid environment - agents.py

Change the environment to: 
```
loc_A, loc_B = (0, 0), (0,1)
loc_C, loc_D = (1,0), (1, 1)
```

note: '0' = clean, '1' = dirty

Location A is now at top left, B is top right. 
Location C is bottom left, and D is bottom right.

Agent Descriptions
1. Random Agent

The RandomVacuumAgent selects actions randomly from the possible moves ('Up', 'Down', 'Left', 'Right', 'Suck', 'NoOp').

    We added 'Up', and 'Down' commands, to be able to move in all diretion in a 2 x 2 environment.

2. Table-Driven Agent

    The TableDrivenVacuumAgent uses a predefined percept-action table that includes all possible states for a 2x2 grid, up to 2 percepts. 
    We decided to go with up to 2 percepts as this is a simple demonstration assignment. 

3. Simple Reflex Agent

The SimpleReflexVacuumAgent acts based on condition-action rules:

    Cleans a dirty cell.
    Moves to adjacent cells according to a fixed sequence, which we determined would be a clockwise motion i.e. A -> B -> D -> C. 

4. Model-Based Reflex Agent

The ModelBasedReflexAgent will attempt to clean its cell if it is dirty. If its adjacent cell is dirty, it will move to it to clean it.  The agent maintains an internal model of the environment and updates it based on percepts. It chooses actions to clean all dirty cells efficiently.

# Acknowledgements
We used https://github.com/aimacode/aima-python as a starting reference point. 
