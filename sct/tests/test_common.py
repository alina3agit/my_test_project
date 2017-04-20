import shlex
import subprocess

from constants import *


def parse_text(text):
    try:
        output = text
    except Exception as e:
        logging.error('Failed.', exc_info=e)
        output = e
    return output


def run_script(command_line):
    args = shlex.split(command_line)
    proc = subprocess.Popen(args, stdout=subprocess.PIPE)
    try:
        outs, errs = proc.communicate()
    except Exception as e:
        logging.error('Failed.', exc_info=e)
        proc.kill()
        outs, errs = proc.communicate()

    output = proc.returncode
    output_text = outs.decode('utf-8').replace('\n', '')

    logging.info('Output_text: ' + output_text)
    if output_text:
        output = parse_text(output_text)

    return output


def test_vocabulary(file_name):
    command_line = "python " + MAIN_SCRIPT_PATH + " " + file_name
    return run_script(command_line)


# Test function for module
def _test():
    assert test_vocabulary(BAD_FILE) == ERROR_CODE
    assert test_vocabulary(GOOD_FILE) == GOOD_ANSWER, 'Result: ' + str(test_vocabulary(GOOD_FILE)) + '  ==  ' + str(GOOD_ANSWER)

if __name__ == '__main__':
    _test()
