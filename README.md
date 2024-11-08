
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
This project requires configuring email functionality to work correctly. In the `apps` folder, specifically within the `operations.py` file on lines **24** and **25**, you must replace the placeholder values with your own **Google email** and **Google App Password**.

## Instructions for Email Setup

1. **Locate the file to edit**:
   - Open the `operations.py` file located in the `apps` folder.
   - Go to lines **24** and **25**. These lines contain placeholders for `EMAIL` and `PASSWORD`.

2. **Replace placeholders**:
   - Replace the `EMAIL` placeholder with your own Google email address.
   - Replace the `PASSWORD` placeholder with your Google App Password.

   Example:
   ```python
   EMAIL = "your_email@gmail.com"
   PASSWORD = "your_app_password"

   ## Creating a Google App Password

To securely use your Google email in the project, you need to set up a **Google App Password**. Follow these steps:

1. **Enable 2-Step Verification**:
   - Go to your Google Account ([https://myaccount.google.com](https://myaccount.google.com)).
   - In the **Security** section, locate and enable **2-Step Verification**. This must be set up before creating an App Password.

2. **Create an App Password**:
   - Once 2-Step Verification is enabled, return to the **Security** section.
   - Under **Signing in to Google**, select **App Passwords**.
   - In the **App Passwords** window:
     - Choose **Mail** as the app.
     - Choose **Other (Custom name)** for the device, then enter a name (e.g., "ProjectEmail").
     - Google will generate a 16-character App Password for you.

3. **Use the App Password in Your Project**:
   - Copy the generated App Password. Use it in place of your normal password where required in your project.

## Important Notes
- **Updating App Passwords**: If you lose access to your App Password, follow the steps above to create a new one and update it in your project.

## Running the App
- now everything is done start the flask server



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
