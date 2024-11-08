
# Brain Detection Flask App

This project is a Flask-based web application for brain detection. It allows users to upload brain scan images and returns detection results based on a machine learning model.

## Features
- Upload brain scan images
- Get real-time detection results
- Simple, clean user interface
- an interface for admin to controlle the overall performance of the system

## Prerequisites

Before running the app, ensure you have the following installed:

- **Python 3.x**
- **pip** (Python package manager)
- **Virtual Environment** (Optional but recommended)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/abalex12/Brain-Tumor_Detection_app.git
   cd Brain-Tumor_Detection_app
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the App



1. **Start the Flask server:**
   ```bash
   python run.py
   ```

2. **Access the app in your browser:**
  Open [http://localhost:5000](http://localhost:5000) in your web browser.



## How It Works

1. The user uploads an image of a brain scan.
2. The image is processed using a pre-trained machine learning model.
3. The model detects relevant features and returns the results to the user.

## Troubleshooting

- If you encounter any issues related to missing dependencies, try running:
  ```bash
  pip install --upgrade pip
  ```

- For issues with Flask or Python, ensure your Python version is 3.x and that all dependencies are correctly installed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.