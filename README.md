# CS440_Assign1
Vacuum_world

# Vacuum World 2x2 Environment

This project extends the classic Vacuum World problem to a 2x2 grid environment. The environment and agent models have been updated to accommodate this new setup, and four different types of agents have been implemented and tested: Random Agent, Table-Driven Agent, Simple Reflex Agent, and Model-Based Reflex Agent.

- Move from Python 3.5 to 3.7.
- More emphasis on Jupyter (Ipython) notebooks.
- More projects using external packages (tensorflow, etc.).



# Setup
Prerequisites

Ensure that Python is installed on your machine. You may also need to install some dependencies. All required packages are listed in the requirements.txt file.
Installation

1. Clone the repository:
```
https://github.com/aimacode/aima-python.git
cd aima-python
```
2. Set up a virtual environment and install dependencies:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Also install ipykernel:
```
python3 -m pip install ipykernel -U --force-reinstall
python3 -m ipykernel --version
```

note: 
- Check to make sure that you are in the correct environment. 
- Restart vsCode

## Environment Description
The environment is now a 2x2 grid, represented as follows:
# 2x2 grid environment

Change the environment to: 
```
loc_A, loc_B = (0, 1), (1, 0)
```

note: 0 = clean, 1 = dirty

Location A is now at top right, while location B remains at bottom left corner in our new 2x2 environment. 

Agent Descriptions
1. Random Agent

The RandomVacuumAgent selects actions randomly from the possible moves ('Up', 'Down', 'Left', 'Right', 'Suck', 'NoOp').

We added 'Up', and 'Down' commands. 

2. Table-Driven Agent

The TableDrivenVacuumAgent uses a predefined percept-action table that includes all possible states for a 2x2 grid.
3. Simple Reflex Agent

The SimpleReflexVacuumAgent acts based on condition-action rules:

    Cleans a dirty cell.
    Moves to adjacent cells according to a fixed sequence.

4. Model-Based Reflex Agent

The ModelBasedReflexAgent maintains an internal model of the environment and updates it based on percepts. It chooses actions to clean all dirty cells efficiently.
