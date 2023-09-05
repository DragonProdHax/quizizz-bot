# Quizizz Bot
`quizizzBot` is a Python bot that provides functionalities to join Quizizz games, fetch the list of players, create dummy bots.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Methods](#methods)
- [Usage](#usage)
- [License](#license)
- [Contribution](#contribution)
- [Version](#version)

## Features
- Join Quizizz games using a join code.
- List players in the game.
- Create dummy players with customizable names.
- Optionally, automatically create exam-like conditions.
- Microsoft Edge WebDriver (for headless browsing)
- Chrome WebDriver (for headless browsing)

## Prerequisites
Before using QuizizzBot, make sure you have the following installed

- Python 3.x
- Selenium
- BeautifulSoup4
- Requests
- Microsoft Edge WebDriver (for headless browsing)
- Chrome WebDriver (for headless browsing)

You can install the required Python libraries using pip

```bash
pip install selenium beautifulsoup4 requests
```

## Installation
1. Clone the repository or download the source code to your local machine.
```bash
git clone https://github.com/FaceND/quizizz-bot.git
```
3. Make sure you have Python installed on your system.
4. Before using `quizizzBot`, make sure you have the required libraries installed
5. You may also need to download the appropriate WebDriver for your browser (e.g., ChromeDriver or EdgeDriver) and add it to your system's PATH.

## Methods

### checkStatus()
> ### Key Features
- Checks the status of a URL and returns the HTTP status code.
- Handles connection errors and HTTP errors.
> ### Method
- `url`: The URL to be checked.
##
### generateBotName()
> ### Key Features
  - Generates a random bot name with a specified minimum and maximum character length.
> ### Method
  - `min_chr`: The minimum number of characters for the generated name.
  - `max_chr`: The maximum number of characters for the generated name.
##
### listPlayer()
> ### Key Features
  - Lists players in the Quizizz game.
  - Optionally, you can choose to show the player list and set a maximum waiting time.
> ### Method
  - `show_listPlayer`: Set to `True` to display the list of players (default is `True`).
  - `max_waitTime`: Maximum time to wait for elements to load (default is 30 seconds).
##
### dummy()
> ### Key Features
  - Simulates a player joining a Quizizz game with a given name.
  - Can handle duplicate access and other errors.
  - Optionally, you can create an automated exam with the `makeAutoExam` parameter.
> ### Method
  - `name`: The name of the dummy player.
  - `makeAutoExam`: Set to True to simulate exam-like conditions (default is False).
  - `max_waitTime`: Maximum time to wait for elements to load (default is 30 seconds).
##
### mutiDummy()
> ### Key Features
  - Spawns multiple dummy players concurrently using Python's multiprocessing.
  - You can specify the number of processes, a list of names, and other options.
> ### Method
  - `num_processes`: The number of dummy players to create concurrently.
  - `NameList`: A list of names for dummy players (default is an empty list).
  - :construction:`makeAutoExam`: Set to `True` to simulate exam-like conditions (default is `False`). 
  - `max_waitTime`: Maximum time to wait for elements to load (default is 30 seconds).
##
### :warning:getAnswer():warning: 
> ### Key Features
  -  :construction: Under Development
> ### Method
  - :construction: Under Development

## Usage
To use the `quizizzBot` class, you can create an instance and call its methods as shown below
> Remember to replace `'your_join_code'` and `'Your Name'` with the appropriate values for your use case. You can also customize the documentation further to include more details about your project.

### Example 1
```python
from Quizizz import quizizzBot

# Initialize the quizizzBot with the join code
quizz = quizizzBot(join_code='your_join_code')

# List players in the game
players = quizz.listPlayer()
print("Players in the game:", players)
```

### Example 2
```python
from Quizizz import quizizzBot

# Instantiate the bot
quizz = quizizzBot(join_code='your_join_code')

# List players in the waiting room
quizz.listPlayer()

# Create and run dummy players
quizz.dummy('Dummy1', makeAutoExam=True)
quizz.dummy('Dummy2', makeAutoExam=False)
```

### Example 3
```python
from Quizizz import quizizzBot

# Initialize the quizizzBot with the join code
quizz = quizizzBot(join_code='your_join_code')

BotList = ['Bot1', 'Bot2', 'Bot3']

if __name__ == '__main__':
    # Create multiple dummy players concurrently with random names
    quizz.mutiDummy(num_processes=len(BotList), NameList=BotList, makeAutoExam=True)

    # Create multiple dummy players concurrently with random names
    quizz.mutiDummy(num_processes=3, makeAutoExam=True)
```

## Contribution
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or create a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
This project was inspired by the need for automating Quizizz games for educational purposes.

## Version
- Version: 23.9.5
