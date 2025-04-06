# rag_swimrules Project

## Overview
The `rag_swimrules` project is a retrieval-augmented generation testbed designed for testing a notebook-based chatbot. This project aims to facilitate experiments and evaluations of chatbot performance and automated LLM evaluation. The chatbot is built using the LangChain framework.

Rules used in this test is based on Article 101 in [USA Swimming 2025 mini-rulebook](https://websitedevsa.blob.core.windows.net/sitefinity/docs/default-source/governance/governance-lsc-website/rules_policies/rulebooks/2025-mini-rulebook.pdf).

`glossary_terms.txt` contains the glossary terms from USA Swimming 2025 mini-rulebook.  Manually created.

`interpretation_guidance.txt` contains guidance on how to apply the technical rules.  Manually created.

`swimming_situations.json` contains the swimming situations.  Manually created from downloaded copy of [situations and resolution document](https://www.pvswim.org/official/rules/2025-03-situations-and-resolutions-stroke-and-turn.pdf).

`swimming_situations2.json` contains the swimming situations.  Manually created from downloaded copy of [situations and resolution document](https://www.pvswim.org/official/rules/2025-03-situations-and-resolutions-stroke-and-turn.pdf) with the assistance of ChatGPT using the following [prompt](src/extraction_prompt.txt).

## Project Structure
Collecting workspace information`@workspace` accuracy and speed can be improved by building a remote workspace index. [Learn More](https://aka.ms/vscode-copilot-workspace-remote-index)

Build remote workspace index

Here’s a clear and concise project structure documentation for your README.md file:

### Project Structure
GHCP prompt for generating project structure documentation:
```plaintext
@workspace in the repo generate a clear and concise project structure documentation for a README.md file. Include:  
- A hierarchical folder/file structure with brief descriptions of each component  
- Key files (e.g., `src/`, `config/`, `tests/`) and their purposes
- for files in src/ folder, include a brief description of the main functionality of each file
- A markdown table summarizing the structure for readability  
- Optional: Highlight critical files (e.g., `main.js`, `package.json`)  
Format the output as a bulleted list with indents for subfolders.
```

Collecting workspace informationHere’s a clear and concise project structure documentation for your README.md file:

#### Hierarchical Folder/File Structure
- **.env**: Environment variables for the project.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **LICENSE**: License information for the project.
- **README.md**: Documentation and overview of the project.
- **requirements.txt**: Python dependencies required for the project.
- **.vscode/**: Configuration files for Visual Studio Code.
  - **settings.json**: Workspace-specific settings for VS Code.
- **db/**: Contains database-related files.
  - **swim_rules/**: Rules related to swimming.
  - **swim_rules_semantic/**: Semantic rules for swimming.
  - **swim_rules_techrules/**: Technical rules for swimming.
- **notebooks/**: Jupyter notebooks for analysis and testing.
  - **analyze_test_results.ipynb**: Notebook for analyzing test results.
  - **chatbot_test_target_responses.ipynb**: Tests chatbot responses against target outputs.
  - **chatbot_test.ipynb**: General chatbot testing notebook.
  - **chunk_retrieval_testbed.ipynb**: Testbed for chunk retrieval functionality.
- **raw_data/**: Raw data files used in the project.
  - **2025-03-situations-and-resolutions-stroke-and-turn.pdf**: Document on stroke and turn situations.
  - **2025-mini-rulebook.pdf**: Mini rulebook for swimming.
  - **glossary_terms.txt**: Glossary of terms used in the project.
  - **interpretation_guidance.txt**: Guidance for interpreting rules.
  - **swimming_situations.json**: JSON file with swimming situations data.
  - **swimming_situations2.json**: Additional swimming situations data.
  - **technical_rules/**: Contains technical rules data.
- **results/**: Directory for storing results of analyses or tests.
- **sandbox/**: Experimental or temporary files for testing purposes.
- **src/**: Source code for the project.


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