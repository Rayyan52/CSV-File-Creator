
# CSV File Creator

This Python script generates a CSV file containing a predefined set of questions and answers related to the Cold War and its proxy wars, such as Vietnam, Afghanistan, and South America.

## Features

- Creates a CSV file with  rows of questions and answers.
- The data is focused on the Cold War, proxy wars, and significant historical events.
- the data can be inserted of your own choice too
  

## File Output

The script generates a CSV file named `Cold_War_ProxyWars_QA.csv`. This file contains:
- A header row with two columns: "Question" and "Answer".
- make sure to provide the file path for the CSV file

## Prerequisites

- Python 3.x installed on your system.

## Usage

1. Save the script to a file, e.g., `create_csv.py`.
2. Run the script using the command:

   ```bash
   python create_csv.py
   ```

3. The CSV file `Cold_War_ProxyWars_QA.csv` will be created in the specified directory.

## Customization

- To change the questions and answers, edit the `questions_answers` list in the script.
- To save the CSV file in a different location, update the `file_path` variable in the script.

## Example Output

The CSV file will look like this:

| Question                                  | Answer                                       |
|-------------------------------------------|----------------------------------------------|
| What years did the Cold War span?         | 1947 to 1991                                |
| What were the two main opposing powers?   | The United States and the Soviet Union      |
| ...                                       | ...                                         |

## License

This project is provided as-is without warranty. Feel free to modify and use it for educational purposes.
