import streamlit as st
from simulation import run_simulation

st.title("Distributed Deadlock Detection Simulation")

num_processes = st.slider("Number of Processes",2,10,5)

if st.button("Run Random Simulation"):

    deadlock, cycle = run_simulation(num_processes)

    if deadlock:
        st.error("Deadlock Detected!")
        st.write(cycle)
    else:
        st.success("No Deadlock Detected")

if st.button("Force Deadlock Scenario"):

    deadlock, cycle = run_simulation(num_processes, force_deadlock=True)

    st.error("Deadlock Detected!")
    st.write(cycle)
