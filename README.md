
## Description
This project was built using Python, Flask, Jinja2, HTML, and CSS. It's still a work in progress.
Currently, the game goes through a series of riddles stored in a text file, and the game ends when all riddles have been solved.

<img width="1506" alt="Screenshot 2024-12-23 at 9 28 46 PM" src="https://github.com/user-attachments/assets/edfe31ee-1797-4d13-ac1a-19164af5cf23" />

<img width="1503" alt="Screenshot 2024-12-24 at 7 43 15 PM" src="https://github.com/user-attachments/assets/fd4ccf04-6605-41dd-a312-6edebb48a354" />

## Features
- Solve riddles and score points for correct answers.
- Simple user interface with a clean design.
- Scores are tracked throughout the game.

## Setup Instructions

### 1. Clone the repository
To get started, clone the repository to your local machine.

```bash
  git clone https://github.com/your-username/quest-of-the-lost-relics.git
  cd quest-of-the-lost-relics
```
### 2. Install Dependencies

```bash
pip install -r requirements.txt
```
### 3. Setting the Secret Key
For security reasons, the app.secret_key is commented out by default. To run the app locally, you need to uncomment the line in app.py and set a secret key.
```python
# Uncomment the line below and set your own secret key when running the app
# app.secret_key = secrets.token_hex(32)  # Secure session data, generate your own secret key
You can generate your secret key using Python:
```
```python
import secrets
print(secrets.token_hex(32))
```
### 4. Run the Application
To start the game, run the following command in your terminal:

```bash
python app.py
```
This will start the Flask development server. You can access the game by going to http://127.0.0.1:5000 in your browser.

## Future Improvements
- Incorporating storyline
- Styling game over page
- Adding a timer
- Different riddles each session
  
