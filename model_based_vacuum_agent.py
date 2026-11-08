class ModelBasedVacuumCleaner:
    def __init__(self):
        self.environment = ['dirty', 'clean', 'dirty', 'dirty']  # 2x2 grid: [0,0] [0,1] [1,0] [1,1]
        self.position = 0
        self.model = {}

    def perceive(self):
        return self.environment[self.position]

    def update_model(self, perception):
        self.model[self.position] = perception

    def predict_future_state(self):
        # Use the internal model to predict the state of this cell
        if self.model.get(self.position) == 'dirty':
            return 'dirty'
        else:
            return 'clean'

    def decide_action(self):
        perception = self.perceive()
        self.update_model(perception)
        if perception == 'dirty':
            return 'suck'
        else:
            future_state = self.predict_future_state()
            if future_state == 'dirty':
                return 'suck'
            else:
                return 'move'

    def act(self, action):
        if action == 'suck':
            self.environment[self.position] = 'clean'
        elif action == 'move':
            self.position = (self.position + 1) % len(self.environment)


agent = ModelBasedVacuumCleaner()
print("Initial environment:", agent.environment)
for _ in range(8):
    action = agent.decide_action()
    agent.act(action)
    print(f"Position: {agent.position}, Action: {action}, Environment: {agent.environment}, Model: {agent.model}")
print("Final environment:", agent.environment)
