from core.ai_engine import AIEngine


class ResearchAgent:

    def __init__(self):
        self.name = "Arkavian Research Agent"
        self.ai_engine = AIEngine()

    def research(self, topic):
        print(f"Researching topic: {topic}")
        ai_result = self.ai_engine.run(topic)
        return f"Research summary generated for '{topic}' using {ai_result}."


if __name__ == "__main__":
    agent = ResearchAgent()
    result = agent.research("AI automation trends")
    print(result)
