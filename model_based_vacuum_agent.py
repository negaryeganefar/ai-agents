class ModelBasedVacuumCleaner:
    def __init__(self):
        self.environment = [['dirty', 'dirty'], ['clean', 'dirty']]
        self.position = (0, 0)
        self.model = {}

    def perceive(self):
        return self.environment[self.position[0]][self.position[1]]

    def update_model(self, perception):
        self.model[self.position] = perception

    def predict_future_state(self):
        if self.model.get(self.position) == 'dirty':
            # If the current cell is dirty, predict it will remain dirty
            return 'dirty'
        else:
            # Otherwise, predict it will be clean
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
            self.environment[self.position[0]][self.position[1]] = 'clean'
        elif action == 'move':
            row, col = self.position
            col += 1
            if col == len(self.environment[0]):
                col = 0
                row = (row + 1) % len(self.environment)
            self.position = (row, col)


agent = ModelBasedVacuumCleaner()
for _ in range(6):
    action = agent.decide_action()
    agent.act(action)
    print(f"Position: {agent.position}, Action: {action}, Environment: {agent.environment}, Model: {agent.model}")
