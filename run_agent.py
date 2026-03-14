from core.ai_engine import AIEngine
from agents.research_agent import ResearchAgent

engine = AIEngine()
research_agent = ResearchAgent()

task = "Latest trends in AI agents"

print("Running Arkavian AI...\n")

engine.run(task)
result = research_agent.research(task)

print("\nResearch Agent Result:")
print(result)
