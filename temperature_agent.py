class TemperatureAgent:
    def __init__(self):
        self.location = (0, 0)  # percept
        self.environment = [[17, 24], [17, 24]]
        self.target = 20
        self.step = 0.5

    def interpret_input(self):
        return self.environment[self.location[0]][self.location[1]]  # state

    def rule_action(self, state):
        if state < self.target:
            print("Turning on heater in room", self.location, "->", state + self.step)
            self.environment[self.location[0]][self.location[1]] += self.step
        elif state > self.target:
            print("Turning on cooler in room", self.location, "->", state - self.step)
            self.environment[self.location[0]][self.location[1]] -= self.step
        else:
            print("Moving to the next room")
            row, col = self.location
            col += 1
            if col == len(self.environment[0]):
                col = 0
                row = (row + 1) % len(self.environment)
            self.location = (row, col)


agent = TemperatureAgent()
print("Initial environment:", agent.environment)
for _ in range(32):
    state = agent.interpret_input()
    agent.rule_action(state)
print("Final environment:", agent.environment)
