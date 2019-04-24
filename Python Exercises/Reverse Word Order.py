def reverse_sentence(sent):
    new_list = sent.split()
    return ' '.join([new_list[itr] for itr in range(len(new_list) - 1, -1, -1)])


# Another Solution

def reverseWord(word):
    return ' '.join(word.split()[::-1]
                    )


print(reverse_sentence(input('Please enter sentence to be reversed: ')))