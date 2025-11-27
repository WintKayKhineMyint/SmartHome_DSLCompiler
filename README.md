# SmartHome_DSLCompiler
A Domain-Specific Language and Visualization System for Smart Home Automation

# Overview
This project implements a Domain-Specific Language (DSL) for defining smart-home automation rules and a compiler that converts this DSL into executable Python automation logic.

The project demonstrates:
* Compiler components (lexer->parser->sementic analyzer-> code generator)
* DSL design
* Automation logic
* Real-time visualization using HTML + JSON

## Project Structure
```
SmartHome/
│
├── rules.smarthome        # DSL file containing smart-home rules
├── run.py                 # Python automation engine generated from DSL
├── devices.json           # State output file read by the dashboard
├── dashboard.html         # Real-time visualization
├── README.md              # Project documentation
```
## How System Works

1. DSL Input (rules.smarthome)
   - User writes the automation rules such as:
     ```
       when time >= 17:00
        turn_on led_light
        turn_on speaker
     ```

     You degine:
     * Events
     * Time conditions
     * Device Actions
     * Automation routines

2. Compiler Pipeline
   The compiler follows 4 main phases:
     + Lexical Analysis
     + Syntax Analysis
     + Sematic Analysis
     + Code Generation

3. Python Automation Engine
   The generated engine
      + Stores all device states
      + Evaluates rules through execute (event,time)
      + Update devices.json
      + Demonstrates for testing.

4. Real-Time Visualization
   The dashboard:
        + Reads devices.json
        + Shows device icons
        + Displays ON/OFF, locked/unlocked states
        + Lights glow when ON
      - This provides a live simulation of smart-home routines

Supported Devices: led_light, door, tv, fan, thermostat, oven, washer

## How to Run the Project 

1. Open the project folder SmartHome/
2. Run the automation engine "python3 run.py"
3. See the live view in dashboad.html
  
## Technology Used
+ Custom DSL - .smarthome
+ Frontend   -  HTML, CSS
+ Backend    - Python
