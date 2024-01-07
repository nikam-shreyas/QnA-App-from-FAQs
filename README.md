# QnA App from FAQs

**Build a Question Answering System from a CSV File with Google AI**

## Overview

This project leverages Google AI's powerful PALM model to create a question-answering (QA) system from a provided CSV file of question-answer pairs. It offers a user-friendly interface with Streamlit and efficient vector database management with FAISS.

## Key Features

- **PALM-powered Question Answering:** Employs Google AI's PALM model for robust question understanding and accurate answer retrieval.
- **Streamlit UI:** Provides an intuitive web interface for user interaction with the QA system.
- **FAISS Vector Database:** Optimizes search performance for fast and efficient question-answering.
- **Customizable Data:** Works with any CSV file containing question-answer pairs, allowing for adaptability to various domains.

## Getting Started

**Prerequisites:**

- Python 3.7 or later.
- A Google API key ([https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)) wh_ich you need to put in the environment variable named GOOGLE_API_KEY.

**Installation:**

1. Clone this repository:
   ```bash
   git clone https://github.com/nikam-shreyas/QnA-App-from-FAQs.git
   ```
2. Create a virtual environment and activate it (recommended):
   ```bash
   python -m venv env
   source env/bin/activate # for maxOS/Linux
   env\Scripts\activate    # for Windows
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

**Environment Variables:**

- Set the `GOOGLE_API_KEY` environment variable to your Google API key.

**Running the App:**

1. Start the Streamlit app (Running it for the first time may take some time to create the vector database from the CSV file.):
   ```bash
   streamlit run streamlit_ui.py
   ```
2. Access the app in your web browser (usually at http://localhost:8501).

**Customizing Data:**

- Replace the provided `FAQ.csv` file with your own CSV file containing question-answer pairs.
- Alternatively, edit the `CSV_FILE_PATH` variable in `streamlit_ui.py` to point to your desired CSV file.

**Troubleshooting:**

- If you encounter errors, double-check the installation steps, API key configuration, and CSV file format.
- Refer to the documentation for PALM, Langchain, FAISS, and Streamlit for more detailed troubleshooting guidance.

## Contributing

We welcome contributions to improve this project! Please fork the repository and submit pull requests.

## License

This project is licensed under the MIT License.
