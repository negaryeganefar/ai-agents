class RoutePlanningAgent:
    def __init__(self, start, goal, grid):
        self.position = start
        self.goal = goal
        self.grid = grid
        self.path = []

    def perceive(self):
        return self.position

    def act(self):
        if self.position == self.goal:
            return 'GoalReached'
        # Goal-based rule: choose the move that gets closest to the goal
        x, y = self.position
        moves = [('Right', x, y + 1), ('Down', x + 1, y), ('Left', x, y - 1), ('Up', x - 1, y)]
        best = None
        for name, nx, ny in moves:
            if 0 <= nx < len(self.grid) and 0 <= ny < len(self.grid[0]) and self.grid[nx][ny] == 0:
                dist = abs(nx - self.goal[0]) + abs(ny - self.goal[1])
                if best is None or dist < best[0]:
                    best = (dist, name)
        return best[1]

    def update_position(self, action):
        x, y = self.position
        if action == 'Right':
            self.position = (x, y + 1)
        elif action == 'Down':
            self.position = (x + 1, y)
        elif action == 'Left':
            self.position = (x, y - 1)
        elif action == 'Up':
            self.position = (x - 1, y)
        self.path.append(self.position)


# Route map (0 = road, 1 = wall)
grid = [
    [0, 1],
    [0, 0],
]

agent = RoutePlanningAgent(start=(0, 0), goal=(1, 1), grid=grid)

while agent.position != agent.goal:
    percept = agent.perceive()
    action = agent.act()
    print(f"Position: {percept}, Action: {action}")
    agent.update_position(action)

print("Path to goal:", agent.path)
