This is a short python script I wrote to generate secure, memorable passwords using the xkcd password method.
Reference https://xkcd.com/936/

To run the script, make sure you have python version 3.X in your path, then run this command from the project root directory:
  
  LINUX or MAC
    
    ./xkcdpwgen.py
    
  WINDOWS
    
    python xkcdpwgen.py
    
To see this additional usage information, just run the command above followed by -h or --help:

    usage: xkcdpwgen.py [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]
    
    Generate a secure, memorable password using the XKCD method
    
    optional arguments:
      -h, --help            show this help message and exit
      -w WORDS, --words WORDS
                            include WORDS in the password (default=4)
      -c CAPS, --caps CAPS  capitalize the first letter of CAPS random words
                            (default=0)
      -n NUMBERS, --numbers NUMBERS
                            insert NUMBERS random numbers in the password
                            (default=0)
      -s SYMBOLS, --symbols SYMBOLS
                            insert SYMBOLS random symbols in the password
                            (default=0)
