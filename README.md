# ai-second-brain

I've gone through stages of using logseq, notion, obsidian, markdown and text files, apple notes to build my second brain.
I need a balance in functionality and ease of use.
Markdown files on their own are not enough.
Logseq is too manual.
Notion is great for organization, but it feels heavy and like I'm missing something at the same time.
LLMs are great, but I need a way to connect the dots and make it all work together.

I need infrastructure with the simplicity of markdown, network graph capabilities of logseq, and organization of Notion.
My personal librarian, research assistant, database, and knowledge base.

This repoistory holds the code for a second brain.

## Feature Roadmap

The user interacts with the system through a chat interface.

Core features:

- Document Q&A
- Generalized Personal Assistant

## Architecture Roadmap

- Cloud-hosted vector database
- Hybrid vector search
- Evals
- APIs for vector database upsertion, retrieval, and deletion
- APIs for LLM interaction
- APIs for output formatting

## Feature Breakdown

### Document Q&A

- Document management
    - Search
    - Retrieval
    - Summarization
    - Classification
- Document generation
    - Newsletters
    - Reports
    - Tweets
    - LinkedIn posts

### Generalized Personal Assistant

- Framework to handle user interaction outside of document interactions
