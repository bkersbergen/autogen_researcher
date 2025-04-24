import os
import re
from dotenv import load_dotenv
from duckduckgo_search import DDGS

from autogen import ConversableAgent, UserProxyAgent

# --- Load .env configuration ---
load_dotenv()

OLLAMA_MODEL = os.getenv("LOCAL_LLM", "llama3.2")
OLLAMA_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
MAX_LOOPS = int(os.getenv("MAX_WEB_RESEARCH_LOOPS", 2))
RESULTS_PER_SEARCH = int(os.getenv("RESULTS_PER_SEARCH", 5))

# --- Disable Docker (fully local) ---
os.environ["AUTOGEN_USE_DOCKER"] = "False"

# --- Shared config for all agents using Ollama ---
ollama_llm_config = {
    "config_list": [
        {
            "model": OLLAMA_MODEL,
            "api_key": "ollama",  # dummy, required field
            "base_url": OLLAMA_URL,
            "api_type": "openai",
            "price": [0, 0]  # suppress pricing warning
        }
    ]
}

# --- Create agents ---
user = UserProxyAgent(
    name="User",
    human_input_mode="NEVER",
    code_execution_config={"use_docker": False}
)

query_agent = ConversableAgent(
    name="QueryAgent",
    system_message="Return only a single-line search query string. No formatting or explanations.",
    llm_config=ollama_llm_config
)

summary_agent = ConversableAgent(
    name="SummaryAgent",
    system_message="Summarize the search results in Markdown with source citations.",
    llm_config=ollama_llm_config
)

reflect_agent = ConversableAgent(
    name="ReflectAgent",
    system_message="Identify 2-3 key knowledge gaps or follow-up questions based on the summary.",
    llm_config=ollama_llm_config
)

# --- DuckDuckGo search wrapper ---
def duckduckgo_search(query: str, max_results=5) -> str:
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)
    return "\n".join(
        f"**{r['title']}**: {r['body']} ({r['href']})" for r in results
    )

# --- Cleanup: Extract raw query string ---
def clean_query(raw: str) -> str:
    match = re.search(r'\*\*Query:\*\*\s*(.*)', raw)
    if match:
        return match.group(1).strip()
    return raw.strip().splitlines()[0]  # fallback

# --- Core research loop ---
class LocalDeepResearcher:
    def __init__(self, topic: str):
        self.topic = topic
        self.summary = ""

    def run(self) -> str:
        query = self.topic
        for i in range(MAX_LOOPS):
            print(f"\n Loop {i+1} | Query: {query}")
            search_results = duckduckgo_search(query, RESULTS_PER_SEARCH)

            # Summarize results
            summary_prompt = f"Topic: {self.topic}\nSearch Results:\n{search_results}"
            new_summary = summary_agent.generate_reply(messages=[{"role": "user", "content": summary_prompt}])
            self.summary += f"\n{new_summary}" if self.summary else new_summary

            # Reflect on knowledge gaps
            gaps = reflect_agent.generate_reply(messages=[{"role": "user", "content": self.summary}])

            # Generate a new search query
            query_prompt = f"Topic: {self.topic}\nSummary:\n{self.summary}\nGaps:\n{gaps}"
            query_response = query_agent.generate_reply(messages=[{"role": "user", "content": query_prompt}])
            query = clean_query(query_response)

        return f"# Research Summary\n\n{self.summary.strip()}\n\n## Topic\n{self.topic}"


# --- CLI entrypoint ---
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Local Deep Researcher using AutoGen + Ollama")
    parser.add_argument("topic", type=str, help="Research topic to explore")
    args = parser.parse_args()

    researcher = LocalDeepResearcher(args.topic)
    print(researcher.run())
