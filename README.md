# rag_swimrules Project

## Overview
The `rag_swimrules` project is a retrieval-augmented generation testbed designed for testing a notebook-based chatbot. This project aims to facilitate experiments and evaluations of chatbot performance and automated LLM evaluation. The chatbot is built using the LangChain framework.

Rules used in this test is based on Article 101 in [USA Swimming 2025 mini-rulebook](https://websitedevsa.blob.core.windows.net/sitefinity/docs/default-source/governance/governance-lsc-website/rules_policies/rulebooks/2025-mini-rulebook.pdf).

`glossary_terms.txt` contains the glossary terms from USA Swimming 2025 mini-rulebook.  Manually created.

`interpretation_guidance.txt` contains guidance on how to apply the technical rules.  Manually created.

## Project Structure
Collecting workspace information`@workspace` accuracy and speed can be improved by building a remote workspace index. [Learn More](https://aka.ms/vscode-copilot-workspace-remote-index)

Build remote workspace index

Here’s a clear and concise project structure documentation for your README.md file:

### Project Structure
GHCP prompot for generating project structure documentation:
```plaintext
@workspace Generate a clear and concise project structure documentation for a README.md file. Include:  
- A hierarchical folder/file structure with brief descriptions of each component  
- Key files (e.g., `src/`, `config/`, `tests/`) and their purposes  
- A markdown table summarizing the structure for readability  
- Optional: Highlight critical files (e.g., `main.js`, `package.json`)  
Format the output as a bulleted list with indents for subfolders and a table for quick reference.  
```
Collecting workspace informationHere’s a clear and concise project structure documentation for your README.md file:

### Project Structure

#### Hierarchical Folder/File Structure
- **`.env`**: Environment variables for the project.
- **`.gitignore`**: Specifies files and directories to be ignored by Git.
- **LICENSE**: License information for the project.
- **`README.md`**: Project documentation.
- **`requirements.txt`**: Python dependencies for the project.
- **`.vscode/`**: VS Code-specific settings.
  - **`settings.json`**: Configuration for the VS Code workspace.
- **db**: Contains database files.
  - **`swim_rules/`**: Stores rule-related database files.
    - **`chroma.sqlite3`**: SQLite database for swim rules.
  - **`swim_rules_semantic/`**: Stores semantic rule-related database files.
    - **`chroma.sqlite3`**: SQLite database for semantic swim rules.
- **notebooks**: Jupyter notebooks for testing and experimentation.
  - **`chatbot_test.ipynb`**: Notebook for chatbot testing.
  - **`chunk_retrieval_testbed.ipynb`**: Notebook for chunk retrieval experiments.
- **raw_data**: Contains raw input data files.
  - **`2025-mini-rulebook.pdf`**: PDF document of the mini rulebook.
  - **`glossary_terms.txt`**: Glossary of terms.
  - **`interpretation_guidance.txt`**: Guidance for interpreting rules.
- **sandbox**: Experimental notebooks and scripts.
  - **`chunk_relevence_testbed.ipynb`**: Notebook for testing chunk relevance.
  - **`show_chunks.ipynb`**: Notebook for displaying chunks.
- **src**: Source code for the project.
  - **`__init__.py`**: Marks the directory as a Python package.
  - **`doc_ingestion.py`**: Create VectorStore using RecursiveCharacterTextSplitter.
  - **`doc_ingestion_semantic.py`**: Create VectorStore using SemanticChunker.
  - **`pdf_read_test.ipynb`**: Notebook for testing PDF reading.

#### Summary Table

| File/Folder              | Description                                      |
|--------------------------|--------------------------------------------------|
| .env                   | Environment variables for the project.          |
| .gitignore             | Files/directories ignored by Git.               |
| LICENSE                | License information.                            |
| README.md              | Project documentation.                          |
| requirements.txt       | Python dependencies.                            |
| settings.json  | VS Code workspace settings.                     |
| swim_rules         | Rule-related database files.                    |
| swim_rules_semantic| Semantic rule-related database files.           |
| notebooks             | Jupyter notebooks for testing and experiments.  |
| raw_data              | Raw input data files.                           |
| sandbox               | Experimental notebooks and scripts.             |
| src                   | Source code for the project.                    |



## Installation
To set up the project, clone the repository and install the required dependencies. You can do this by running:

```bash
# install duckdb using homebrew for local persistence
brew install duckdb

# install the required dependencies
pip install -r requirements.txt
```



## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.