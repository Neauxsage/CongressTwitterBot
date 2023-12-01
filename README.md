# CongressTwitterBot

ALL.PY
•	Runs the following scripts in a specific order:

PDF.PY
•	Opens an Excel Workbook
•	Accesses a Specific Worksheet
•	Parses and Cleans URLs
•	Saves Data to Excel
•	Web Scraping Setup
•	Navigates to a URL
•	Extracts Links
•	Selects a New Link
•	Saves the Original and Cleaned Links
•	Closes the Web Browser


BILL.PY
•	Retrieves the current working directory.
•	Loads an Excel workbook named 'links.xlsx' and accesses a specific sheet 'text'.
•	Extracts a hyperlink from cell A1 of the sheet.
•	Parses the URL to create a document title, replacing slashes with hyphens.
•	Sets up Selenium WebDriver for Chrome, using ChromeDriverManager for driver management.
•	Opens the extracted hyperlink in a Selenium-controlled browser.
•	Waits up to 10 seconds for an element with the ID 'bill-summary' to load on the webpage.
•	Retrieves the text content of the 'bill-summary' element.
•	Closes the Selenium WebDriver.
•	Creating and Saving a Word Document:
•	Initializes a new Word document.
•	Adds the retrieved text from the webpage to the document.
•	Saves the Word document in a 'texts' folder within the current working directory, with a filename based on the parsed URL.
•	Executing the Script: Runs the main function if the script is executed as the main program.


TEST.PY
•	Initial Setup:
•	Imports necessary libraries.
•	Sets up logging for terminal output.
•	Defines API keys for Tweepy (Twitter API client) and OpenAI.
•	Initializes Tweepy and OpenAI clients.
•	Document Processing:
•	Identifies the script's running directory.
•	Retrieves Word documents from a specified 'texts' directory.
•	Randomly selects one of these documents.
•	Reads the selected document and splits its content into chunks.
•	Summary Generation:
•	For each chunk of the document, uses OpenAI's GPT model to generate a summary.
•	Handles retries in case of rate limit errors from OpenAI.
•	Combines all chunk summaries into a single text.
•	Tweet Generation and Posting:
•	Generates a tweet-sized summary from the combined text, adhering to Twitter's character limit.
•	Posts the tweet using Tweepy if it's within the character limit.
•	Handles errors and excessive attempts in tweet generation.
•	File Management:
•	Moves the processed document to an 'archive' directory.
•	Clears the 'texts' directory after processing.
•	Spreadsheet Update (Error Handling):
•	In case of a tweet error, deletes all documents in 'texts'.
•	Updates and manages a 'links' spreadsheet, deleting the last row if needed.

DEL.PY
•	Word Count in .docx Files: It defines a function count_words_in_docx to count the number of words in a .docx file.
•	Listing Files: It lists all the files in the directory ./texts/.
•	File Deletion Flag: Initializes a flag file_deleted to track if any file is deleted during the script's execution.
•	File Processing:
•	Iterates over each file in the ./texts/ directory.
•	For each file ending with .docx (indicating a Word document):
•	Counts the number of words in the document.
•	Prints the file name and its word count.
•	If the word count exceeds 5,000 words:
•	Prints a message indicating the file is being deleted.
•	Deletes the file.
•	Sets the file_deleted flag to True.
•	Conditional Script Execution:
•	If any file has been deleted (i.e., if file_deleted is True), it runs a Python script named all.py.

CLEARXL.PY
•	Retrieves the current working directory using os.getcwd().
•	Constructs the file path for an Excel workbook named 'links.xlsx' located in the current directory.
•	Loads the Excel workbook located at the constructed path.
•	Selects a sheet within the workbook named "text".
•	Deletes all rows in the "text" sheet, effectively clearing all cells.
•	Saves the changes made to the workbook.
•	Closes the workbook to free up system resources.
•	Prints a message indicating the successful clearance of the cells.
