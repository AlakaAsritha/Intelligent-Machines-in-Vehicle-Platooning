# Intelligent Machines in Vehicle Platooning 
### Python-Based Simulation of Vehicular Communication Protocols

This project presents a Python-based simulation framework for analyzing intelligent vehicle platooning using multiple vehicular communication protocols. The goal is to evaluate how different protocols affect platoon performance in terms of latency, reliability, and network efficiency.



## Project Overview

Vehicle platooning is a driving strategy where multiple vehicles travel closely together using automated control and communication technologies. This project simulates such platoons and evaluates the effectiveness of different communication protocols used for vehicle-to-vehicle interactions.

The system focuses on protocol-level analysis rather than hardware deployment and provides graphical visualizations for comparative study.



## Objectives

- Evaluate and compare vehicular communication protocols:
  - C-V2X
  - URLLC
  - GRP
  - GPSR
- Analyze performance metrics such as:
  - Communication latency
  - Reliability
  - Network efficiency
- Visualize platooning behavior and protocol performance
- Provide a scalable Python-based simulation environment for research and learning



## Communication Protocols Used

- **C-V2X (Cellular Vehicle-to-Everything):**  
  Enables vehicles to communicate with other vehicles and infrastructure using cellular networks.

- **URLLC (Ultra-Reliable Low-Latency Communication):**  
  Designed for safety-critical applications requiring extremely low delay and high reliability.

- **GRP (Geographic Routing Protocol):**  
  Uses vehicle position and geographic data to optimize data routing within platoons.

- **GPSR (Greedy Perimeter Stateless Routing):**  
  A location-based routing protocol that selects optimal packet forwarding paths.


## System Features

- Python-based simulation of vehicle platooning scenarios
- Configurable simulation parameters:
  - Number of vehicles
  - Communication range
  - Driving behavior models
- Performance metric calculation:
  - Latency
  - Packet delivery ratio
  - Reliability
- Graph-based visualization of:
  - Vehicle positions
  - Communication links
  - Protocol comparisons
- Scalable design supporting small and large simulations



## Technologies Used

- Python 3.x
- NumPy
- Matplotlib
- Graph-based visualization techniques



## Operating Environment

- Runs on Windows, macOS, and Linux
- Can be executed using:
  - Command Line Interface (CLI)
  - Jupyter Notebook
  - IDEs like PyCharm or VS Code
- No graphical user interface (GUI); interaction is script-based



## Intended Users

- Researchers and academicians in intelligent transportation systems
- Transportation and automotive engineers
- Undergraduate and postgraduate students
- Developers interested in vehicular network simulations
- Policy makers and industry stakeholders exploring platooning concepts



## Visualization & Results

The project includes visual representations of:
- Vehicle platooning behavior under different protocols
- Protocol-wise comparisons of:
  - Average latency
  - Reliability
  - Network efficiency

These visualizations help in understanding protocol strengths and weaknesses.



## Limitations

- Simulation-based analysis only (no real-world deployment)
- Accuracy depends on modeling assumptions
- No graphical user interface
- Performance depends on system hardware for large simulations


## Conclusion

This project demonstrates how intelligent communication protocols influence vehicle platooning performance. By using a Python-based simulation framework, it provides valuable insights into protocol behavior and serves as a strong foundation for future research in autonomous vehicles and intelligent transportation systems.


## License

This project is developed for academic and research purposes.
