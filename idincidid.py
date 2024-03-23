def cprint(text, color='white', attrs=[], **kwargs):
    """
    Print text with specified color and attributes.

    Colors:
        'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'

    Attributes:
        'bold', 'dark', 'underline', 'blink', 'reverse', 'concealed'

    Example:
        cprint('Hello, world!', 'red', 'bold')
        cprint('Hello, world!', color='red', attrs=['bold'])
    """
    colors = {
        'black': 30,
        'red': 31,
        'green': 32,
        'yellow': 33,
        'blue': 34,
        'magenta': 35,
        'cyan': 36,
        'white': 37,
    }
    attributes = {
        'bold': 1,
        'dark': 2,
        'underline': 4,
        'blink': 5,
        'reverse': 7,
        'concealed': 8,
    }
    fmt_str = '\033[{};{}m'.format(';'.join(str(attributes.get(attr, 0)) for attr in attrs), colors.get(color, 39))
    reset_str = '\033[0m'
    text = '{}{}{}'.format(fmt_str, text, reset_str)
    print(text, **kwargs)
