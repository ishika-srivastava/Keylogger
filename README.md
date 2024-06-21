# Keylogger

## Overview

A keylogger is a program that records the keys pressed on a keyboard. This project demonstrates a simple keylogger implemented in Python that logs keystrokes to a file.

## Features

- Capture keystrokes using `pynput`
- Log keystrokes to a file
- Run the keylogger in the background
- Sending logs via email
- Simple and easy to understand

## Setup

### Clone the repository:

```
$ git clone https://github.com/ishika-srivastava/Keylogger.git
$ cd Keylogger
```

### Install dependencies:

```
$ pip install -r requirements.txt
```

## Usage

### Run the keylogger:

```
$ python keylogger.py
```

### Run the keylogger in background:

```
$ python keylogger_in_background.py
```

## Logging

The application, logs keystrokes in a structured file format. Logs are stored in key_log.txt. Integrated encryption for secure storage and transmission of logs.

## Background Execution

Utilized Python's threading capabilities to run the keylogger in the background, minimizing system resource usage.

## Notes

- Ensure Python 3.12.0 and the required libraries are installed.
- Customize encryption settings or network configurations as needed.
- To stop the keylogger program, press the 'Esc' key

## Further Considerations

#### - Ehtics and Legality

- Always use keyloggers responsibly and ethically.
- Ensure you have explicit permission from the device owner.

#### - Detection and Prevention

- Understand hoe keyloggers can be detected and prevented to improve your cybersecurity skills
- Implement additional security measures to prevent unauthorized access to the keylogger logs.

## Author

Ishika Srivastava</br>
Contact: ishika.srivastava029@gmail.com
