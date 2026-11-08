class LightSwitchAgent:
    def __init__(self):
        self.environment = ['on', 'off', 'on', 'on']
        self.position = 0
        self.model = {}

    def perceive(self):
        return self.environment[self.position]

    def update_model(self, perception):
        self.model[self.position] = perception

    def predict_future_state(self):
        if self.model.get(self.position) == 'on':
            # If the light is on, predict it will remain on
            return 'on'
        else:
            # Otherwise, predict it will be off
            return 'off'

    def decide_action(self):
        perception = self.perceive()
        self.update_model(perception)
        if perception == 'on':
            return 'toggle'
        else:
            future_state = self.predict_future_state()
            if future_state == 'on':
                return 'toggle'
            else:
                return 'move'

    def act(self, action):
        if action == 'toggle':
            self.environment[self.position] = 'off'
        elif action == 'move':
            self.position = (self.position + 1) % len(self.environment)


agent = LightSwitchAgent()
for _ in range(6):
    action = agent.decide_action()
    agent.act(action)
    print(f"Position: {agent.position}, Action: {action}, Environment: {agent.environment}, Model: {agent.model}")
