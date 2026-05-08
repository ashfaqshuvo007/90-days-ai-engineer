# 90-days-ai-engineer

Collection of topics, daily logs, resources and roadmap for the switch from Backend Engineer to AI Product Engineer

## Phase 0: Crash Courses

Before you write a single line of project code, get your hands dirty with these in isolated scripts. Spend each day on one topic; build tiny throwaway experiments and break them intentionally.

### Day 1: API anatomy & structured output

- Run the OpenAI/Anthropic quickstarts (Python & JS).

- Send a message, stream it, mess with temperature/top_p, hit a rate limit, parse an error.

- Force JSON output using the response_format parameter (or tool calling with strict: true). Write a script that asks for a fictional invoice and stores the parsed JSON in a dict. Intentionally prompt it to break the schema and catch the failure.

### Day 2: Function calling & tool use

- Define a tool that simulates a database lookup (e.g., get_customer_orders). Make the LLM decide when to call it. Loop until it returns a final answer.

- Create a second tool that modifies data (update_ticket_status). Chain them: first retrieve, then update. This is the core of every AI agent.

### Day 3: Minimal RAG pipeline

- Chunk a PDF (use LangChain’s text splitter or just a naive recursive split).

- Generate embeddings with OpenAI text-embedding-3-small, store in a local Chroma or in-memory list.

- Do a similarity search, stuff top-3 chunks into a prompt, answer a question.

- Break it: what happens if chunks are too small, too large, or irrelevant? Watch how confident the LLM remains. That’s the hallucination lesson.

### Day 4: Basic backend + frontend “Hello AI”

- FastAPI endpoint that receives a query, calls OpenAI, streams back the response.

- Minimal frontend with plain HTML/JS fetch that renders streaming tokens. Or use Streamlit for speed.

- Add one more endpoint that accepts a JSON payload, validates it, and returns structured output. This is your template for every project.
