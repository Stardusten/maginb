from typing import Union, Optional


def ansi_stylize(
    text: str,
    fg: Optional[Union[str, int]] = None,
    bg: Optional[Union[str, int]] = None,
    bold: bool = False,
    italic: bool = False,
    underline: bool = False
    ):
    """
    使用 ANSI 转义字符设置文本的前景色、背景色、粗体、斜体和下划线

    :param text: 要设置样式的文本
    :param fg: 前景色名称或代码 (如 'red', 31)
    :param bg: 背景色名称或代码 (如 'blue', 44)
    :param bold: 是否使用粗体 (默认为 False)
    :param italic: 是否使用斜体 (默认为 False)
    :param underline: 是否使用下划线 (默认为 False)
    :return: 带有 ANSI 转义字符的文本
    """
    # 字典映射颜色名称到 ANSI 代码
    colors = {
        "black": 0, "red": 1, "green": 2, "yellow": 3,
        "blue": 4, "magenta": 5, "cyan": 6, "white": 7
    }

    # ANSI 转义序列的构建
    codes = []

    if bold:
        codes.append('1')  # ANSI 代码 1: 粗体
    if italic:
        codes.append('3')  # ANSI 代码 3: 斜体
    if underline:
        codes.append('4')  # ANSI 代码 4: 下划线

    if isinstance(fg, str) and fg.lower() in colors:
        codes.append(str(30 + colors[fg.lower()]))  # 文本颜色代码，如红色是 31
    elif isinstance(fg, int):
        codes.append(str(fg))  # 直接使用数字代码

    if isinstance(bg, str) and bg.lower() in colors:
        codes.append(str(40 + colors[bg.lower()]))  # 背景色代码，如蓝色是 44
    elif isinstance(bg, int):
        codes.append(str(bg))  # 直接使用数字代码

    # 将所有的代码组合成一个转义序列，并应用到文本中
    start = '\x1b[' + ';'.join(codes) + 'm'
    end = '\x1b[0m'  # 重置所有属性
    return f"{start}{text}{end}"


LEVEL_STYLE_MAP = {
    'NOTEST': {
        'fg': 'black',
    },
    'DEBUG': {
        'fg': 'magenta',
    },
    'INFO': {
        'fg': 'blue',
    },
    'WARNING': {
        'fg': 'yellow',
    },
    'ERROR': {
        'fg': 'red',
    },
    'SUCCESS': {
        'fg': 'green',  
    },
    'CRITICAL': {
        'fg': 'red',
        'bold': True,
        'underline': True,
    }
}


def logging(msg: str, level: str):
    level_styles = LEVEL_STYLE_MAP[level]
    text = f'[{ansi_stylize(level, **level_styles)}] {msg}'
