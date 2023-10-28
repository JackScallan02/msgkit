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
from msgkit.logging import logger as l
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

l.giveCode(['testfolder'])
l.debuglog('The DFS is not working correctly')
```

## Development

Want to contribute? Create a new issue and/or make a pull request.

## License

MIT
