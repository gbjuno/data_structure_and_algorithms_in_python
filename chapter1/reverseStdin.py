def reverseStdin():
    stdin = []
    try:
        while True:
            stdin.append(raw_input('input >'))
    except EOFError:
        print
        stdout = stdin[-1::-1]
        for i in stdout:
            print i

reverseStdin()


