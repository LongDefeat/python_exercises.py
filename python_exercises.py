def product(a,b):
    return a * b

def weekday_name(day_of_week):
    Days = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ]

    if day_of_week < 1 or day_of_week > 7:
        return None

    return Days[day_of_week - 1]

def last_element(lst):
    if lst:
        return lst[-1]

def number_compare(a,b):
    if a == b:
        return 'Numbers are equal'
    if a > b:
        return 'First is greater'
    if a < b:
        return 'Second is greater'

def reverse_string(phrase):
    return phrase[::-1]

def single_letter_count(word, letter):
    return word.count(letter)

def multiple_letter_count(phrase):
    count = {}
    for ltr in phrase:
        count[ltr] = count.get(ltr, 0) + 1
    return count

lst = [1,2,3,4,5]

def list_manipulation(lst, command, location, value=None):
    if command == "remove":
        if location == "beginning":
            return lst.pop(0)
        if location == "end":
            return lst.pop()
    elif command == 'add':
        if location == "beginning":
            lst.insert(0, value)
            return lst
        elif location == "end":
            lst.append(value)
            return lst

def is_palindrome(phrase):
    normal = phrase.lower().replace(' ', '')
    rev = ''.join(reversed(normal))
    if phrase == rev:
        return True
    return False

# Their solution
# def is_palindrome(phrase):
#     normalized = phrase.lower().replace(' ', '')
#     return normalized == normalized[::-1]

def frequency(lst, search_term):
    return lst.count(search_term)

def flip_case(phrase, to_swap):
    swap = ""
    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
        swap += ltr
    return swap

def multipy_even_nums(nums):
    product = 1
    for num in nums:
        if num % 2 == 0:
            return product * num
    return product
        
def capitalize(phrase):
    return phrase.capitalize()

def compact(lst):
   return [val for val in lst if val]

def intersection(l1, l2):
    # turns both lists into sets and then makes a list of the common numbers in lists
    return list(set(l1) & set(l2))

def is_even(num):
        return num % 2 == 0  

def is_string(el):
        return isinstance(el, str)  

def partition(lst, fn):

    true_list = []
    false_list = []

    for val in lst:
        if fn(val):
            true_list.append(val)
        else:
            false_list.append(val)
    return [true_list, false_list]

def mode(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    max_value = max(counts.values())
    for (num, freq) in counts.items():
        if freq == max_value:
            return num

def calculate(operation, a, b, make_int=False, message="The result is"):
    if operation == "add":
        res = a + b
    elif operation == "subtract":
        res = a - b
    elif operation == "multiply":
        res = a * b
    elif operation == "divide":
        res = a / b
    else:
        return

    if make_int:
        result = int(res)
    
    return f"{message} {res}"

elmo = ('Elmo', 5, ['hugging', 'being nice'])
sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

def friend_date(a,b):
    if set(a[2]) & set(b[2]):
        return True
    else:
        return False
    # return bool(set(a[2] & set(b[2])))

def triple_and_filter(nums):
    return [num * 3 for num in nums if num % 4 == 0]

def double_and_filter(nums):
    return [num * 2 for num in nums if num % 3 == 0]

names = [
    {'first': 'Ada', 'last': 'Lovelace'},
    {'first': 'Grace', 'last': 'Hopper'},
]

def extract_full_names(people):
   return  [f"{person['first']} {person['last']}" for person in people]

def sum_floats(nums):
    return sum([num for num in nums if isinstance(num, float)])

def list_check(lst):
    # This only returns a boolean if there AT LEAST a list. If bool is removed, then it returns items that are a list
    # return bool([item for item in lst if isinstance(item,list)])
    for item in lst:
        if not isinstance(item, list):
            return False
        return True

def remove_every_other(lst):
    return lst[::2]
    
def sum_pairs(nums, goal):
    checked = set()
    for i in nums: 
        difference = goal - i
        if difference in checked: 
            return (difference, i)
        checked.add(i)
    return ()

def vowel_count(phrase):
    phrase.lower()
    counter = {}

    vowels = set("aeiou")

    for ltr in phrase:
        if ltr in vowels:
            counter[ltr] = counter.get(ltr, 0) + 1
    return counter

def consonant_count(phrase):
    phrase.lower()
    counter = {}

    vowels = set('aeiou')

    for ltr in phrase:
        if ltr not in vowels:
            counter[ltr] = counter.get(ltr, 0) + 1
    return counter

def titleize(phrase):
    return phrase.title()

def find_factors(num):
    # creates list for numbers that are factors of num
    num_list = [n for n in range(1, num // 2 + 1) if num % 2 == 0]
    num_list.append(num)
    return num_list

    # factors = []
    # while (n <= num): 
        # if num % n == 0:
            # factors.append(n)
        # n += 1
    # return factors

def includes(collection, sought, start=None):
    if isinstance(collection, dict):
        return sought in collection.values()
    
    # start is ignored if set because set is unordered
    if start is None or isinstance(collection, set):
        return sought in collection
    return sought in collection[start:]

def repeat(phrase, num):
    if not isinstance(num, int) or num < 0:
        return None
   
    return phrase * num

def truncate(phrase, n): 
    if n < 3:
        return 'Truncation must be at least 3 characters'
    if n > len(phrase) + 2:
        return phrase
    return phrase[:n - 3] + '...'

def two_list_dictionary(keys, values):
    new_dictionary = {}
    for idx, val in enumerate(keys):
        new_dictionary[val] = values[idx] if idx < len(values) else None

    return new_dictionary

nums = [1,2,3,4]

def sum_range(nums, start=0, end=None):
    if end is None:
        end = len(nums)
    return sum(nums[start:end + 1])

def same_frequency(num1, num2):
    num1_str = str(num1)
    num2_str = str(num2)
    num1_len = len(num1_str)
    num2_len = len(num2_str)
    if str(num1_len) == str(num2_len):
        return True
    else: 
        return False
   
def two_oldest_ages(ages):
    unique_ages = set(ages)
    oldest = sorted(unique_ages)[-2:]
    return tuple(oldest)

# AN ALTERNATE WAY
    # oldest = None
    # second = None
    # for age in unique_ages:
    #     if oldest is None or age > oldest:
    #         second = oldest
    #         oldest = ages
    #     elif second is None or age > second:
    #         second = age
    # return (second, oldest)

def find_the_duplicate(nums):
    seen_nums = set()

    for num in nums:
        if num in seen_nums:
            return num
        seen_nums.add(num)

m1 = [
        [1,   2],
        [30, 40],
    ]

def sum_up_diagonals(matrix):
    total = 0

    for i in range(len(matrix)):
        total += matrix[i][i]
        total += matrix[i][-1 - i]
    return total
    # ANOTHER WAY
    # return sum([matrix[i][i] + matrix[i][-1 - i] for i in range(len(matrix))])

def min_max_keys(d):
    keys = d.keys()
    return (min(keys), max(keys))

def find_greater_numbers(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                count += 1
    return count