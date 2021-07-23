"""
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.
In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'.
For this problem, any other format of periods such as '...' are treated as file/directory names.
The canonical path should have the following format:

    The path starts with a single slash '/'.
    Any two directories are separated by a single slash '/'.
    The path does not end with a trailing '/'.
    The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')

Return the simplified canonical path.
"""


def simplifyPath(path):
    stack = [e for e in path.split('/') if e != '' and e != '.']
    result = []
    for e in stack:
        if e == '..':
            if result:
                result.pop()
        else:
            result.append(e)
    return '/' + '/'.join(result)

if __name__ == '__main__':
    path = "/home/"
    print(simplifyPath(path))
    # Returns /home

    path = "/home//foo/"
    print(simplifyPath(path))
    # Returns /home/foo

    path = "/a/./b/../../c/"
    print(simplifyPath(path))
    # Returns /c