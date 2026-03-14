from core.ai_engine import AIEngine


class AutomationAgent:

    def __init__(self):
        self.name = "Arkavian Automation Agent"
        self.ai_engine = AIEngine()

    def run(self, task):
        print(f"Running task: {task}")
        ai_result = self.ai_engine.run(task)
        return f"Task '{task}' executed by Arkavian agent using {ai_result}."


if __name__ == "__main__":
    agent = AutomationAgent()
    result = agent.run("Example workflow automation")
    print(result)
