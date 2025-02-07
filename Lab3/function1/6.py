def reverse_words():
    sentence = input()
    words = sentence.split()
    
    reversed_sentence = ""
    for word in reversed(words):
        reversed_sentence += word + " "
    
    print(reversed_sentence.strip())

reverse_words()