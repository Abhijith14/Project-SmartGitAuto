from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

g = Github(os.environ("ACCESS_TOKEN"))
current_user = g.get_user()

print(current_user.login)
# all_repo = []
# for repo in g.get_repos():
#     all_repo.append(repo)
#
# print(len(all_repo))

repo = g.get_repo("Abhijith14/Portfolio-v2")
print(repo.get_contents("README.md").decoded_content)




