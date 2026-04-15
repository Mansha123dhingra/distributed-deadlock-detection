import simpy
import random
from deadlock_detection import WaitForGraph

def run_simulation(num_processes, force_deadlock=False):

    env = simpy.Environment()
    wfg = WaitForGraph()

    processes = [f"P{i}" for i in range(num_processes)]

    if force_deadlock:
        # create guaranteed cycle
        for i in range(len(processes)):
            p1 = processes[i]
            p2 = processes[(i+1) % len(processes)]
            wfg.add_edge(p1, p2)

    else:
        # random relationships
        for _ in range(num_processes):
            p1 = random.choice(processes)
            p2 = random.choice(processes)

            if p1 != p2:
                wfg.add_edge(p1, p2)

    env.run(until=5)

    deadlock, cycle = wfg.detect_deadlock()

    return deadlock, cycle
