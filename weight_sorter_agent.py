class WeightSorterAgent:
    def __init__(self):
        self.location = 0  # percept
        self.environment = [35, 12, 48, 7, 26, 19, 53, 41, 2, 30]  # 10 weights in a line
        self.swaps = 0

    def interpret_input(self):
        return self.environment[self.location], self.environment[self.location + 1]  # state

    def rule_action(self, state):
        current, neighbor = state
        if current > neighbor:
            print("Swapping", current, "and", neighbor)
            self.environment[self.location] = neighbor
            self.environment[self.location + 1] = current
            self.swaps += 1
        else:
            print("Moving to the next position")
        self.location += 1


agent = WeightSorterAgent()
print("Initial environment:", agent.environment)
passes = 0
while True:
    passes += 1
    swaps_before = agent.swaps
    while agent.location < len(agent.environment) - 1:
        state = agent.interpret_input()
        agent.rule_action(state)
    print("Pass", passes, "finished:", agent.environment)
    agent.location = 0
    if agent.swaps == swaps_before:
        break
print("Final environment:", agent.environment)
