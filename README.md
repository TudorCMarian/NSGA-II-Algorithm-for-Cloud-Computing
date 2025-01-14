# Cloud Computing Resources Optimization using NSGA-II Algorithm 

### Introduction 

We use NSGA-II to minimize costs and maximize task execution speed in a distributed network, generating efficient solutions for CPU, RAM, and storage allocation.

#### **Understanding the Problem and Objectives**

-   **Conflicting Objectives**:
    -   Minimize the total resource costs (CPU, RAM, Storage).
    -   Maximize task execution speed (minimize response time).
-   **Possible Constraints**:
    -   Available resources are limited.
    -   Tasks have specific requirements for CPU, RAM, and storage.

#### 2. **Problem Modeling**

-   **Solution Representation**:
    -   Each individual represents a solution, encoded as a vector (allocations for CPU, RAM, and Storage).
-   **Objective Functions**:
    -   f1(solution) = Total resource costs
    -   f2(solution) = -Execution speed (or response time)

#### 3. **NSGA-II Algorithm**

-   **Initialization**: Generate an initial population of solutions (random allocations).
-   **Evaluation**: Calculate the objective values for each solution.
-   **Non-dominated Sorting**: Group solutions into fronts based on dominance.
-   **Crowding Distance**: Calculate crowding distance for diversity.
-   **Selection**: Select parents using elitism and crowding distance mechanisms.
-   **Crossover and Mutation**: Create a new population through crossover and mutation.
-   **Iteration**: Repeat the steps until the stopping criterion (e.g., number of generations) is met.

#### 4. **Implementation**
**![Pseudo1](https://github.com/user-attachments/assets/dd68b80b-e7e9-4404-acea-73dcf887e041)
**
**![Pseudo2](https://github.com/user-attachments/assets/7276c501-ca01-4e78-95ed-96ee346aca7d)
**
-   **Structure**:
    -   **Data Input**: Tasks and available resources.
    -   **Initialization**: Generate solutions and initialize the population.
    -   **NSGA-II Loop**: Apply the algorithm steps.
    -   **Display Results**: Pareto front and optimal solutions.

#### 5. **Testing**

-   Test the algorithm on different datasets, simulating real-world scenarios (variations in the number of tasks and resources).
-   Analyze the obtained solutions and evaluate the trade-offs between objectives.
