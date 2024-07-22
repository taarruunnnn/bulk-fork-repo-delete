# Bulk Fork Repo Delete

This Python script allows you to bulk delete all forked repositories from your GitHub account.

## Features

- Deletes all forked repositories from a GitHub account
- Handles pagination to delete more than 20 repositories at a time
- Provides a count of deleted repositories
- Shows the number of remaining forked repositories after deletion

## Prerequisites

- Python 3.x
- GitHub account
- Personal access token with `delete_repo` permission

## Installation

1. Clone this repository or download the script.
2. Install the required dependencies:

```bash
pip install requests
```

## Usage

1. Run the script:

```bash
python delete_forks.py
```

2. Enter your GitHub username when prompted.
3. Enter your GitHub personal access token when prompted.
4. Confirm that you want to delete all forked repositories.

## Warning

This script will delete ALL forked repositories in your GitHub account. This action is irreversible. Make sure you have backups or don't need any of the forked repositories before running this script.

## How It Works

1. The script uses the GitHub API to fetch all forked repositories for the given user.
2. It then iterates through each repository and deletes it.
3. The process continues until all forked repositories are deleted.
4. Finally, it provides a summary of deleted and remaining repositories.

## Author

Tarun Ghosh

## Acknowledgments

- GitHub API Documentation
- Requests library
