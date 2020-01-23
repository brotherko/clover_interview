import textwrap
import tempfile


def mockFileName(str):
    temp = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
    temp.writelines(textwrap.dedent(str))
    temp.close()
    return temp.name
