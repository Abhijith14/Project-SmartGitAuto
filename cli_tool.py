import os
import re

project_dir = os.listdir('.')


# get all branch : .git/refs/remotes/origin/
# get main branch: .git/refs/heads/


# get curr branch: .git/FETCH_HEAD
# commit history : .git/logs/HEAD


def remove_symbols(data, elements=['\n', '\t']):
    for i in elements:
        data = data.replace(i, " ")

    return data


def get_project_name(file_path='.git/config'):
    pconfig = open(file=file_path, mode='r')
    ret_data = []
    for data in pconfig:
        ret_data.append(remove_symbols(data))
    purl = list(filter(lambda v: re.match(' url', v), ret_data))
    purl = purl[0].split(" url = ")

    # extract name from url
    return purl[1].split('/')[-1]


def get_current_branch(file_path='.git/FETCH_HEAD'):
    pconfig = open(file=file_path, mode='r')
    ret_data = []
    for data in pconfig:
        ret_data.append(remove_symbols(data))
    print(ret_data)
    ret_data = ret_data[0].split("'")
    return ret_data[1]


def get_project_version(file_path='.git/logs/refs/heads/'):
    curr_branch = get_current_branch()
    print(curr_branch)
    pconfig = open(file=file_path+str(curr_branch))
    ret_data = []
    for data in pconfig:
        # print(data)
        ret_data.append(remove_symbols(data))
    commit_c = 0
    for i in ret_data:
        commit_c = commit_c + i.count('commit:')

    print(commit_c)

if ".git" in project_dir: # Returns True if it is a git directory.
    print(get_project_name())
    get_project_version()
