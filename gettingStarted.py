

def welcome_assignment_answers(question):
    if question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":

        answer = "paste_your_hash_here"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = 5
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = int(2)
    elif question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":

        answer = "your_passphrase_from_slack"
    else:
        answer = "Error: Question not recognized"
    return answer


if __name__ == "__main__":
    print(welcome_assignment_answers(
        "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?"))
    print(welcome_assignment_answers("Are encoding and encryption the same? - Yes/No"))
    print(welcome_assignment_answers("Is it possible to decrypt a message without a key? - Yes/No"))
    print(welcome_assignment_answers("Is it possible to decode a message without a key? - Yes/No"))
    print(welcome_assignment_answers("Is a hashed message supposed to be un-hashed? - Yes/No"))
    print(welcome_assignment_answers(
        "What is the SHA256 hashing value of your NYU email and use the answer in your code - "))
    print(welcome_assignment_answers("Is MD5 a secured hashing algorithm? - Yes/No"))
    print(welcome_assignment_answers(
        "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number"))
    print(welcome_assignment_answers(
        "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number"))
    
    
#Questions:
#"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
#"Are encoding and encryption the same? - Yes/No":
#"Is it possible to decrypt a message without a key? - Yes/No":
#"Is it possible to decode a message without a key? - Yes/No":
#"Is a hashed message supposed to be un-hashed? - Yes/No":
#"What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
#"Is MD5 a secured hashing algorithm? - Yes/No":
#"What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
#"What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":

