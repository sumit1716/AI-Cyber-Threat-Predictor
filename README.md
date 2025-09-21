# AI Cyber Threat Protection

This AI-powered Intrusion Detection System uses a high-accuracy Random Forest Classifier to classify network traffic as normal or malicious. Deployed as a real-time Flask API, it provides an effective solution for cybersecurity threat prediction and analysis.

## Features

- **High-Accuracy Model:** Uses a pre-trained Random Forest model (`ids_random_forest_model.pkl`) for accurate threat detection.
- **Real-Time API:** Deployed as a Flask API (`app.py`) for easy integration and real-time predictions.
- **Pre-trained Model:** The project includes a trained model, so you don't need to train it from scratch.

## Installation

To get this project up and running on your local machine, follow these simple steps.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/sumit1716/AI-Cyber-Threat-Predictor.git](https://github.com/sumit1716/AI-Cyber-Threat-Predictor.git)
    ```

2.  **Go to the project directory:**
    ```bash
    cd AI-Cyber-Threat-Predictor
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: Make sure you have a `requirements.txt` file listing all the libraries like scikit-learn, Flask, etc.)*

## Usage

You can run the Flask API to get real-time predictions.

1.  **Run the application:**
    ```bash
    python app.py
    ```

2.  The API will start. You can now send requests to the API endpoint to classify network traffic.

## Technologies Used

-   **Python:** The main programming language.
-   **scikit-learn:** For the machine learning model.
-   **Flask:** For creating the API.
-   **Jupyter Notebook:** For data analysis and model training (if applicable).

## Contact

-   **GitHub:** [sumit1716](https://github.com/sumit1716)

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
