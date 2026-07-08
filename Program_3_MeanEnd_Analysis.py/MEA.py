class MeansEndAnalysis:
    def __init__(self, operators):
        self.operators = operators

    def solve(self, current, goal):
        print(f"Current State: {current} | Goal State: {goal}")

        # Goal reached
        if current == goal:
            return []

        # Find the difference between current and goal
        diff = self.find_difference(current, goal)

        if not diff:
            return []

        # Select an operator to reduce the difference
        op = self.select_operator(diff)

        if not op:
            print(f"No operator found to resolve difference: {diff}")
            return None

        # Solve preconditions first
        preconditions_path = self.solve(current, op['precond'])

        if preconditions_path is None:
            return None

        # Apply the operator
        new_state = current.copy()
        new_state.update(op['effect'])

        print(f"Applying Operator: {op['name']}")
        print(f"New State: {new_state}")

        # Solve the remaining goal
        remaining_path = self.solve(new_state, goal)

        if remaining_path is None:
            return None

        return preconditions_path + [op['name']] + remaining_path

    def find_difference(self, current, goal):
        for key in goal:
            if current.get(key) != goal[key]:
                return (key, goal[key])
        return None

    def select_operator(self, diff):
        key, value = diff
        for op in self.operators:
            if op['effect'].get(key) == value:
                return op
        return None
class MeansEndAnalysis:
    def __init__(self, operators):
        self.operators = operators

    def solve(self, current, goal):
        print(f"Current State: {current} | Goal State: {goal}")

        # Goal reached
        if current == goal:
            return []

        # Find the difference between current and goal
        diff = self.find_difference(current, goal)

        if not diff:
            return []

        # Select an operator to reduce the difference
        op = self.select_operator(diff)

        if not op:
            print(f"No operator found to resolve difference: {diff}")
            return None

        # Solve preconditions first
        preconditions_path = self.solve(current, op['precond'])

        if preconditions_path is None:
            return None

        # Apply the operator
        new_state = current.copy()
        new_state.update(op['effect'])

        print(f"Applying Operator: {op['name']}")
        print(f"New State: {new_state}")

        # Solve the remaining goal
        remaining_path = self.solve(new_state, goal)

        if remaining_path is None:
            return None

        return preconditions_path + [op['name']] + remaining_path

    def find_difference(self, current, goal):
        for key in goal:
            if current.get(key) != goal[key]:
                return (key, goal[key])
        return None

    def select_operator(self, diff):
        key, value = diff
        for op in self.operators:
            if op['effect'].get(key) == value:
                return op
        return None


# Example Operators
operators = [
    {
        'name': 'Buy Flour',
        'precond': {},
        'effect': {'have_flour': True}
    },
    {
        'name': 'Buy Eggs',
        'precond': {},
        'effect': {'have_eggs': True}
    },
    {
        'name': 'Bake Cake',
        'precond': {
            'have_flour': True,
            'have_eggs': True
        },
        'effect': {'cake_ready': True}
    }
]

# Initial State
current_state = {
    'have_flour': False,
    'have_eggs': False,
    'cake_ready': False
}

# Goal State
goal_state = {
    'cake_ready': True
}

# Solve
mea = MeansEndAnalysis(operators)
solution = mea.solve(current_state, goal_state)

print("\nSolution Path:")
print(solution)