from agents.agent_orchestrator import AgentOrchestrator


def main():
    task = "Improve customer support with AI automation"

    print("Running Arkavian multi-agent system...\n")

    orchestrator = AgentOrchestrator()
    results = orchestrator.run_all(task)

    print("Results:\n")
    for agent_name, result in results.items():
        print(f"{agent_name}: {result}")


if __name__ == "__main__":
    main()
