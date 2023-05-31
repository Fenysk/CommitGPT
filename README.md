# CommitGPT

CommitGPT is a script that automates the generation of commit messages for your Git project. This script uses the OpenAI GPT-3.5 Turbo model to generate brief summaries of changes made to a project and commit messages based on those changes. 

## Prerequisites

- An OpenAI account and API key
- Python installed
- The GitPython package installed 
- The python-dotenv package installed 

## Installation

1. Clone this repository or download the script :

```bash
git clone https://github.com/Fenysk/CommitGPT.git
```

2. Install the required Python packages :

```bash
pip install gitpython python-dotenv openai
```

3. Create a .env file in the same directory as your script and define your OpenAI informations :

```py
OPENAI_API_KEY="[YOUR API KEY]"
OPENAI_ORGANIZATION="[YOUR ORGANIZATION ID]"
```

## Usage

To run the script, execute the following command :

```bash
python CommitGPT.py
```

After running, the script will :

1. Retrieve the modified files added with git add.
2. Generate a brief summary of changes made to the project.
3. Ask for your approval of the generated summary. If not approved, you can choose to regenerate the summary or manually input a summary.
4. Generate a commit message using the approved summary.
5. Ask for your approval of the generated commit message. If not approved, you can regenerate the commit message or quit the process.
6. Perform the commit with the approved commit message.