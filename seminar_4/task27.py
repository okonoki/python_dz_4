# Пользователь вводит текст (строка).
# Словом считается последовательность непробельных символов идущих подряд, слова разделены одним пробелом.
# Определите, сколько различных слов содержится в этом тексте.

# Input: She sells sea shells on the sea shore
# The shells that she sells are sea shells I'm sure
# So if she sells sea shells on the sea shore
# I'm sure that the shells are sea shore shells

# Output: 13

words = '''She sells sea shells on the sea shore
The shells that she sells are sea shells I'm sure
So if she sells sea shells on the sea shore
I'm sure that the shells are sea shore shells'''.lower()

print(words)

# she sells sea shells on the sea shore
# the shells that she sells are sea shells i'm sure
# so if she sells sea shells on the sea shore
# i'm sure that the shells are sea shore shells

words = words.split()

print(words)

# ['she', 'sells', 'sea', 'shells', 'on', 'the', 'sea', 'shore', 'the', 'shells', 'that', 'she', 'sells', 'are', 'sea',
# 'shells', "i'm", 'sure', 'so', 'if', 'she', 'sells', 'sea', 'shells', 'on', 'the', 'sea', 'shore', "i'm", 'sure',
# 'that', 'the', 'shells', 'are', 'sea', 'shore', 'shells']

words = set(words)

print(words)

# {'if', 'shells', 'on', 'she', 'shore', "i'm", 'sea', 'are', 'so', 'sells', 'that', 'sure', 'the'}

words = len(words)

print(words)  # 13
