import os
import sys

pythonpath = os.getenv('PYTHONPATH', '')

if pythonpath != '':
    pythonpath += ':'

currentpath = os.path.dirname(os.path.abspath(__file__))

os.environ["PYTHONPATH"] = f"{pythonpath}{currentpath}"

run_command = f"python apps/{sys.argv[1]}.py"

os.system(run_command)
