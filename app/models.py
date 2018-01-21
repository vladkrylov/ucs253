import html

def rot13alg(s):
    result = ''
    roi = [(ord('a'), ord('z')),
           (ord('A'), ord('Z'))]
    for c in s:
        ascii = ord(c)
        for low, high in roi:
            if ascii >= low and ascii <= high:
                result_ascii = ascii + 13
                if result_ascii > high:
                    result_ascii += low - high - 1
                result += chr(result_ascii)
                break
        else:
            result += c
    return html.escape(result)

