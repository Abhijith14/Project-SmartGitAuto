import os
import re
import time

import requests

project_dir = os.listdir('.')
types = ['Script/Python', 'Script/Web', 'Script', 'Website(PHP)', 'Website(Django)', 'Website', 'Computer Vision', 'Machine Learning', 'Automation']
python_list = ['Script/Python', 'Website(Django)', 'Computer Vision', 'Machine Learning', 'Automation']


res = []
for (dir_path, dir_names, file_names) in os.walk('.'):
    res.extend(file_names)



def create_readme(NAME, VERSION, LINK, TYPE):
    PROJECT_NAME, PROJECT_VERSION, PROJECT_LINK, PROJECT_TYPE, PROJECT_LOGO = NAME, VERSION, LINK, TYPE, "assets/logo.png"
    readme_file_content = ""
    # heading
    with requests.get('https://raw.githubusercontent.com/Abhijith14/Project-SmartGitAuto/master/readme_samples/heading.md') as f:
        text = f.text
        text = text.replace('{{PROJECT_NAME}}', PROJECT_NAME)
        text = text.replace('{{PROJECT_LOGO}}', PROJECT_LOGO)
        text = text.replace('{{PROJECT_VERSION}}', PROJECT_VERSION)
        text = text.replace('{{PROJECT_LINK}}', PROJECT_LINK)
        text = text.replace('{{PROJECT_TYPE}}', PROJECT_TYPE)

    readme_file_content = readme_file_content + text + "\n\n<br>\n"

    if PROJECT_TYPE in python_list:
        with requests.get('https://raw.githubusercontent.com/Abhijith14/Project-SmartGitAuto/master/readme_samples/python-env.md') as f:
            text = f.text

        readme_file_content = readme_file_content + text + "\n\n<br>\n\n"

    # Todo: run

    # project assistance
    with requests.get('https://raw.githubusercontent.com/Abhijith14/Project-SmartGitAuto/master/readme_samples/project-assistance.md') as f:
        text = f.text
        text = text.replace('{{PROJECT_NAME}}', PROJECT_NAME)
        text = text.replace('{{PROJECT_LINK}}', PROJECT_LINK)

    readme_file_content = readme_file_content + text + "\n\n<br>\n\n"

    # BUILD AND AUTHOR
    with requests.get('https://raw.githubusercontent.com/Abhijith14/Project-SmartGitAuto/master/readme_samples/build_with_and_authors.md') as f:
        text = f.text

    readme_file_content = readme_file_content + text + "\n\n<br>\n\n"

    # PLAGARISM
    with requests.get('https://raw.githubusercontent.com/Abhijith14/Project-SmartGitAuto/master/readme_samples/plagarism.md') as f:
        text = f.text
        text = text.replace('{{PROJECT_NAME}}', PROJECT_NAME)
        text = text.replace('{{PROJECT_LINK}}', PROJECT_LINK)

    readme_file_content = readme_file_content + text + "\n\n<br>\n\n"

    f_write = open("README.md", 'w', encoding="utf-8")
    f_write.write(readme_file_content)
    f_write.close()


def remove_symbols(data, elements=['\n', '\t']):
    for i in elements:
        data = data.replace(i, " ")

    return data


def get_project_name(desc=0, file_path='.git/config'):
    pconfig = open(file=file_path, mode='r')
    ret_data = []
    for data in pconfig:
        ret_data.append(remove_symbols(data))
    purl = list(filter(lambda v: re.match(' url', v), ret_data))
    purl = purl[0].split(" url = ")

    # extract name from url
    pname = purl[1].split('/')[-1]
    if desc == 0:
        print("Project Name : ", pname)
    else:
        print("Project Description : None")
    return pname


def get_current_branch(file_path='.git/HEAD'):
    pconfig = open(file=file_path, mode='r')
    ret_data = []
    for data in pconfig:
        ret_data.append(remove_symbols(data))
    ret_data = ret_data[0].split("/")
    return ret_data[-1][:-1]


def get_project_version(file_path='.git/logs/refs/heads/'):
    curr_branch = get_current_branch()
    pconfig = open(file=file_path+str(curr_branch))
    ret_data = []
    for data in pconfig:
        # print(data)
        ret_data.append(remove_symbols(data))
    commit_c = 0
    for i in ret_data:
        commit_c = commit_c + i.count('commit:')

    project_ver = str((commit_c/10) + 1) + ".0"

    print("Project Version : ", project_ver)
    return project_ver


def is_django():
    if 'manage.py' in res:
        return True
    else:
        return False


def is_Python():
    if not is_django():
        for files in res:
            if str(files).endswith('.py'):
                return True

    return False


def is_website():
    for files in res:
        if str(files).endswith(".html"):
            return True
    return False


def is_php():
    for files in res:
        if str(files).endswith(".php"):
            return True
    return False


def return_project_type():
    if is_Python():
        if is_django():
            return types[4]
        else:
            return types[0]
    elif is_website():
        if is_php():
            return types[3]
        else:
            return types[5]
    else:
        return types[2]


def check_git_folder(dir_):
    if ".git" in dir_:
        return True
    return False


def create_config_file(config_file):
    try:
        try:
            os.mkdir('.SmartGitAuto')
        except OSError:
            pass

        fmain_w = open('.SmartGitAuto/config', "w")
        fmain_w.writelines(config_file)
        fmain_w.close()
    except Exception as e:
        print("Error Code : ", e)
        exit(0)
    return True


def get_project_type():
    print()
    curr_project_type = return_project_type()
    print("{} detected as project type".format(curr_project_type))
    choice = input("Do you wish to make a change ? (Y|N)")
    print()
    def_types = list(enumerate(types))
    if choice == 'Y' or choice == 'y':
        print("Enter a new project type or select from the default types.")
        print("Default types are : ", (str(def_types).replace("[", "")).replace("]", ""))
        print()
        choice_types = input("Project Type : ")
        if choice_types.isdigit():
            choice_types = int(choice_types)
        set_ = 0
        for type_ in def_types:
            if choice_types in type_:
                set_ = 1
                curr_project_type = type_[1]
                break
        if set_ == 0:
            curr_project_type = choice_types

    else:
        print("Project Type :", curr_project_type, "set.")

    return curr_project_type


def get_project_link(file_path='.git/config'):
    pconfig = open(file=file_path, mode='r')
    ret_data = []
    for data in pconfig:
        ret_data.append(remove_symbols(data))
    purl = list(filter(lambda v: re.match(' url', v), ret_data))
    purl = purl[0].split(" url = ")

    return purl[-1]


def getData():
    print("Initialising SmartGitAuto..")
    print("Checking for .git folder :", check_git_folder(project_dir))
    print()
    project_name = get_project_name()
    project_desc = get_project_name(1)
    project_link = get_project_link()
    project_version = get_project_version()
    project_branch = get_current_branch()
    project_type = get_project_type()

    if check_git_folder(project_dir):
        print("===========================================================")
        print("Scraping Repo Data ! : Kindly wait...")
        time.sleep(0.5)
        print()
        repo_config = ["project: \n"]
        try:
            repo_config.append("\tname: " + project_name + "\n")
            time.sleep(0.5)
            repo_config.append("\tdescription: " + project_desc + "\n")
            time.sleep(0.5)
            repo_config.append("\tversion: " + project_version + "\n")
            time.sleep(0.5)
            repo_config.append("\tbranch: " + project_branch + "\n")
            repo_config.append("\ttype: " + project_type + "\n")

        except Exception as e:
            print("Error Code : ", e)
            exit(0)
        print("===========================================================")
        if not create_config_file(repo_config):
            print("Error Unknown !!")

    else:
        print("This folder is not a git workspace. Initialise git and rerun the script !")

    create_readme(project_name, project_version, project_link, project_type)


def create_gitignore():
    url = "https://raw.githubusercontent.com/Abhijith14/Project-SmartGitAuto/master/.gitignore"
    resp = requests.get(url)
    gitignore_filew = open('.gitignore', 'w')
    gitignore_filew.write(resp.text)
    gitignore_filew.close()


def create_license(license="GPL3"):
    if license == "GPL3":
        url = "https://raw.githubusercontent.com/Abhijith14/Project-SmartGitAuto/master/LICENSE"

    if url:
        resp = requests.get(url)
        gitl_filew = open('LICENSE', 'w')
        gitl_filew.write(resp.text)
        gitl_filew.close()
    else:
        print("URL Retrieval Failed !!")


def main():
    getData()
    create_gitignore()
    create_license()


if __name__ == '__main__':
    main()
