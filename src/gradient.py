from colorama import init

def gradient(rgb1, rgb2, text):
    """
    Returns the given text with a smooth RGB gradient applied across it.

    :param rgb1: Tuple (R, G, B) start color
    :param rgb2: Tuple (R, G, B) end color
    :param text: The string to apply the gradient to
    :return: Gradient-colored string
    """
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2

    result = ""
    length = len(text.replace("\n", ""))
    if length == 0:
        return text

    index = 0

    for char in text:
        if char == "\n":
            result += "\n"
            continue

        r = int(r1 + (r2 - r1) * index / (length - 1))
        g = int(g1 + (g2 - g1) * index / (length - 1))
        b = int(b1 + (b2 - b1) * index / (length - 1))

        result += f"\033[38;2;{r};{g};{b}m{char}"
        index += 1

    result += "\033[0m"
    return result
