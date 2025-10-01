class Rule:
    def __init__(self, conditions, conclusion):
        self.conditions = conditions
        self.conclusion = conclusion

class ExpertSystem:
    def __init__(self):
        self.rules = []
        self.facts = dict()
        self.trueFacts = set()

    def infer(self):
        for rule in self.rules:
            for condition in rule.conditions:
                if condition not in self.facts:
                    response = input(f"Is it true that {condition}? (yes/no): ").strip().lower()

                    if response == 'yes':
                        self.facts[condition] = "yes"
                    else:
                        self.facts[condition] = "no"

        for key, value in self.facts.items():
            if value == "yes":
                self.trueFacts.add(key)

        for rule in self.rules:
            if self.trueFacts in rule:
                print(rule.conclusion)

        # for rule in self.rules:
        #     matched = []
        #     for condition in rule.conditions:
        #         if condition in self.facts:
        #             matched.append(True)
        #         else:
        #             matched.append(False)
        #
        #     if all(matched):

# Example usage
if __name__ == "__main__":
    # Create an expert system
    es = ExpertSystem()
    # Add rules
    es.rules.append(Rule(["sunny"], "wear_sunglasses"))
    es.rules.append(Rule(["rainy"], "take_umbrella"))
    es.rules.append(Rule(["sunny", "weekend"], "go_to_beach"))
    # Perform inference
    es.infer()
    # Print final facts
    # print("Final facts:", es.facts)