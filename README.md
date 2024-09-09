# Screenshot_Assist
A simple desktop application for taking screenshots and scheduling automatic screenshots. Built with Python using `customtkinter` for the GUI and `Pillow` for capturing screenshots.

## Features

- **Take Screenshot**: Capture the current screen and save the image.
- **Timer**: Schedule automatic screenshots after a specified delay.
- **Hotkeys**: Use keyboard shortcuts to take screenshots and start the timer.

## Installation

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Installing Dependencies

To install the necessary Python packages, you can use `pip`:

```bash
pip install pillow keyboard customtkinter
```

### Running the App

1. **Clone the Repository**

   ```bash
   git clone https://github.com/PRATIKK0709/Screenshot_Assist/.git
   cd screenshot-app
   ```

2. **Run the Executable**

   - For Windows, navigate to the `bin` directory and run the executable:
     ```bash
     bin/ScreenshotApp.exe
     ```

3. **Running from Source**

   If you want to run the app from source (Python script), ensure you have the dependencies installed and execute:

   ```bash
   python src/main.py
   ```

## Usage

1. **Take Screenshot**: Click the "Take Screenshot" button in the GUI or use the keyboard shortcut `Ctrl+S`.
2. **Start Timer**: Enter a delay in seconds and click "Start Timer" or use the keyboard shortcut `Ctrl+D` to start automatic screenshots after the specified delay.

## Keyboard Shortcuts

- `Ctrl+S`: Take a screenshot immediately.
- `Ctrl+D`: Start the timer for automatic screenshots.

## Contributing

If you have suggestions or improvements, please fork the repository and submit a pull request. For major changes, open an issue to discuss what you would like to change.

