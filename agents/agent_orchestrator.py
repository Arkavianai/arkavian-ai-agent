from agents.automation_agent import AutomationAgent
from agents.research_agent import ResearchAgent
from agents.business_agent import BusinessAgent


class AgentOrchestrator:
    def __init__(self):
        self.automation_agent = AutomationAgent()
        self.research_agent = ResearchAgent()
        self.business_agent = BusinessAgent()

    def run_all(self, task):
        automation_result = self.automation_agent.run(task)
        research_result = self.research_agent.research(task)
        business_result = self.business_agent.analyze(task)

        return {
            "automation": automation_result,
            "research": research_result,
            "business": business_result,
        }
