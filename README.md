# Distributed Deadlock Detection Simulation using Wait-For Graph

**Name:** Mansha  
**Registration Number:** 22MIC0162

## Project Description
This project implements a **Discrete Event Simulation of a Distributed Deadlock Detection Algorithm** using the **Wait-For Graph (WFG) model**. The simulation is built using **SimPy** to model process events and **Streamlit** to provide an interactive interface for running the simulation.

The system simulates multiple processes competing for shared resources across distributed sites. Each site maintains a **local Wait-For Graph**, and deadlocks are detected using a **cycle detection (edge-chasing/probe-based) approach**.

## Technologies Used
- Python
- SimPy
- Streamlit
- NetworkX

## System Components
1. **Processes** – Simulated using SimPy, representing distributed processes requesting resources.
2. **Resources** – Shared resources requested by processes.
3. **Wait-For Graph (WFG)** – Represents dependencies between processes waiting for resources.
4. **Deadlock Detection Algorithm** – Detects cycles in the Wait-For Graph.
5. **Streamlit Interface** – Allows users to run and visualize the simulation.

## How the Simulation Works
1. Processes request shared resources.
2. If a resource is unavailable, the process waits for the process holding it.
3. The Wait-For Graph is updated with edges representing waiting relationships.
4. The algorithm checks the graph for cycles.
5. If a cycle is found, a **deadlock is detected**.

Example of a deadlock cycle:

P1 → P2 → P3 → P1

This indicates that each process is waiting for another in the cycle, causing a deadlock.

## Running the Project

Install dependencies:
