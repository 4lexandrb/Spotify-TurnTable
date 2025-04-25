# Spotify TurnTable

## Overview
Spotify TurnTable is a web application that allows users to interact with their Spotify playlists. The application features a dynamic interface where users can change the background image based on their playlists and activate various functions through buttons.

## Project Structure
```
Spotify-TurnTable
├── static
│   ├── css
│   │   └── styles.css       # Contains CSS styles for the application
│   ├── js
│   │   └── scripts.js       # Contains JavaScript code for functionality
│   └── images               # Directory for storing images
├── templates
│   └── index.html           # Main HTML template for the application
├── app
│   ├── __init__.py          # Initializes the Flask application
│   ├── routes.py            # Defines the routes for the application
│   └── utils.py             # Contains utility functions
├── main.py                  # Entry point of the application
├── requirements.txt         # Lists project dependencies
└── README.md                # Documentation for the project
```

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd Spotify-TurnTable
   ```

2. **Install dependencies**:
   Make sure you have Python and pip installed. Then run:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Execute the following command to start the Flask application:
   ```
   python main.py
   ```

4. **Access the application**:
   Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Usage
- Upon accessing the application, you will be prompted to log in to your Spotify account.
- After authentication, you will be redirected to the main interface where you can view your playlists.
- Use the buttons provided to change the background image and activate various functions related to your playlists.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.