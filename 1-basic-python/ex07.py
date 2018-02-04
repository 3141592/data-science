def domainGet(input):
    start = input.find('@')
    end = input.find(' ', start) + 1
    print(input[start:end])
    print(input)

domainGet('user@domain.com')
