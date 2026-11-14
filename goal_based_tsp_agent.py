import math


class TravelingSalesmanAgent:
    def __init__(self, start, cities):
        self.position = start
        self.cities = cities
        self.visited = [start]
        self.path = [start]
        self.goal = len(cities)

    def perceive(self):
        return self.position

    def act(self):
        # Goal: visit all cities
        if len(self.visited) == self.goal:
            return 'GoalReached'
        # Greedy rule: choose the nearest unvisited city
        x, y = self.cities[self.position]
        nearest = None
        for city in self.cities:
            if city not in self.visited:
                if nearest is None:
                    nearest = city
                elif math.dist((x, y), self.cities[city]) < math.dist((x, y), self.cities[nearest]):
                    nearest = city
        return nearest

    def update_position(self, action):
        self.position = action
        self.visited.append(action)
        self.path.append(action)


# Cities on a 2x2 grid (x, y)
cities = {
    'A': (0, 0),
    'B': (0, 1),
    'C': (1, 1),
    'D': (1, 0),
}

agent = TravelingSalesmanAgent(start='A', cities=cities)

while len(agent.visited) < len(agent.cities):
    percept = agent.perceive()
    action = agent.act()
    print(f"Position: {percept}, Action: {action}")
    agent.update_position(action)

print("Path to goal:", agent.path)
