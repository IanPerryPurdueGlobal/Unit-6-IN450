Dressing Room Simulation

This project simulates customers using dressing rooms in a store. Each customer runs in its own thread, waits for an available room, tries on items, and reports usage and wait times. The simulation tracks metrics such as utilization, throughput, and efficiency.

How It Works
- Customer threads request a dressing room, try on items, and record metrics.
- DressingRoom manages room availability using a semaphore and stores all metrics.
- Scenario runs a full simulation with a chosen number of rooms, customers, and items.
- main.py allows you to run multiple scenarios in a loop until you type exit.

Running the Program
Run: python main.py

You will be prompted for:
- Number of rooms (type exit to quit)
- Number of customers
- Number of items (0 = random, otherwise 1–6)

Each run is labeled as a new scenario.

Input Rules
- Rooms must be ≥ 1
- Customers must be ≥ 1
- Items must be 0–6
- Typing exit at the first prompt ends the program

Output
Each scenario prints:
- Utilization
- Throughput
- Efficiency
- Average items
- Average usage time
- Average wait time
- Total elapsed time
