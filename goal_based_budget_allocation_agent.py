class BudgetAllocationAgent:
    def __init__(self, budget, resources):
        self.budget = budget
        self.resources = resources
        self.allocation = {r: 0 for r in resources}
        self.total_weight = sum(resources.values())
        self.goal = {r: budget * w / self.total_weight for r, w in resources.items()}

    def perceive(self):
        return self.allocation

    def act(self):
        if sum(self.allocation.values()) == self.budget:
            return 'GoalReached'
        # Goal-based rule: fund the resource with the largest deficit
        best = None
        for r in self.resources:
            deficit = self.goal[r] - self.allocation[r]
            if best is None or deficit > best[0]:
                best = (deficit, r)
        return best[1]

    def update_allocation(self, action):
        self.allocation[action] += 1


# Resources with their weights and the total budget
resources = {'R1': 3, 'R2': 8, 'R3': 17}
budget = 28

agent = BudgetAllocationAgent(budget=budget, resources=resources)

while sum(agent.allocation.values()) < agent.budget:
    percept = agent.perceive()
    action = agent.act()
    print(f"Allocation: {percept}, Action: {action}")
    agent.update_allocation(action)

print("Final allocation:", agent.allocation)
