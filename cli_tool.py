import os
import re

project_dir = os.listdir('.')


# get all branch : .git/refs/remotes/origin/
# get main branch: .git/refs/heads/


# get curr branch: .git/FETCH_HEAD
# commit history : .git/logs/HEAD


def remove_symbols(data, elements=['\n', '\t']):
    for i in elements:
        data = data.replace(i, "")

    return data


def get_project_name(file_path='.git/config'):
    pconfig = open(file=file_path, mode='r')
    ret_data = []
    for data in pconfig:
        ret_data.append(remove_symbols(data))
    purl = list(filter(lambda v: re.match('url', v), ret_data))
    purl = purl[0].split("url = ")

    # extract name from url
    return purl[1].split('/')[-1]


def get_project_version(file_path=''):



if ".git" in project_dir: # Returns True if it is a git directory.
    print(get_project_name())

