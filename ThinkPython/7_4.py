def eval_loop():
    while True:
        prompt = raw_input('> ')
        if prompt == 'done':
            break
        answer = eval(prompt)
        print answer

eval_loop()
