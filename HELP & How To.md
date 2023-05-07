# T1A3 Weather CLI Help Documentation

## Dependencies & System/Hardware Requirements

The T1A3 Weather CLI depends on the following libraries:

- requests

These dependencies will be installed automatically to the virtual enviroment when running the run.sh script.

- Operating System: Windows, macOS, or Linux
- Python version: 3.10 or higher

## Installation and Use

### Installation

1. Ensure you have Python 3.10 or higher installed on your system. You can download the latest version of Python from https://www.python.org/downloads/.

2. Clone or download the T1A3 Weather CLI repository.

3. Open a terminal or command prompt and navigate to the root directory of the T1A3 Weather CLI.

   ```bash
   cd /path/to/your/directory
   ```

   Replace /path/to/your/directory with the actual path to the folder containing the run.sh script.
   The contents of the directory should look like this:

   ```bash
   .
   ├── EXPORTS
   ├── README.md
   ├── main.py
   ├── requirements.txt
   ├── run.sh
   └──
   ```

4. Run the following command to set up and activate a virtual environment:

   ```bash
   ./run.sh
   ```

   This will create a virtual environment in the root directory of the T1A3 Weather CLI and install the required dependencies.

   If the file is not executable, you will need to run the following command then run the previous command again:

   ```bash
   chmod +x run.sh
   ```

   if you are using Windows, you will need to run the following commands instead:

   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

   This will create a virtual environment, install the required dependencies from the requirements.txt file, activate the virtual environment and run the program.

### Using the T1A3 Weather CLI

when you ran the run.sh script, the virtual environment was activated and the program was run. If you exited the program, you can run it again by executing the following command again in the root directory of the T1A3 Weather CLI:

1.  Run the run.sh script:
      
    ```bash
    ./run.sh
    ```
    The application will start, and the main menu will be displayed.

```
[s] Select City
[1] Display Current weather for Selected City
[2] Display Current day forecast for Selected City
[3] Display 7 day Weather History for Selected City
[4] Export data options
[q] Quit Program
```

2.  Choose an option by entering the corresponding number or letter:

3.  Follow the on-screen instructions to perform the desired operation.
4.  To exit the application, enter 'q' at the any time.

## Command Line Arguments

The T1A3 Weather CLI application does not use any command-line arguments. Instead, it features an interactive user interface that allows you to perform various operations.
