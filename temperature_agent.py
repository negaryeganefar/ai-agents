class TemperatureAgent:
    def __init__(self):
        self.environment = [17, 24]  # initial temperature of two rooms
        self.target = 20  # goal temperature
        self.step = 0.5  # temperature change per action

    def interpret_input(self, room):
        return self.environment[room]  # state

    def rule_action(self, room, state):
        if state < self.target:
            print("Turning on heater in room", room, "->", state + self.step)
            self.environment[room] += self.step
        elif state > self.target:
            print("Turning on cooler in room", room, "->", state - self.step)
            self.environment[room] -= self.step
        else:
            print("Room", room, "is at target temperature")


agent = TemperatureAgent()
print("Initial temperatures:", agent.environment)
for _ in range(8):
    for room in range(len(agent.environment)):
        state = agent.interpret_input(room)
        agent.rule_action(room, state)
print("Final temperatures:", agent.environment)
