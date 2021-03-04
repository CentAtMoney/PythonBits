import sys

from collections import OrderedDict

#I, II, III, IV, V, VI, VII, VIII, IX, X, XI, XII, XIII, XIV, XV, XVI, XVII, XVIII, ... IL, L, LI, ... C, ... D, ... M, ...
#1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, ... 49, 50, 51, ... 100, ... 500, ... 1000, ...

d = OrderedDict({1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V'})

def lookup(di, value):

    for k, v in di.items():
        if v == value:
            return k

    return None

def decode(s):
    """fucked roman numeral decoder"""    
    val = 0
    

    if len(s) < 1:
        return val
    
    is_neg = s[0] == '-'
    if is_neg and len(s) > 2:
        s = s[1::]

    for i in range(len(s)):
        
        print(i)
        c = 'M'
        if (c == 'I') and (i != (len(s) - 1)):
            if s[i + 1] != 'I':
                val += int(lookup(d, s[i + 1])) - 1
                s = s[2::]
            elif s[i + 1] == 'I':
                val += 1
        else:
            val += int(lookup(d, s[i]))

    return val

def main(argv):
    
    val = 893

    print(encode(val))
    print(decode(val))

def encode(num):
    """Mediocre roman numeral encoder"""
    encoding = ""

    if num < 0:
        encoding += '-'
        num = abs(num)
    
   #loop over the dictionary of number: symbol
    for k in d:
        
        #append the number of multiples of the symbol
        for i in range(((num + 1) // k) - 1):
            encoding += d[k]
        #if one less than the key append I + key 
        if (num + 1) % k == 0:
            num -= k - 1
            encoding += 'I' + d[k]
        #else just finish off appending the symbols
        elif (num // k) > 0:
            encoding += d[k]
        
        #all else fails we try to add 1 through 3 inc. and append the corrosponding number of I's
        for i in range(1, 4):
            if num + i == k:
                encoding += 'I'
        
        num = num % k
    
    return encoding
      
if __name__ == "__main__": main(sys.argv)
