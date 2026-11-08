class VacuumAgent:
    def __init__(self):
        self.location = (0, 0)  # percept
        self.environment = [['dirty', 'dirty'], ['clean', 'dirty']]

    def interpret_input(self):
        return self.environment[self.location[0]][self.location[1]]  # state

    def rule_action(self, state):
        if state == 'dirty':
            print("Cleaning cell", self.location)
            self.environment[self.location[0]][self.location[1]] = 'clean'
        else:
            print("Moving to the next cell")
            row, col = self.location
            col += 1
            if col == len(self.environment[0]):
                col = 0
                row = (row + 1) % len(self.environment)
            self.location = (row, col)


agent = VacuumAgent()
print("Initial environment:", agent.environment)
for _ in range(7):
    state = agent.interpret_input()
    agent.rule_action(state)
print("Final environment:", agent.environment)
