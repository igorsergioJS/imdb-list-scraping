# Movie Dataset Generator

This repository contains a Python code for extracting movie information from an IMDb list and generating a dataset in JSON and CSV formats.

## Configuration

Before running the code, make sure to replace the following variables according to your needs:

```python
link_list = "INSERT LINK TO THE MOVIE LIST HERE"
num_pages = INSERT NUMBER OF PAGES IN THE LIST HERE
```

Make sure to provide the correct link to the desired movie list and the total number of pages present in the list.

## Requirements

Make sure you have the following requirements installed:

- Python 3.x
- requests library
- BeautifulSoup library

You can install the dependencies by running the following command:

```
pip install requests beautifulsoup4
```

## Running the Code

After configuring the variables and installing the dependencies, you can run the Python code `scraping-imdb.py`. It will extract the movie information from the list and generate the JSON and CSV files.

The command to run the code is:

```
python scraping-imdb.py
```

## Results

Upon completion of the execution, the following files will be generated:

- `movies.json`: JSON file containing the movie information.
- `movies.csv`: CSV file containing the movie information.

The files will be saved in the same directory where the code was executed.

**Note:** Make sure that the `ex_file.json` and `ex_file.csv` files do not exist in the directory before execution, as those names are used in the example code.

If everything goes smoothly, you will see the message "Files saved successfully: movies.json and movies.csv" in the terminal.

Feel free to adjust the code or add more functionality as needed. Enjoy exploring the IMDb movie list!
