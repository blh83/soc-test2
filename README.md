Please do not spend more than 3 hours on this.
# SOC Test
## Instructions
1. Fork this repo
2. Write a small app that accepts a csv file as an upload. The csv file is a contact list. The contents of the list need to be inserted into a database. There needs to be a way to view and delete after the upload.
4. Either demonstrate in code or provide an explanation in this README on how you would handle very large files.
5. Either demonstrate in code or provide an explanation in this README on how you would handle different encodings.
6. Submit this as a pull request.


For very large files I would have broken the parsing of the csv (and saving to the database) into chunks using python's chunks() function.  For example "for chunk in csv_file.chunks(): save the data".  Usually, you also have to make changes to nginx to accept files above a certain size. 


For different encodings, if it's just unicode and utf-8 I'd have to worry about, I'd use the encode() function of python.  However, this is not always really reliable and frankly you have to mess around with it a bit.  If multiple encodings are expected, then I'd probably have to write a table that detects the encoding and decodes it to the correct type for storage in the database.

NOTE: The layout of the pages I've submitted, are by no means ideal.  Flow and user experience would be accounted for better (and I don't have buttons that navigate between the pages), but I tried to keep it simple for the sake of getting functionality correct.
