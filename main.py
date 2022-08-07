from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

g = Github(os.environ["ACCESS_TOKEN"])
current_user = g.get_user()

print(current_user.login)

# Repo Object
repo = g.get_repo("Abhijith14/TestRepo-SmartGitAuto")

# check for contents
contents = repo.get_contents("")
all_files = []
while contents:
    file_content = contents.pop(0)
    print(file_content.type)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))
    else:
        file = file_content
        all_files.append(str(file).replace('ContentFile(path="', '').replace('")', ''))

print(repo.language)
print(all_files)

# if ".SmartGitAuto" in all_files:



