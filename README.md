UAV Threat Detection and UGV Route Replanning Simulation

System Overview

This project simulates a simplified UAV–UGV collaborative system in a 2D
grid environment. The UAV generates threat detections and communicates
them to the UGV using a lightweight JSON message format. After receiving
the threat information, the UGV marks risk zones on its environment map
and computes a safe path from the start position to the goal using the
A* path planning algorithm.

The system is composed of four main modules:

-   Threat Generation: Simulates UAV detections with configurable false
    positive and false negative rates.
-   Communication Module: Serializes and transmits threat information
    using JSON messages.
-   Risk Mapping: Expands each detected threat into a configurable
    safety zone on the grid.
-   Path Planning: Computes a collision-free route while avoiding
    identified risk zones.

A graphical interface developed with Pygame visualizes the environment,
detected threats, planned route, and live movement of the UGV.

System Workflow

1.  The UAV generates synthetic threats classified as either Person or
    Vehicle.
2.  Each detection is converted into a JSON message and transmitted to
    the UGV.
3.  The UGV decodes the received messages and extracts the threat
    information.
4.  A safety radius is applied around every detected threat to create
    risk zones.
5.  The A* algorithm computes the safest available route from the start
    position to the destination.
6.  The planned path and robot movement are visualized in real time
    using Pygame.

Assumptions and Constraints

-   The environment is represented as a fixed 20 × 20 grid.
-   The UGV moves only in four directions (up, down, left, and right).
-   Threats remain stationary throughout a simulation.
-   Two threat classes are considered: Person and Vehicle.
-   Detection uncertainty is simulated using configurable False Positive
    and False Negative probabilities.
-   Every detected threat generates a circular safety region with a
    predefined radius.
-   Communication between the UAV and UGV is assumed to be reliable.

Threat Detection

Instead of using a real object detection model, the project generates
synthetic threat detections to create repeatable testing scenarios.

Each generated threat contains: - Threat ID - Threat class - Confidence
score - Grid coordinates - Timestamp

Detection uncertainty is simulated through: - False Negatives (FN):
Existing threats that are not detected. - False Positives (FP):
Incorrect detections that create unnecessary obstacles.

UAV–UGV Communication

Threat information is exchanged through lightweight JSON messages
containing: - threat_id - class - confidence - location - timestamp

The sender serializes each detection using json.dumps(), while the
receiver reconstructs the original data using json.loads().

Risk Zone Generation

After receiving threat messages, the UGV updates its environment by
creating safety zones around each detected threat. Each threat location
is expanded using a configurable radius, marking nearby cells as
hazardous. These risk zones are treated as obstacles during path
planning.

Path Planning

The navigation module implements the A* search algorithm using: -
Manhattan distance heuristic - Four-directional movement - Neighbor
validation - Path reconstruction - Obstacle and risk-zone avoidance

If no safe route exists, the planner reports that no valid path could be
found.

Visualization

The simulation is visualized using Pygame.

Green: Start Blue: Goal Red: Threats Orange: Risk zones Yellow: Planned
path Purple: UGV White: Free space

Evaluation Metrics

-   Path Length: Number of cells in the computed path.
-   Risk Zone Violation: Indicates whether the generated path enters a
    risk zone.

Test Plan

1.  No threats – shortest path generated.
2.  Single threat blocks the route – planner replans successfully.
3.  Multiple threats – planner avoids risk zones.
4.  False positive detection – unnecessary detour measured.
5.  False negative detection – risk-zone violation detected.
6.  Delayed message – planner updates after receiving threat data.
7.  Conflicting detections – deterministic conflict resolution.
8.  Stress test with multiple threats – acceptable execution time.

Key Findings

1.  A* generated efficient routes when no threats were present.
2.  Risk zones successfully redirected the UGV around hazardous areas.
3.  False positives increased path length.
4.  False negatives posed the greatest safety risk.
5.  The modular design supports future extensions.


