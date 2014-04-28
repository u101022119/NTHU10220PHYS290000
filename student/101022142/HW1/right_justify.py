#1-2.right_justify.py
string ="what are you talk about?"
def right_justify(string):
    difference = 70- len(string);
    return (difference*' ')+ string

print(right_justify(string))
