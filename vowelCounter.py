def count_vowels(sentence):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in sentence if char in vowels)
    return count
        
sentence = input('Enter a sentence: ')
print('Number of vowels in the sentence is', count_vowels(sentence))

