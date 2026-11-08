class VacuumAgent:
    def __init__(self):
        self.location = 0  # percept
        self.environment = ['dirty', 'dirty', 'clean', 'dirty']  # 2x2 grid: [0,0] [0,1] [1,0] [1,1]

    def interpret_input(self):
        return self.environment[self.location]  # state

    def rule_action(self, state):
        if state == 'dirty':
            print("Cleaning cell", self.location)
            self.environment[self.location] = 'clean'
        else:
            print("Moving to the next cell")
            self.location = (self.location + 1) % len(self.environment)


agent = VacuumAgent()
print("Initial environment:", agent.environment)
for _ in range(7):
    state = agent.interpret_input()
    agent.rule_action(state)
print("Final environment:", agent.environment)
