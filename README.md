# Jumbo Server

The usage-agnostic "Brain" for the Jumbo AI system. This FastAPI-based server acts as the central intelligence node, processing inputs and generating expressions, text, and buzzer commands for the Jumbo hardware.

## Features

- **Brain API**: A `/jumbo-ai/brain` endpoint that maintains conversation context and simulates a conscious lifeform.
- **Modular Architecture**: Built with SOLID principles, separating core configuration, LLM integration, and API routes.
- **LLM Integration**: Uses OpenRouter (compatible with OpenAI SDK) to access powerful models like Gemini Flash.
- **Dependency Management**: Powered by [uv](https://github.com/astral-sh/uv) for fast and reliable package management.

## Prerequisites

- **Python 3.12+**
- **uv**: Python package installer and resolver.
  - Install via curl: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - Or pip: `pip install uv`

## Setup

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd Jumbo-Server
    ```

2.  **Environment Configuration**:
    Copy the example environment file and configure your API keys.
    ```bash
    cp .env.example .env
    ```
    Edit `.env` and add your `OPENROUTER_API_KEY`.

    > **Note**: The System Prompt is defined in `src/app/core/constants.py` if you wish to modify Jumbo's personality.

3.  **Install Dependencies**:
    Sync the project environment with `uv`.
    ```bash
    uv sync
    ```

## Running the Server

Start the development server with hot-reload enabled:

```bash
uv run uvicorn src.app.main:app --reload --host 0.0.0.0
```

The server will start at `http://0.0.0.0:8000`.
We have used `0.0.0.0` to allow connections from other devices(Jumbo Hardware) on the same network. 

**Note**: Take special care if you are on a public network.

## API Usage

### Chat with Jumbo

**Endpoint**: `POST /jumbo-ai/brain`

**Request Body**:
```json
{
  "message": "Limitless connection established. Wake up Jumbo."
}
```

**Example Curl**:
```bash
curl -X POST "http://localhost:8000/jumbo-ai/brain" \
  -H "Content-Type: application/json" \
  -d '{"message": "Wake up friend!"}'
```

**Response**:
Jumbo returns a JSON sequence of expressions and texts.
```json
[
    {"Expression": "SHOCKED", "BuzzerDuration": 0.1, "Text": "Ooh?", "DisplayDuration": 2.0},
    {"Expression": "HAPPY", "BuzzerDuration": 0.0, "Text": "Hello Friend!", "DisplayDuration": 5.0}
]
```

## Testing

Run the test suite using `pytest`:

```bash
# Run tests with a mock API key
OPENROUTER_API_KEY=test_key uv run pytest tests/
```

## Project Structure

```
Jumbo-Server/
├── src/app/
│   ├── api/            # API Route definitions
│   ├── core/           # Configuration, Constants, Interfaces
│   ├── services/       # LLM Client, History Management
│   └── main.py         # Application Entrypoint
├── tests/              # Automated Tests
├── .env                # Secrets (Not committed)
├── .env.example        # Template for secrets
└── pyproject.toml      # Project & dependencies configuration
```
