## MSGKIT

MsgKit is a Python library that provides you with in-code solutions to your bugs. It utilizes the OpenAI API by feeding in your code, the error, and getting a response at run-time.

## Features

- Import the logger object and use any of the documented functions

## Installation

All that is needed to use MsgKit is:
```sh
pip install msgkit
```

## Example usage:
```
l.giveCode(['directory']) #Gives the name of the directory which contains the files of the code.
l.debuglog('The DFS is not working correctly') #Give it the bug
```

## Development

Want to contribute? Create a new issue and/or make a pull request.

## License

MIT
