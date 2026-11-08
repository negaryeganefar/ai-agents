class TemperatureAgent:
    def __init__(self):
        self.environment = [17, 24]  # initial temperature of two rooms
        self.position = 0
        self.target = 20  # goal temperature
        self.step = 0.5  # temperature change per action
        self.model = {}

    def perceive(self):
        return self.environment[self.position]

    def update_model(self, perception):
        self.model[self.position] = perception

    def predict_future_state(self):
        # Use the internal model to predict the state of this room
        if self.model.get(self.position) < self.target:
            return 'cold'
        elif self.model.get(self.position) > self.target:
            return 'hot'
        else:
            return 'target'

    def decide_action(self):
        perception = self.perceive()
        self.update_model(perception)
        if perception < self.target:
            return 'heat'
        elif perception > self.target:
            return 'cool'
        else:
            future_state = self.predict_future_state()
            if future_state == 'cold':
                return 'heat'
            elif future_state == 'hot':
                return 'cool'
            else:
                return 'move'

    def act(self, action):
        if action == 'heat':
            self.environment[self.position] += self.step
        elif action == 'cool':
            self.environment[self.position] -= self.step
        elif action == 'move':
            self.position = (self.position + 1) % len(self.environment)


agent = TemperatureAgent()
print("Initial temperatures:", agent.environment)
for _ in range(18):
    action = agent.decide_action()
    agent.act(action)
    print(f"Position: {agent.position}, Action: {action}, Environment: {agent.environment}, Model: {agent.model}")
print("Final temperatures:", agent.environment)
