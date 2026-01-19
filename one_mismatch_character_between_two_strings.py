#one mismatch cjaracter from two strings(remember for single mismatch use xor, if they ask multiple then use frequency counting)
# Take input string s (original string)
s = input()

# Take input string t (shuffled version of s with one extra character)
t = input()

# Initialize a variable to store the XOR result
# We start with 0 because XOR with 0 keeps the value unchanged:
#   x ^ 0 = x
res = 0

# Loop through each character in string s
for ch in s:
    # ord(ch) converts the character into its ASCII integer value
    # Example: ord('a') = 97
    #
    # XOR (^) has an important property:
    #   same_number ^ same_number = 0
    #
    # This means characters that appear in BOTH s and t
    # will cancel each other out when XORed
    res ^= ord(ch)

# Loop through each character in string t
for ch in t:
    # XOR again with ASCII value of each character in t
    #
    # Since t contains all characters of s PLUS one extra character,
    # all common characters from s and t cancel out,
    # and only the extra character's ASCII value remains in 'res'
    res ^= ord(ch)

# At this point, 'res' stores the ASCII value of the extra character
#
# chr(res) converts the ASCII value back to a character
# Example: chr(97) = 'a'
print(chr(res))
