import requests
import sys

def install_dependencies():
    try:
        import requests
    except ImportError:
        print("Installing required dependencies...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        print("Dependencies installed successfully.")

def get_forked_repos(username, token, page=1, per_page=100):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    params = {
        "type": "fork",
        "page": page,
        "per_page": per_page
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def delete_repo(username, repo_name, token):
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.delete(url, headers=headers)
    response.raise_for_status()
    print(f"Deleted: {repo_name}")

def get_remaining_forks(username, token):
    url = f'https://api.github.com/users/{username}/repos'
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    params = {'type': 'fork'}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return len(response.json())

def delete_all_forks(username, token):
    deleted_count = 0
    page = 1
    while True:
        repos = get_forked_repos(username, token, page)
        if not repos:
            break
        
        for repo in repos:
            delete_repo(username, repo['name'], token)
            deleted_count += 1
        
        page += 1

    remaining_forks = get_remaining_forks(username, token)
    print(f'Total repositories deleted: {deleted_count}')
    print(f'Total forked repositories remaining: {remaining_forks}')

def main():
    install_dependencies()

    username = input("Enter your GitHub username: ")
    token = input("Enter your GitHub access token with delete_repo permission: ")

    confirm = input("Are you sure you want to delete all your forked repositories? (yes/no): ")
    if confirm.lower() != "yes":
        print("Operation cancelled.")
        sys.exit(0)

    try:
        delete_all_forks(username, token)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()