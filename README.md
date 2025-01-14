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

-   **Algorithm steps**:
![Pseudo1](https://github.com/user-attachments/assets/597b0fb6-0215-4d0f-8253-f86d28499cd3)
![Pseudo2](https://github.com/user-attachments/assets/fbbc166b-e124-4036-ae8a-2cdb981beaf4)

-   **Structure**:
    -   **Data Input**: Tasks and available resources.
    -   **Initialization**: Generate solutions and initialize the population.
    -   **NSGA-II Loop**: Apply the algorithm steps.
    -   **Display Results**: Pareto front and optimal solutions.

#### 5. **Testing**

-   Test the algorithm on different datasets, simulating real-world scenarios (variations in the number of tasks and resources).
-   Analyze the obtained solutions and evaluate the trade-offs between objectives.

#### 6. **Results**
![image](https://github.com/user-attachments/assets/72ab87a9-6401-4781-9eb1-e0e6cc55f55a)
![image](https://github.com/user-attachments/assets/ef7145ae-5661-444a-b9ff-cca8f6a249d6)
