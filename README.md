# Retrieval-augmented generation

Loosely based on: https://github.com/mikeshwe/retrieval-augmented

## Prerequisites

- Python 3.x
- `virtualenv` (for managing virtual environments)

## Installation

Clone the repository:

```bash
git@github.com:abasallo/rag.git
```

Create the virtual environment:

```bash
virtualenv env
```

Activate the virtual environment:

```bash
source env/bin/activate
```

Install necessary dependencies:

```bash
pip3 install -r requirements.txt
```

Copy .env.example as .env and add the missing secrets as appropriate.

```bash
cp .env.example .env
nano .env
```

## Execution

python3 main.py

## Test

Recommended Query: 

`How should I negotiate my salary and other benefits at work?`

Try directly in: 

https://chat.openai.com/?model=text-davinci-002-render-sha

And through the command-line and compare.
