# Project Directory Builder

This tool was created for developers who are able to envision their application in a file structure and remove the time it takes to create all the new files and directories. With not only saving developers time when building their projects, but also keeping projects organized, achievable, and tidy.

## Usage

Run the following script: `python main.py`

### CLI Arguments

You are able to pass the following arguments to the script above 

| Arg         | Shorthand | Type  | Description                                                 | Default Value
| -           | -         | -     | -                                                           | -
| `--file`    | `-f`      | `str` | `The .md file to parse and find the directory tree schema.` | `README.md`
| `--heading` | `-h`      | `str` | `The text to start the parsing at.`                         | `Directory Tree Schema`

### Formatting the File

The program will scan the file passed as the argument to `--file` and try to find the following text: `

---

# Dev Notes

## Directory Tree Schema
file_ext=[.py, .md, .txt]
```
- project-directory-builder
  - .vscode
  - .venv
  - src
    - schema_builder.py
    - project_builder.py
    - utils
      - constants.py
  - .gitignore
  - main.py
  - README.md
  - requirements.txt
```
