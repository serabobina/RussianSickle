import Colors


def bruteForce(string, brute_range, decode_func):
    answer = ''

    for i in range(*brute_range):
        answer += Colors.decode_color + f'KEY [{i}]: '

        cracked_string = decode_func(string, i)
        answer += Colors.greed_color + cracked_string + '\n'
    return answer.rstrip()
