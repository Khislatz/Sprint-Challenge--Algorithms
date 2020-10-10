  
'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    if not word:
        return count
    else:
        if word[:2]=='th':
            count +=1 
        return count + count_th(word[1:])               

string = input(str("Enter a string:"))
print(f'There are {count_th(string)} "th" in the word {string}.')

# string = "abcthxyz"
# print(f'There are {count_th(string)} "th" in the word {string}.')