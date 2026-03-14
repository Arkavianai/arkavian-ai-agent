from core.ai_engine import AIEngine


class BusinessAgent:

    def __init__(self):
        self.name = "Arkavian Business Agent"
        self.ai_engine = AIEngine()

    def analyze(self, business_problem):
        print(f"Analyzing business problem: {business_problem}")
        ai_result = self.ai_engine.run(business_problem)
        return f"Insights generated for '{business_problem}' using {ai_result}."


if __name__ == "__main__":
    agent = BusinessAgent()
    result = agent.analyze("Improving operational efficiency")
    print(result)
