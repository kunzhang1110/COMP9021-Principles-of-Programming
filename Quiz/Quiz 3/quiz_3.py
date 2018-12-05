# Prompts the user for a word and outputs the list of
# all subwords of the word of height 1.
#
# Written by Kun Zhang for COMP9021


def extract_subwords(word):
    i = 0    # start index pointer

    out = []
    # elminate redundant whitespace 
    word = word.split()
    word = "".join(word)
    last_index = len(word) - 1

      
    while i <= last_index:  
        P_count = 0    # parenthese counter
        flag = 1    # flag to increment i
        first_P_index = 0
  #      print("i=",i,word[i])

        for j in range(i, last_index + 1):
       #     print("j=",j,word[j], "P_count =", P_count)        
            if word[j] == "(":
                P_count += 1
                
            if P_count == 0:
                if word[j] == ",":
                    i = j + 1
                    flag = 0
                    break
            elif P_count == 1:
                if word[j] == "(":
                    P1 = j
                
                if word[j] == ")":
                    out.append(word[i:j+1]) 
                    i = j + 1
                    flag = 0
                    break
            else:   # when P_count > 1
                    i = P1
                    break

        if flag == 1:
            i += 1

    # insert back spaces
    for i in range(len(out)):
        for j in range(len(out[i])):
            if out[i][j] == ",":
                out[i] = out[i][:j] + ", " + out[i][j+1:]
    
    return out
        


word = input('Enter a word: ')
#word = "f1(f2(f3(a,b), c), f2(a, f3(a,b)), f2(bcb), f2(0,f3(eeee)))"
print('The subwords of "{:}" of height 1 are:\n    {:}'.
                                        format(word, extract_subwords(word)))
