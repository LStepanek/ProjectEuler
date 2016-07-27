# Number letter counts
# Problem 17

def letters(n):
    if n == 1000:
        return(len('onethousand'))

    numbers = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
            'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
            'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
            'eighty', 'ninety']
    name = ''

    if n // 100 is not 0:
        name += numbers[n // 100] + 'hundred'
        n -= (n // 100) * 100
        if n is not 0:
            name += 'and'
    if n >= 20 and n // 10 is not 0:
        name += tens[n // 10]
        n -= (n // 10) * 10
    if n is not 0:
        name += numbers[n]
    return(len(name))

print(sum(letters(i) for i in range(1001)))
