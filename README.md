# rag_swimrules Project

## Overview
The `rag_swimrules` project is a retrieval-augmented generation testbed designed for testing a notebook-based chatbot. This project aims to facilitate experiments and evaluations of chatbot performance in various scenarios.

## Project Structure
```
rag_swimrules
|-- raw_data/
|-- db/
├── notebooks
│   └── chatbot_test.ipynb
├── src
│   ├── __init__.py
│   ├── chatbot.py
│   └── utils.py
├── tests
│   ├── __init__.py
│   └── test_chatbot.py
├── requirements.txt
├── setup.py
└── README.md
```

## Installation
To set up the project, clone the repository and install the required dependencies. You can do this by running:

```bash
# install duckdb using homebrew for local persistence
brew install duckdb

# install the required dependencies
pip install -r requirements.txt
```

## Usage
To use the chatbot, you can run the Jupyter notebook located in the `notebooks` directory. This notebook contains tests and experiments that showcase the chatbot's functionality and performance.

## Contributing
Contributions are welcome! If you would like to contribute to the project, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.