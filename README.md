# Research Copilot AI Agent

An AI-powered research assistant that leverages LangChain, OpenAI's GPT models, and web search tools to help you conduct research quickly and efficiently.

## 📋 Features

- **Structured Research Output**: Get organized responses with topic, summary, sources, and tools used
- **Multi-tool Search**: Harnesses both Wikipedia and DuckDuckGo search for comprehensive results
- **Model Flexibility**: Compatible with OpenAI and Anthropic models
- **Error Handling**: Robust parsing with error fallback mechanisms

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/howyashpanchal/research-copilot-ai-agent.git
   cd research-copilot-ai-agent
   ```

2. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

3. Create a `.env` file with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## 🚀 Usage

Run the main script:
```bash
python3 main.py
```

When prompted, enter your research query. For example:
- "What is quantum computing and its potential applications?"
- "Explain the history and impact of the Renaissance on modern art"
- "Summarize recent developments in renewable energy technology"

## 🔧 Configuration

The default configuration uses OpenAI's `gpt-4o-mini` model. You can modify `main.py` to use different models:

```python
# For OpenAI
LLM = ChatOpenAI(model="gpt-4o-mini")  # or any other OpenAI model
```

## 🧠 How It Works

1. The system uses a Pydantic model (`ResearchResponse`) to structure output
2. It leverages tool-calling LLM capabilities to search Wikipedia and DuckDuckGo
3. The agent processes your query, decides which tools to use, and gathers information
4. Results are formatted into structured output with topic, summary, sources, and tools used

## 🔄 Tools

- **Wikipedia Search**: Access comprehensive information from Wikipedia
- **DuckDuckGo Search**: Retrieve broader web results for your queries

## 📄 License

This project is open-source and available under the MIT License.

---

Created by Yash Panchal • https://github.com/howyashpanchal
