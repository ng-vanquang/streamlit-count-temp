# Streamlit Visitor Counter App

A simple Streamlit application that tracks and displays the number of visitors to your web app. The visitor count persists between application restarts using a text file for storage.

## Features

- Tracks unique visits (counted on app initialization and page reloads)
- Persists visitor count to a file
- Maintains state between application restarts
- Clean and simple user interface

## Prerequisites

- Python 3.6 or higher
- Virtual environment (recommended)

## Installation

1. Clone this repository or download the files:
```bash
git clone <repository-url>
# or download manually
```

2. Create and activate a virtual environment:
```bash
# Windows
virtualenv myEnv
myEnv\Scripts\activate

# Unix/macOS
virtualenv myEnv
source myEnv/bin/activate
```

3. Install the required packages:
```bash
pip install streamlit
```

## Usage

1. Run the Streamlit application:
```bash
# Windows
myEnv\Scripts\streamlit.exe run app.py

# Unix/macOS
streamlit run app.py
```

2. Open your web browser and navigate to:
```
http://localhost:8501
```

The application will display the current visitor count, which increments with each new visit or page reload.

## How It Works

- The app uses a text file (`visitor_count.txt`) to store the visitor count
- Each time the app initializes or a user reloads the page, the count increments
- Streamlit's session state prevents double-counting during the same session
- The count persists between application restarts

## Project Structure

```
Streamlit_access_count/
├── app.py              # Main application file
├── visitor_count.txt   # File storing the visitor count
└── README.md          # This documentation
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE).