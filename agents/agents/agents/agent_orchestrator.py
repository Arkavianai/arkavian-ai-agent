# Arkavian Agent Orchestrator

from automation_agent import AutomationAgent
from research_agent import ResearchAgent
from business_agent import BusinessAgent


class AgentOrchestrator:

    def __init__(self):
        self.automation_agent = AutomationAgent()
        self.research_agent = ResearchAgent()
        self.business_agent = BusinessAgent()

    def run_all(self):
        print("Starting Arkavian multi-agent workflow...\n")

        automation_result = self.automation_agent.run("Automate invoice workflow")
        research_result = self.research_agent.research("AI workflow automation trends")
        business_result = self.business_agent.analyze("How to improve operational efficiency")

        return {
            "automation": automation_result,
            "research": research_result,
            "business": business_result,
        }


if __name__ == "__main__":
    orchestrator = AgentOrchestrator()
    results = orchestrator.run_all()

    print("\nArkavian Orchestrator Results:")
    for key, value in results.items():
        print(f"{key}: {value}")
