# Advanced Keylogger

This project is an advanced keylogger script written in Python. It logs keystrokes and periodically sends the log file to a specified email address. This script is strictly for educational purposes. Unauthorized use of keyloggers is illegal and unethical.

## Features

- Logs all keystrokes.
- Sends log file via email at regular intervals.
- Runs in the background as a hidden process.
- Multi-threaded for efficient operation.

## Requirements

- Python 3.x
- Required Python libraries:
  - `pynput`
  - `smtplib` (built-in)
  - `ssl` (built-in)
  - `threading` (built-in)

## Installation

1. Install the required libraries:
    ```bash
    pip install pynput
    ```

2. Clone this repository or download the `optimized_keylogger.py` script.

3. Update the script with your email credentials:
    ```python
    email_address = "your_email@example.com"
    email_password = "your_password"
    recipient_email = "recipient_email@example.com"
    ```

## Usage

1. Run the script:
    ```bash
    python optimized_keylogger.py
    ```

2. The keylogger will start logging keystrokes and sending the log file via email every 5 minutes.

3. To stop the keylogger, press the `esc` key.

## Configuration

- **log_file**: Path to the log file. Default is `keylog.txt`.
- **email_interval**: Interval for sending emails, in seconds. Default is 300 seconds (5 minutes).
- **email_address**: Your email address.
- **email_password**: Your email password.
- **recipient_email**: The recipient's email address.

## Important Notes

- **Ethical and Legal Considerations**:
  - Obtain explicit permission from all users of the device.
  - Inform users about the logging and obtain consent.
  - Adhere to local laws and regulations.

This script is provided strictly for educational purposes. Unauthorized deployment or use of this software is illegal and unethical. Always respect privacy and obtain proper permissions before using any keylogging software.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
