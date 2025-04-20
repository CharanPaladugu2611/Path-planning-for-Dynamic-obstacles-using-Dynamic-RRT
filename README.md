# 🧭 Dynamic Path Planning with RRT* in Dynamic Environments

Welcome to the repository for our ENPM661 Final Project, where we implemented a robust and dynamic path planning algorithm using Rapidly-exploring Random Trees (RRT*) that navigates complex environments filled with both static and dynamic obstacles. This project is inspired by the Dynamic RRT algorithm and incorporates real-time replanning and visualization of optimal paths.
<p align="left">
<img src="https://github.com/user-attachments/assets/93b3a905-0673-4875-a69c-ec91d8df9dc4" width="350" height="350">
<img src="https://github.com/user-attachments/assets/0d82fbf6-6c6f-40ec-8f0d-e0db93b75854" width="350" height="350">
</p>


## 📌Project Overview:
This implementation leverages:

* A customized RRT* algorithm enhanced for dynamic environments.
* Real-time detection and handling of obstacle collisions.
* 2D simulation with randomly generated rectangular and circular obstacles.
* Dynamic obstacle movement modeled using velocity vectors and rebound logic.
* Replanning upon collision with dynamic obstacles.<br/>


## 🛠️Technologies Used:


* Python 3
* NumPy
* OpenCV
* Matplotlib
* ImageIO
* Google Colab (for convenience)

## 🔍 Features:
* Dynamic Obstacles: Obstacles with randomly assigned speeds and movement directions.
* Collision Detection: Rechecks path validity and replans if a collision is detected.
* Rewiring and Optimization: Uses RRT* heuristics to optimize paths with rewiring.
* Efficient Sampling: Uniform random sampling with steering heuristics.

## 📈Results:
* Average Planning Time: ~12.5s over 400 runs
* Path Replanning: Occurs dynamically when an obstacle crosses the path
* Run-time Stability: Algorithm gracefully adapts to dynamic obstacle changes

## ✨Future Work:
* Integrate with ROS2 for real robot deployment (initial experiments done using Turtlebots).
* Add support for informed sampling.
* Explore machine learning-based sampling heuristics to improve convergence rates.
