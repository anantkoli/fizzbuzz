from __future__ import absolute_import
from common.constants import max_int, min_int, max_len, min_len


def validate_param(param, op_type=str, name=''):
    # should validate as we want to avoid the sql injection attacks if any
    # op param > int, str
    try:
        val = op_type(param)
        if op_type == str:
            try:
                check = int(param)
                message = "ValueError: Please enter {} as a string.".format(name)
                raise Exception(message)
            except ValueError:
                pass
            return val.strip(" ").replace(" ", "").replace("/", "")
        else:
            return val
    except ValueError:
        message = "ValueError: Please enter {} as {}.".format(name, op_type)
        raise Exception(message)


def validate_range(param, dtype=str, name=''):
    if dtype == int:
        if min_int <= param <= max_int:
            return param
        else:
            message = "Please use the range for {} in between {} to {}.".format(name, min_int, max_int)
            raise Exception(message)
    elif dtype == str:
        if min_len <= len(param) <= max_len:
            return param
        else:
            message = "Please use the word length for {} in range {} to {}.".format(name, min_len, max_len)
            raise Exception(message)


if __name__ == "__main__":
    print(validate_param(3, int, name='num1'))
    print(validate_param('fizz', name='str1'))
    print(validate_range(100, int))
    print(validate_range('buzz'))
