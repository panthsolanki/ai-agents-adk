from google.adk.agents import LlmAgent, SequentialAgent

# Step 1: Extract User Profile
profiler = LlmAgent(
    name="ProfilerAgent",
    model="gemini-2.5-flash",
    instruction="Extract skills and goals from the user's text. Format as a bulleted list.",
    output_key="user_profile"
)

# Step 2: Suggest Careers
analyst = LlmAgent(
    name="MarketAnalyst",
    model="gemini-2.5-flash",
    instruction="Based on the profile in {user_profile}, suggest 3 matching career paths.",
    output_key="career_suggestions"
)

# Step 3: Create Roadmap
planner = LlmAgent(
    name="ActionPlanner",
    model="gemini-2.5-flash",
    instruction="Look at {career_suggestions}. Pick the best fit and write a 3-step action plan.",
    output_key="final_roadmap"
)

# The Orchestrator
root_agent = SequentialAgent(
    name="root_agent",
    sub_agents=[profiler, analyst, planner],
    description="A multi-stage agent that profiles users and provides career roadmaps."
)