"""
def test():
    epic_fail()
def epic_fail():
    raise Exception('Failing hard!')
test()
"""

import traceback

try:
    raise Exception('This is the error message.')
    print('Hello!')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')