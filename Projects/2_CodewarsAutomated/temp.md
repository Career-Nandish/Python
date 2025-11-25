# Codewars Challenges


# Table of Contents

1. [The Hashtag Generator](##1-the-hashtag-generator)
2. [Human Readable Time](##2-human-readable-time)
3. [Simple Pig Latin](##3-simple-pig-latin)
4. [Moving Zeros To The End](##4-moving-zeros-to-the-end)
5. [Rot13](##5-rot13)
6. [Directions Reduction](##6-directions-reduction)
7. [Product of consecutive Fib numbers](##7-product-of-consecutive-fib-numbers)
8. [Number Pairs](##8-number-pairs)
9. [Convert a Boolean to a String](##9-convert-a-boolean-to-a-string)
10. [Sort Numbers](##10-sort-numbers)
11. [Find the unique number](##11-find-the-unique-number)
12. [Give me a Diamond](##12-give-me-a-diamond)
13. [Consecutive strings](##13-consecutive-strings)
14. [Find the stray number](##14-find-the-stray-number)
15. [Two Sum](##15-two-sum)
16. [Find the next perfect square!](##16-find-the-next-perfect-square)
17. [Calculating with Functions](##17-calculating-with-functions)
18. [Beginner Series #3 Sum of Numbers](##18-beginner-series-3-sum-of-numbers)
19. [Mumbling](##19-mumbling)
20. [Duplicate Encoder](##20-duplicate-encoder)
21. [Convert a string to an array](##21-convert-a-string-to-an-array)
22. [Unique In Order](##22-unique-in-order)
23. [Odd or Even?](##23-odd-or-even)
24. [Highest Scoring Word](##24-highest-scoring-word)
25. [Playing with digits](##25-playing-with-digits)
26. [Sort the odd](##26-sort-the-odd)
27. [Take a Number And Sum  Its Digits Raised To The Consecutive Powers And ....¡Eureka!!](##27-take-a-number-and-sum--its-digits-raised-to-the-consecutive-powers-and-eureka)
28. [Bouncing Balls](##28-bouncing-balls)
29. [Mexican Wave](##29-mexican-wave)
30. [Build a pile of Cubes](##30-build-a-pile-of-cubes)
31. [Write Number in Expanded Form](##31-write-number-in-expanded-form)
32. [Replace With Alphabet Position](##32-replace-with-alphabet-position)
33. [Shortest Word](##33-shortest-word)
34. [Take a Ten Minutes Walk](##34-take-a-ten-minutes-walk)
35. [Count the smiley faces!](##35-count-the-smiley-faces)
36. [You only need one - Beginner](##36-you-only-need-one---beginner)
37. [Isograms](##37-isograms)
38. [Build Tower](##38-build-tower)
39. [Persistent Bugger.](##39-persistent-bugger)
40. [Tribonacci Sequence](##40-tribonacci-sequence)
41. [String ends with?](##41-string-ends-with)
42. [Equal Sides Of An Array](##42-equal-sides-of-an-array)
43. [Number of People in the Bus](##43-number-of-people-in-the-bus)
44. [Exes and Ohs](##44-exes-and-ohs)
45. [DNA to RNA Conversion](##45-dna-to-rna-conversion)
46. [You're a square!](##46-youre-a-square)
47. [Break camelCase](##47-break-camelcase)
48. [Sum of odd numbers](##48-sum-of-odd-numbers)
49. [Beginner Series #1 School Paperwork](##49-beginner-series-1-school-paperwork)
50. [Highest and Lowest](##50-highest-and-lowest)
51. [Is he gonna survive?](##51-is-he-gonna-survive)
52. [Ones and Zeros](##52-ones-and-zeros)
53. [Convert number to reversed array of digits](##53-convert-number-to-reversed-array-of-digits)
54. [Convert boolean values to strings 'Yes' or 'No'.](##54-convert-boolean-values-to-strings-yes-or-no)
55. [Get the Middle Character](##55-get-the-middle-character)
56. [Two to One](##56-two-to-one)
57. [Printer Errors](##57-printer-errors)
58. [Binary Addition](##58-binary-addition)
59. [Categorize New Member](##59-categorize-new-member)
60. [Keep Hydrated!](##60-keep-hydrated)
61. [Beginner - Lost Without a Map](##61-beginner---lost-without-a-map)
62. [Complementary DNA](##62-complementary-dna)
63. [Sum Arrays](##63-sum-arrays)
64. [Reverse words](##64-reverse-words)
65. [Area or Perimeter](##65-area-or-perimeter)
66. [Fake Binary](##66-fake-binary)
67. [Remove String Spaces](##67-remove-string-spaces)
68. [Sentence Smash](##68-sentence-smash)
69. [Return Negative](##69-return-negative)
70. [Counting sheep...](##70-counting-sheep)
71. [Convert a String to a Number!](##71-convert-a-string-to-a-number)
72. [If you can't sleep, just count sheep!!](##72-if-you-cant-sleep-just-count-sheep)
73. [Find Maximum and Minimum Values of a List](##73-find-maximum-and-minimum-values-of-a-list)
74. [Sum without highest and lowest number](##74-sum-without-highest-and-lowest-number)
75. [Opposites Attract](##75-opposites-attract)
76. [Are You Playing Banjo?](##76-are-you-playing-banjo)


## Challenges

## [1. The Hashtag Generator](https://www.codewars.com/kata/52449b062fb80683ec000024)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![5 kyu](https://img.shields.io/badge/5%20kyu-important?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Strings, Algorithms|
|`Completed On`|2024-07-24T12:24:37.974+0000|


## Description 

The marketing team is spending way too much time typing in hashtags.   

Let's help them with our own Hashtag Generator!



Here's the deal:



- It must start with a hashtag (`#`).

- All words must have their first letter capitalized, and remaining letters lowercased.



- If the final result is longer than 140 chars it must return `false`.

- If the input or the result is an empty string it must return `false`.

## Examples



" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"

"    Hello     World   "                  =>  "#HelloWorld"

""                                        =>  false



## Code 

```python
def generate_hashtag(s):
    if len(s) == 0:
        return False
    else:
        res = "#" + "".join([w.title() for w in s.strip().split()])
        if len(res) > 140:
            return False
        else:
            return res

```

## [2. Human Readable Time](https://www.codewars.com/kata/52685f7382004e774f0001f7)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![5 kyu](https://img.shields.io/badge/5%20kyu-important?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Date Time, Mathematics, Algorithms|
|`Completed On`|2024-07-24T12:10:16.466+0000|


## Description 

Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (`HH:MM:SS`)



* `HH` = hours, padded to 2 digits, range: 00 - 99

* `MM` = minutes, padded to 2 digits, range: 00 - 59

* `SS` = seconds, padded to 2 digits, range: 00 - 59



The maximum time never exceeds 359999 (`99:59:59`)



You can find some examples in the test fixtures.

## Code 

```python
def make_readable(seconds):
    hour, res = divmod(seconds,3600)
    mins, sec =  divmod(res,60)
    return f"{hour:02}:{mins:02}:{sec:02}"
```

## [3. Simple Pig Latin](https://www.codewars.com/kata/520b9d2ad5c005041100000f)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![5 kyu](https://img.shields.io/badge/5%20kyu-important?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Regular Expressions, Algorithms|
|`Completed On`|2024-07-24T11:19:04.885+0000|


## Description 

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.



## Examples



```python
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
```





## Code 

```python
def pig_it(text):
    return " ".join([(word[1:] + word[0] + "ay") if word.isalpha() else word for word in text.split()])
```

## [4. Moving Zeros To The End](https://www.codewars.com/kata/52597aa56021e91c93000cb0)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![5 kyu](https://img.shields.io/badge/5%20kyu-important?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Arrays, Sorting, Algorithms|
|`Completed On`|2024-07-24T11:12:03.489+0000|


## Description 

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.



```python
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
```





## Code 

```python
def move_zeros(lst):
    return [i for i in lst if i!=0] + [0] * lst.count(0)
```

## [5. Rot13](https://www.codewars.com/kata/530e15517bc88ac656000716)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![5 kyu](https://img.shields.io/badge/5%20kyu-important?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Ciphers, Fundamentals|
|`Completed On`|2024-07-24T10:56:27.257+0000|


## Description 

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.



Create a function that takes a string and returns the string ciphered with Rot13. 

If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".



```if:python
Please note that using `encode` is considered cheating.
```





## Code 

```python
def rot13(message):
    rot13 = ""
    for c in message:
        if c.isupper():
            rot13 += chr(65+ (ord(c) -65 + 13)%26)
        elif c.islower():
            rot13 += chr(97+ (ord(c) -97 + 13)%26)
        else:
            rot13 += c
    return rot13
```

## [6. Directions Reduction](https://www.codewars.com/kata/550f22f4d758534c1100025a)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![5 kyu](https://img.shields.io/badge/5%20kyu-important?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals|
|`Completed On`|2024-07-18T11:20:46.194+0000|


## Description 

#### Once upon a time, on a way through the old wild *mountainous* west,…



… a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too. 



Going to one direction and coming back the opposite direction *right away* is a needless effort. Since this is the wild west, with dreadful weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!



#### How I crossed a *mountainous* desert the smart way.



The directions given to the man are, for example, the following (depending on the language):



```
["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
or
{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
or
[North, South, South, East, West, North, West]
```

You can immediately see that going "NORTH" and *immediately* "SOUTH" is not reasonable, better stay to the same place!

So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:



```
["WEST"]
or
{ "WEST" }
or
[West]
```



#### Other examples:



In `["NORTH", "SOUTH", "EAST", "WEST"]`, the direction `"NORTH" + "SOUTH"` is going north and coming back *right away*. 



The path becomes `["EAST", "WEST"]`, now `"EAST"` and `"WEST"` annihilate each other, therefore, the final result is `[]` (nil in Clojure).



In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are *not* directly opposite but they become directly opposite after the reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].



#### Task



Write a function `dirReduc` which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N *side by side*).



- The Haskell version takes a list of directions with `data Direction = North | East | West | South`. 

- The Clojure version returns nil when the path is reduced to nothing. 

- The Rust version takes a slice of `enum Direction {North, East, West, South}`.

- The OCaml version takes a list of `type direction = | North | South | East | West`.



#### See more examples in "Sample Tests:"



#### Notes



- Not all paths can be made simpler. 

The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not *directly* opposite of each other and can't become such. Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].

- if you want to translate, please ask before translating.

## Code 

```python
def dir_reduc(a):
    i = 0
    while i < len(a) - 1:
        if len(a[i]) == len(a[i+1]) and (a[i] != a[i+1]):
            a.pop(i)
            a.pop(i)
            i = 0
        else:
            i+=1
    return a

```

## [7. Product of consecutive Fib numbers](https://www.codewars.com/kata/5541f58a944b85ce6d00006a)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![5 kyu](https://img.shields.io/badge/5%20kyu-important?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Algorithms, Mathematics|
|`Completed On`|2024-07-17T12:37:00.249+0000|


## Description 

The Fibonacci numbers are the numbers in the following integer sequence (`Fn`):

`0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...`



such that:



```math
F(0) = 0\\F(1) = 1\\F(n) = F(n-1) + F(n-2)
```



Given a number, say `prod` (for product), we search two Fibonacci numbers `F(n)` and `F(n+1)` verifying:

```math
F(n) * F(n+1) = prod
```

## Code 

```python
def product_fib(prod):
    a, b = 0, 1
    while (a*b) < prod:
        a, b = b, b + a 
    return [a, b, prod == (a*b)]
```

## [8. Number Pairs](https://www.codewars.com/kata/563b1f55a5f2079dc100008a)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![7 kyu](https://img.shields.io/badge/7%20kyu-white?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Arrays, Fundamentals|
|`Completed On`|2024-07-13T21:34:01.865+0000|


## Description 

In this kata the aim is to compare each pair of integers from two arrays, and return a new array of large numbers.



Note: Both arrays have the same dimensions.



#### Example:



```python
arr1 = [13, 64, 15, 17, 88]
arr2 = [23, 14, 53, 17, 80]
get_larger_numbers(arr1, arr2) == [23, 64, 53, 17, 88]
```



  



## Code 

```python
def get_larger_numbers(a, b):
    return list(map(lambda x, y : max(x, y), a, b))
```

## [9. Convert a Boolean to a String](https://www.codewars.com/kata/551b4501ac0447318f0009cd)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![8 kyu](https://img.shields.io/badge/8%20kyu-lightgrey?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Strings, Fundamentals|
|`Completed On`|2024-07-13T21:27:40.757+0000|


## Description 

Implement a function which convert the given boolean value into its string representation.



Note: Only valid inputs will be given.





## Code 

```python
def boolean_to_string(b):
    return "True" if b else "False"
```

## [10. Sort Numbers](https://www.codewars.com/kata/5174a4c0f2769dd8b1000003)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![7 kyu](https://img.shields.io/badge/7%20kyu-white?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals|
|`Completed On`|2024-07-13T21:27:09.219+0000|


## Description 

Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.



For example:



```python
solution([1,2,3,10,5]) # should return [1,2,3,5,10]
solution(None) # should return []
```





## Code 

```python
def solution(nums):
    return sorted(nums) if nums else []
```

## [11. Find the unique number](https://www.codewars.com/kata/585d7d5adb20cf33cb000235)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![6 kyu](https://img.shields.io/badge/6%20kyu-FFFF00?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals, Algorithms, Arrays, Performance|
|`Completed On`|2024-07-13T21:21:51.932+0000|


## Description 

There is an array with some numbers. All numbers are equal except for one. Try to find it!



```python
find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
```



It’s guaranteed that array contains at least 3 numbers.



The tests contain some very huge arrays, so think about performance.



This is the first kata in series:



1. Find the unique number (this kata)

2. [Find the unique string](https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3)

3. [Find The Unique](https://www.codewars.com/kata/5862e0db4f7ab47bed0000e5)

## Code 

```python
def find_uniq(arr):
    return [i for i in set(arr) if arr.count(i) == 1][0] 
```

## [12. Give me a Diamond](https://www.codewars.com/kata/5503013e34137eeeaa001648)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![6 kyu](https://img.shields.io/badge/6%20kyu-FFFF00?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Strings, ASCII Art, Fundamentals|
|`Completed On`|2024-07-13T21:08:56.346+0000|


## Description 

Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help.



## Task



You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (`*`) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (`\n`).



Return `null/nil/None/...` if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.



## Examples



A size 3 diamond:



```
 *
***
 *
```



...which would appear as a string of `" *\n***\n *\n"`



A size 5 diamond:



```
  *
 ***
*****
 ***
  *
```



...that is: 

```
"  *\n ***\n*****\n ***\n  *\n"
```

## Code 

```python
def diamond(n):
    if n%2 ==0 or n <=0:
        return None
    res = [(" " * (n//2-i)) + ("*" * (2*i + 1)) for i in range(n//2 + 1)]
    res += res[:n//2][::-1]
    return "\n".join(res) + "\n"
```

## [13. Consecutive strings](https://www.codewars.com/kata/56a5d994ac971f1ac500003e)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![6 kyu](https://img.shields.io/badge/6%20kyu-FFFF00?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals|
|`Completed On`|2024-07-12T19:10:16.160+0000|


## Description 

You are given an array(list) `strarr` of strings and an integer `k`. Your task is to return the **first** longest string

consisting of k **consecutive** strings taken in the array.



#### Examples:

```
strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

Concatenate the consecutive strings of strarr by 2, we get:

treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so 
longest_consec(strarr, 2) should return "folingtrashy".

In the same way:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
```

n being the length of the string array, if `n = 0` or `k > n` or `k <= 0` return "" (return `Nothing` in Elm, "nothing" in Erlang).



#### Note

consecutive strings : follow one after another without an interruption

## Code 

```python
def longest_consec(s, k):
    return max(["".join(s[i:i+k]) for i in range(len(s))], key=lambda a:len(a)) if 0 < k <= len(s) else ""
```

## [14. Find the stray number](https://www.codewars.com/kata/57f609022f4d534f05000024)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![7 kyu](https://img.shields.io/badge/7%20kyu-white?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals, Algorithms|
|`Completed On`|2024-07-12T18:32:43.477+0000|


## Description 

You are given an *odd-length* array of integers, in which all of them are the same, except for one single number.



Complete the method which accepts such an array, and returns that single different number.



**The input array will always be valid!** (odd-length >= 3)



## Examples



```
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3
```

## Code 

```python
def stray(arr):
    return min(arr, key=arr.count)
```

## [15. Two Sum](https://www.codewars.com/kata/52c31f8e6605bcc646000082)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![6 kyu](https://img.shields.io/badge/6%20kyu-FFFF00?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Arrays, Fundamentals, Algorithms|
|`Completed On`|2024-07-12T18:19:30.758+0000|


## Description 

Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indexes of these items should then be returned in a tuple / list (depending on your language) like so: `(index1, index2)`.



For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.



The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).



Based on: https://leetcode.com/problems/two-sum/



```python
two_sum([1, 2, 3], 4) # returns (0, 2) or (2, 0)
two_sum([3, 2, 4], 6) # returns (1, 2) or (2, 1)
```



  



## Code 

```python
def two_sum(numbers, target):
    res = ()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (i, j)
```

## [16. Find the next perfect square!](https://www.codewars.com/kata/56269eb78ad2e4ced1000013)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![7 kyu](https://img.shields.io/badge/7%20kyu-white?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Algebra, Fundamentals|
|`Completed On`|2024-07-11T12:19:54.872+0000|


## Description 

You might know some pretty large perfect squares. But what about the NEXT one?



Complete the `findNextSquare` method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.  



If the argument is itself not a perfect square then return either `-1` or an empty value like `None` or `null`, depending on your language. You may assume the argument is non-negative.



## Examples ( Input --> Output )



```
121 --> 144
625 --> 676
114 --> -1  #  because 114 is not a perfect square
```





## Code 

```python
def find_next_square(sq):
    return ((sq**0.5) + 1)**2 if (sq**0.5).is_integer() else -1

```

## [17. Calculating with Functions](https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![5 kyu](https://img.shields.io/badge/5%20kyu-important?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Functional Programming|
|`Completed On`|2024-07-11T11:52:53.862+0000|


## Description 

This time we want to write calculations using functions and get the results. Let's have a look at some examples:



```python
seven(times(five()))    #  must return 35
four(plus(nine()))      #  must return 13
eight(minus(three()))   #  must return 5
six(divided_by(two()))  #  must return 3
```



Requirements:

* There must be a function for each number from 0 ("zero") to 9 ("nine")

* There must be a function for each of the following mathematical operations: plus, minus, times, divided_by

* Each calculation consist of exactly one operation and two numbers

* The most outer function represents the left operand, the most inner function represents the right operand

* Division should be **integer division**. For example, this should return `2`, not `2.666666...`:

```python
eight(divided_by(three()))
```





## Code 

```python
def evaulate(opd1, right):
    opt, opd2 = right.split()
    if right[0] == "+":
        return int(opd1) + int(opd2)
    elif right[0] == "-":
        return int(opd1) - int(opd2)
    elif right[0] == "*":
        return int(opd1) * int(opd2)
    else:
        return int(opd1) // int(opd2)

def zero(right = None): 
    if not right:
        return "0"
    else:return evaulate("0", right)
def one(right=None): 
    if not right:
        return "1"
    else:return evaulate("1", right)
def two(right=None): 
    if not right:
        return "2"
    else:return evaulate("2", right)
def three(right=None): 
    if not right:
        return "3"
    else:return evaulate("3", right)
def four(right=None): 
    if not right:
        return "4"
    else:return evaulate("4", right)
def five(right=None): 
    if not right:
        return "5"
    else:return evaulate("5", right)
def six(right=None): 
    if not right:
        return "6"
    else:return evaulate("6", right)
def seven(right=None): 
    if not right:
        return "7"
    else:return evaulate("7", right)
def eight(right=None): 
    if not right:
        return "8"
    else:return evaulate("8", right)
def nine(right=None): 
    if not right:
        return "9"
    else:return evaulate("9", right)

def plus(opd): 
    return f"+ {opd}"
def minus(opd): 
    return f"- {opd}"
def times(opd): 
    return f"* {opd}"
def divided_by(opd): 
    return f"/ {opd}"
```

## [18. Beginner Series #3 Sum of Numbers](https://www.codewars.com/kata/55f2b110f61eb01779000053)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![7 kyu](https://img.shields.io/badge/7%20kyu-white?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals, Algorithms|
|`Completed On`|2024-07-11T10:47:15.802+0000|


## Description 

Given two integers `a` and `b`, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return `a` or `b`.



**Note:** `a` and `b` are not ordered!



## Examples (a, b) --> output (explanation)



```
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
```

Your function should only return a number, not the explanation about how you get that number.

## Code 

```python
def get_sum(a,b):
    return sum(range(a, b+1)) if a<b else sum(range(b, a+1))
```

## [19. Mumbling](https://www.codewars.com/kata/5667e8f4e3f572a8f2000039)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![7 kyu](https://img.shields.io/badge/7%20kyu-white?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals, Strings, Puzzles|
|`Completed On`|2024-07-10T13:12:36.965+0000|


## Description 

This time no story, no theory. The examples below show you how to write function `accum`:



#### Examples:

```
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
```



The parameter of accum is a string which includes only letters from `a..z` and `A..Z`.

## Code 

```python
def accum(st):
    return "-".join([c.upper() + c * i for i, c in enumerate(st.lower())])
```

## [20. Duplicate Encoder](https://www.codewars.com/kata/54b42f9314d9229fd6000d9c)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![6 kyu](https://img.shields.io/badge/6%20kyu-FFFF00?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Strings, Arrays, Fundamentals|
|`Completed On`|2024-07-10T13:04:05.350+0000|


## Description 

The goal of this exercise is to convert a string to a new string where each character in the new string is `"("` if that character appears only once in the original string, or `")"` if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.



### Examples



```
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
```



### Notes



Assertion messages may be unclear about what they display in some languages. If you read `"...It Should encode XXX"`, the `"XXX"` is the expected result, not the input!

## Code 

```python
def duplicate_encode(word):
    return "".join([")" if word.lower().count(c) > 1 else "(" for c in word.lower()])
```

## [21. Convert a string to an array](https://www.codewars.com/kata/57e76bc428d6fbc2d500036d)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![8 kyu](https://img.shields.io/badge/8%20kyu-lightgrey?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Arrays, Strings, Fundamentals|
|`Completed On`|2024-07-10T12:59:51.387+0000|


## Description 

Write a function to split a string and convert it into an array of words.



### Examples (Input ==> Output):



```
"Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
```





## Code 

```python
def string_to_array(s):
    return s.split() if s else [s]
```

## [22. Unique In Order](https://www.codewars.com/kata/54e6533c92449cc251001667)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![6 kyu](https://img.shields.io/badge/6%20kyu-FFFF00?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Algorithms, Fundamentals|
|`Completed On`|2024-07-10T12:58:33.283+0000|


## Description 

Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.



For example:



```python
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
```





## Code 

```python
def unique_in_order(sequence):
    return [c for i, c in enumerate(sequence) if i==0 or c!=sequence[i-1]]
```

## [23. Odd or Even?](https://www.codewars.com/kata/5949481f86420f59480000e7)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![7 kyu](https://img.shields.io/badge/7%20kyu-white?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals, Arrays|
|`Completed On`|2024-07-10T12:38:18.044+0000|


## Description 

### Task:



Given a list of integers, determine whether the sum of its elements is odd or even.



Give your answer as a string matching `"odd"` or `"even"`.



If the input array is empty consider it as: `[0]` (array with a zero).



### Examples:



```
Input: [0]
Output: "even"

Input: [0, 1, 4]
Output: "odd"

Input: [0, -1, -5]
Output: "even"
```



Have fun!

## Code 

```python
def odd_or_even(arr):
    return "odd" if sum(arr)%2 else "even"
```

## [24. Highest Scoring Word](https://www.codewars.com/kata/57eb8fcdf670e99d9b000272)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![6 kyu](https://img.shields.io/badge/6%20kyu-FFFF00?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals, Strings, Arrays|
|`Completed On`|2024-07-10T12:37:08.449+0000|


## Description 

Given a string of words, you need to find the highest scoring word.



Each letter of a word scores points according to its position in the alphabet: `a = 1, b = 2, c = 3` etc.



For example, the score of `abad` is `8` (1 + 2 + 1 + 4).



You need to return the highest scoring word as a string.



If two words score the same, return the word that appears earliest in the original string.



All letters will be lowercase and all inputs will be valid.

## Code 

```python
def high(x):
    return max(x.split(), key = lambda w: sum([ord(c) - 96 for c in w]))
```

## [25. Playing with digits](https://www.codewars.com/kata/5552101f47fc5178b1000050)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![6 kyu](https://img.shields.io/badge/6%20kyu-FFFF00?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals, Mathematics|
|`Completed On`|2024-07-10T11:20:43.649+0000|


## Description 

Some numbers have funny properties. For example:



* 89 --> 8¹ + 9² = 89 * 1

* 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

* 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51



Given two positive integers `n` and `p`, we want to find a positive integer `k`, if it exists, such that the sum of the digits of `n` raised to consecutive powers starting from `p` is equal to `k * n`. 



In other words, writing the consecutive digits of `n` as `a, b, c, d ...`, is there an integer `k` such that :

```math
(a^p + b^{p + 1} + c^{p + 2} + d^{p + 3} + ...) = n * k
```



If it is the case we will return `k`, if not return `-1`.



**Note**: `n` and `p` will always be strictly positive integers.



## Examples:



```
n = 89; p = 1 ---> 1 since 8¹ + 9² = 89 = 89 * 1

n = 92; p = 1 ---> -1 since there is no k such that 9¹ + 2² equals 92 * k

n = 695; p = 2 ---> 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2

n = 46288; p = 3 ---> 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
```

## Code 

```python
def dig_pow(n, p):
    res = sum([int(j) ** (p + i) for i, j in enumerate(str(n))])
    return res//n if not res%n else -1
```

## [26. Sort the odd](https://www.codewars.com/kata/578aa45ee9fd15ff4600090d)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![6 kyu](https://img.shields.io/badge/6%20kyu-FFFF00?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals, Arrays, Sorting|
|`Completed On`|2024-07-10T10:55:05.955+0000|


## Description 

## Task



You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.



### Examples



```
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
```



  



## Code 

```python
def sort_array(s):
    new_s = sorted([i for i in s if i%2!=0])
    for i in range(len(s)):
        if s[i]%2==0:
            new_s.insert(i, s[i])
            
    return new_s
```

## [27. Take a Number And Sum  Its Digits Raised To The Consecutive Powers And ....¡Eureka!!](https://www.codewars.com/kata/5626b561280a42ecc50000d1)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![6 kyu](https://img.shields.io/badge/6%20kyu-FFFF00?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals, Mathematics|
|`Completed On`|2024-07-06T22:00:27.445+0000|


## Description 

The number ```$89$``` is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. 

What's the use of saying "Eureka"? Because this sum gives the same number: ```$89 = 8^1 + 9^2$```



The next number in having this property is ```$135$```:



See this property again: ```$135 = 1^1 + 3^2 + 5^3$```



## Task ##



We need a function to collect these numbers, that may receive two integers ```$a$```, ```$b$``` that defines the range ```$[a, b]$``` (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.



## Examples ##



Let's see some cases (input -> output):

```
1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
```



If there are no numbers of this kind in the range `$[a, b]$` the function should output an empty list.

```
90, 100 --> []
```

Enjoy it!!

## Code 

```python
def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    res = []
    n = a
    while n <= b:
        if n < 10:
            res.append(n)
        else:
            if n == sum([int(j) ** (i + 1) for i, j in enumerate(str(n))]):
                res.append(n)
        n += 1
    return res
```

## [28. Bouncing Balls](https://www.codewars.com/kata/5544c7a5cb454edb3c000047)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![6 kyu](https://img.shields.io/badge/6%20kyu-FFFF00?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Puzzles, Algorithms, Mathematics|
|`Completed On`|2024-07-06T21:32:24.251+0000|


## Description 

A child is playing with a ball on the nth floor of a tall building.

The height of this floor above ground level, *h*, is known. 



He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).

 

His mother looks out of a window 1.5 meters from the ground.



How many times will the mother see the ball pass in front of her window (including when it's falling _and_ bouncing)?



#### Three conditions must be met for a valid experiment:



*  Float parameter "h" in meters must be greater than 0

*  Float parameter "bounce" must be greater than 0 and less than 1

*  Float parameter "window" must be less than h.



**If all three conditions above are fulfilled, return a positive integer, otherwise return -1.**



#### Note:

The ball can only be seen if the height of the rebounding ball is strictly *greater* than the window parameter.



#### Examples:

```
- h = 3, bounce = 0.66, window = 1.5, result is 3

- h = 3, bounce = 1, window = 1.5, result is -1 

(Condition 2) not fulfilled).
```

## Code 

```python
def bouncing_ball(h, b, w):
    if h > 0 and 0 < b < 1 and w < h:
        count = 1
        h *= b
        while h > w:
            h *= b
            count += 2
        return count
    return -1
```

## [29. Mexican Wave](https://www.codewars.com/kata/58f5c63f1e26ecda7e000029)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![6 kyu](https://img.shields.io/badge/6%20kyu-FFFF00?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Arrays, Strings, Fundamentals|
|`Completed On`|2024-07-06T21:17:56.006+0000|


## Description 

# Introduction



> The wave (known as the Mexican wave in the English-speaking world outside North America) is an example of metachronal rhythm achieved in a packed stadium when successive groups of spectators briefly stand, yell, and raise their arms. Immediately upon stretching to full height, the spectator returns to the usual seated position.

> The result is a wave of standing spectators that travels through the crowd, even though individual spectators never move away from their seats. In many large arenas the crowd is seated in a contiguous circuit all the way around the sport field, and so the wave is able to travel continuously around the arena; in discontiguous seating arrangements, the wave can instead reflect back and forth through the crowd. When the gap in seating is narrow, the wave can sometimes pass through it. Usually only one wave crest will be present at any given time in an arena, although simultaneous, counter-rotating waves have been produced.



([Wikipedia](https://en.wikipedia.org/wiki/Wave_(audience)))



## Task



In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and you must return an array of strings where an **uppercase** letter is a person standing up.



## Rules

 1.  The input string will always consist of lowercase letters and spaces, but may be empty, in which case you must return an empty array.

 2.  If the character in the string is whitespace then pass over it as if it was an empty seat



## Examples



Good luck and enjoy!

## Code 

```python
def wave(s):
    return [j[:i] + j[i].upper() + j[i+1:] for i, j in enumerate([s] * len(s)) if j[i] != " "]
```

## [30. Build a pile of Cubes](https://www.codewars.com/kata/5592e3bd57b64d00f3000047)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![6 kyu](https://img.shields.io/badge/6%20kyu-FFFF00?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Mathematics, Algorithms|
|`Completed On`|2024-07-06T21:07:06.136+0000|


## Description 

Your task is to construct a building which will be a pile of n cubes.

The cube at the bottom will have a volume of `$ n^3 $`, the cube above 

will have  volume of `$ (n-1)^3 $` and so on until the top which will have a volume of `$ 1^3 $`.



You are given the total volume m of the building.

Being given m can you find the number n of cubes you will have to build?



The parameter of the function findNb `(find_nb, find-nb, findNb, ...)` will be an integer m

and you have to return the integer n such as `$ n^3 + (n-1)^3 + (n-2)^3 + ... + 1^3 = m $`

if such a n exists or -1 if there is no such n.



#### Examples:



```if-not:nasm
findNb(1071225) --> 45

findNb(91716553919377) --> -1
```



if:nasm

```
mov rdi, 1071225
call find_nb            ; rax <-- 45
    
mov rdi, 91716553919377
call find_nb            ; rax <-- -1
```

## Code 

```python
def find_nb(m):
    n = 1
    while m > 0:
        m -= n ** 3
        n += 1
    return n - 1 if m == 0 else -1
```

## [31. Write Number in Expanded Form](https://www.codewars.com/kata/5842df8ccbd22792a4000245)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![6 kyu](https://img.shields.io/badge/6%20kyu-FFFF00?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Strings, Mathematics, Algorithms, Fundamentals|
|`Completed On`|2024-07-06T18:32:49.492+0000|


## Description 

# Write Number in Expanded Form



You will be given a number and you will need to return it as a string in [Expanded Form](https://www.mathsisfun.com/definitions/expanded-notation.html). For example:



```
   12 --> "10 + 2"
   45 --> "40 + 5"
70304 --> "70000 + 300 + 4"
```



NOTE: All numbers will be whole numbers greater than 0.



If you liked this kata, check out [part 2](https://www.codewars.com/kata/write-number-in-expanded-form-part-2)!!

## Code 

```python
def expanded_form(num):
    s_num = str(num)
    return ' + '.join(j + "0" * (len(s_num) - i - 1) for i, j in enumerate(s_num) if j != "0")
```

## [32. Replace With Alphabet Position](https://www.codewars.com/kata/546f922b54af40e1e90001da)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![6 kyu](https://img.shields.io/badge/6%20kyu-FFFF00?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Strings, Fundamentals|
|`Completed On`|2024-07-05T21:46:52.649+0000|


## Description 

Welcome.



In this kata you are required to, given a string, replace every letter with its position in the alphabet.



If anything in the text isn't a letter, ignore it and don't return it.



`"a" = 1`, `"b" = 2`, etc.



## Example



Input = "The sunset sets at twelve o' clock."

Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"



## Code 

```python
import re
def alphabet_position(text):
    return " ".join([str(ord(i) - 96) for i in re.sub(r"[^a-z]", "", text.lower())])
```

## [33. Shortest Word](https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![7 kyu](https://img.shields.io/badge/7%20kyu-white?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals|
|`Completed On`|2024-07-04T12:39:34.963+0000|


## Description 

Simple, given a string of words, return the length of the shortest word(s).



String will never be empty and you do not need to account for different data types.

## Code 

```python
def find_short(s):
    return len(min(s.split(" "), key=lambda x:len(x)))
```

## [34. Take a Ten Minutes Walk](https://www.codewars.com/kata/54da539698b8a2ad76000228)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![6 kyu](https://img.shields.io/badge/6%20kyu-FFFF00?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Arrays, Fundamentals|
|`Completed On`|2024-07-04T12:26:58.361+0000|


## Description 

You live in the city of Cartesia where all roads are laid out in a perfect grid.  You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk.  The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']).  You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return **true** if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point.  Return **false** otherwise.



> **Note**: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only).  It will never give you an empty array (that's not a walk, that's standing still!).

## Code 

```python
def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    return (walk.count("n") == walk.count("s")) and (walk.count("w") == walk.count("e"))
```

## [35. Count the smiley faces!](https://www.codewars.com/kata/583203e6eb35d7980400002a)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![6 kyu](https://img.shields.io/badge/6%20kyu-FFFF00?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Regular Expressions, Fundamentals|
|`Completed On`|2024-07-04T11:58:28.507+0000|


## Description 

Given an array (arr) as an argument complete the function `countSmileys` that should return the total number of smiling faces.  



Rules for a smiling face:

- Each smiley face must contain a valid pair of eyes. Eyes can be marked as `:` or `;`

- A smiley face can have a nose but it does not have to. Valid characters for a nose are `-` or `~`

- Every smiling face must have a smiling mouth that should be marked with either `)` or `D`



No additional characters are allowed except for those mentioned.  



**Valid smiley face examples:** `:) :D ;-D :~)`  

**Invalid smiley faces:**  `;( :> :} :]`



## Example



```
countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
```



## Note



In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same.

## Code 

```python
import re

def count_smileys(arr):
    return len(re.findall(r"[:;][-~]?[\)D]", " ".join(arr)))
```

## [36. You only need one - Beginner](https://www.codewars.com/kata/57cc975ed542d3148f00015b)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![8 kyu](https://img.shields.io/badge/8%20kyu-lightgrey?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals, Strings, Arrays|
|`Completed On`|2024-07-04T10:59:52.160+0000|


## Description 

You will be given an array `a` and a value `x`. All you need to do is check whether the provided array contains the value.



`a` can contain numbers or strings. `x` can be either.

Return `true` if the array contains the value, `false` if not.

## Code 

```python
def check(seq, elem):
    return elem in seq
```

## [37. Isograms](https://www.codewars.com/kata/54ba84be607a92aa900000f1)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![7 kyu](https://img.shields.io/badge/7%20kyu-white?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Strings, Fundamentals|
|`Completed On`|2024-07-04T10:58:42.940+0000|


## Description 

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.



**Example: (Input --> Output)**

"Dermatoglyphics" --> true

"aba" --> false

"moOse" --> false (ignore letter case)



## Code 

```python
def is_isogram(string):
    return len(string) == len(set(string.lower()))
```

## [38. Build Tower](https://www.codewars.com/kata/576757b1df89ecf5bd00073b)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![6 kyu](https://img.shields.io/badge/6%20kyu-FFFF00?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Strings, ASCII Art, Fundamentals|
|`Completed On`|2024-07-04T03:05:19.560+0000|


## Description 

Build Tower

---



Build a pyramid-shaped tower, as an array/list of strings, given a positive integer `number of floors`. A tower block is represented with `"*"` character.



For example, a tower with `3` floors looks like this:



```
[
  "  *  ",
  " *** ", 
  "*****"
]
```



And a tower with `6` floors looks like this:



```
[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
```

## Code 

```python
def tower_builder(n):
    return [("*" * i).center(2*n - 1, ' ') for i in range(1, n*2, 2)]
```

## [39. Persistent Bugger.](https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![6 kyu](https://img.shields.io/badge/6%20kyu-FFFF00?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals, Mathematics|
|`Completed On`|2024-07-03T12:52:56.170+0000|


## Description 

Write a function, `persistence`, that takes in a positive parameter `num` and returns its multiplicative persistence, which is the number of times you must multiply the digits in `num` until you reach a single digit.



For example **(Input --> Output)**:



```
39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2, there are 4 multiplications)
4 --> 0 (because 4 is already a one-digit number, there is no multiplication)
```

## Code 

```python
def persistence(n):
    if n < 10:
        return 0
    else:
        count = 0
        while n >= 10:
            count += 1
            prod = 1
            for i in str(n):
                prod *= int(i)
            n = prod
    return count
            
```

## [40. Tribonacci Sequence](https://www.codewars.com/kata/556deca17c58da83c00002db)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![6 kyu](https://img.shields.io/badge/6%20kyu-FFFF00?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Number Theory, Arrays, Lists, Fundamentals|
|`Completed On`|2024-07-03T11:57:06.650+0000|


## Description 

Well met with Fibonacci bigger brother, AKA Tribonacci.



As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(



So, if we are to start our Tribonacci sequence with `[1, 1, 1]` as a starting input (AKA *signature*), we have this sequence:



```
[1, 1 ,1, 3, 5, 9, 17, 31, ...]
```



But what if we started with `[0, 0, 1]` as a signature? As starting with `[0, 1]` instead of `[1, 1]` basically *shifts* the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:



```
[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
```



Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a **signature** array/list, returns **the first n elements - signature included** of the so seeded sequence.



Signature will always contain 3 numbers; n will always be a non-negative number; if `n == 0`, then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)



If you enjoyed this kata more advanced and generalized version of it can be found in the <a href="http://www.codewars.com/kata/fibonacci-tribonacci-and-friends"  target="_blank" title="Xbonacci sequence">Xbonacci kata</a>



*[Personal thanks to Professor <a href="https://www.coursera.org/instructor/jimfowler" target="_blank" title="Jim Fowler">Jim Fowler</a> on Coursera for his awesome classes that I really recommend to any math enthusiast and for showing me this mathematical curiosity too with his usual contagious passion :)]*

## Code 

```python
def tribonacci(signature, n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    return signature[:n]
```

## [41. String ends with?](https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![7 kyu](https://img.shields.io/badge/7%20kyu-white?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Strings, Fundamentals|
|`Completed On`|2024-07-03T11:00:57.980+0000|


## Description 

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).



Examples:



```
Inputs: "abc", "bc"
Output: true

Inputs: "abc", "d"
Output: false
```

## Code 

```python
def solution(text, ending):
    return text.endswith(ending)
```

## [42. Equal Sides Of An Array](https://www.codewars.com/kata/5679aa472b8f57fb8c000047)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![6 kyu](https://img.shields.io/badge/6%20kyu-FFFF00?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Algorithms, Arrays, Fundamentals|
|`Completed On`|2024-07-03T10:59:43.419+0000|


## Description 

You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N.



```if-not:rust
If there is no index that would make this happen, return `-1`.
```



### For example:



Let's say you are given the array `{1,2,3,4,3,2,1}`:  

Your function will return the index `3`, because the sum of left side of the index (`{1,2,3}`) and the sum of the right side of the index (`{3,2,1}`) both equal `6`.



Let's look at another one.  

You are given the array `{1,100,50,-51,1,1}`:  

Your function will return the index `1`, because the sum of left side of the index (`{1}`) and the sum of the right side of the index (`{50,-51,1,1}`) both equal `1`.



Last one:  

You are given the array `{20,10,-80,10,10,15,35}`  

At index 0 the left side is `{}`  

The right side is `{10,-80,10,10,15,35}`  

They both are equal to `0` when added. (Empty arrays are equal to 0 in this problem)  

Index 0 is the place where the left side and right side are equal.  



Note: Please remember that in most languages the index of an array starts at 0.



### Input



An integer array of length `0 < arr < 1000`. The numbers in the array can be any integer positive or negative.



### Output



The lowest index `N` where the side to the left of `N` is equal to the side to the right of `N`. If you do not find an index that fits these rules, then you will return `-1`.



### Note



If you are given an array with multiple answers, return the lowest correct index.  





## Code 

```python
def find_even_index(arr):
    res = []
    for i in range(0, len(arr)):
        if sum(arr[0:i]) == sum(arr[i +1:]):
            res.append(i)
    if res:return res[0]
    return -1
```

## [43. Number of People in the Bus](https://www.codewars.com/kata/5648b12ce68d9daa6b000099)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![7 kyu](https://img.shields.io/badge/7%20kyu-white?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals|
|`Completed On`|2024-06-28T18:18:29.317+0000|


## Description 

There is a bus moving in the city which takes and drops some people at each bus stop.



You are provided with a list (or array) of integer pairs. Elements of each pair represent the number of people that get on the bus (the first item) and the number of people that get off the bus (the second item) at a bus stop.



Your task is to return the number of people who are still on the bus after the last bus stop (after the last array). Even though it is the last bus stop, the bus might not be empty and some people might still be inside the bus, they are probably sleeping there :D 



Take a look on the test cases.



Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the returned integer can't be negative.



The second value in the first pair in the array is 0, since the bus is empty in the first bus stop.

## Code 

```python
def number(bus_stops):
    return sum([i - j for i, j in bus_stops])
```

## [44. Exes and Ohs](https://www.codewars.com/kata/55908aad6620c066bc00002a)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![7 kyu](https://img.shields.io/badge/7%20kyu-white?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals|
|`Completed On`|2024-06-28T18:14:58.248+0000|


## Description 

Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.



Examples input/output:

```
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
```

## Code 

```python
def xo(s):
    return s.lower().count('x') == s.lower().count('o')
```

## [45. DNA to RNA Conversion](https://www.codewars.com/kata/5556282156230d0e5e000089)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![8 kyu](https://img.shields.io/badge/8%20kyu-lightgrey?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals, Strings|
|`Completed On`|2024-06-28T18:09:04.642+0000|


## Description 

Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T'). 



Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').



Create a function which translates a given DNA string into RNA.



For example:



```
"GCAT"  =>  "GCAU"
```



The input string can be of arbitrary length - in particular, it may be empty.  All input is guaranteed to be valid, i.e. each input string will only ever consist of `'G'`, `'C'`, `'A'` and/or `'T'`.

## Code 

```python
def dna_to_rna(dna):
    return dna.replace("T", "U")
```

## [46. You're a square!](https://www.codewars.com/kata/54c27a33fb7da0db0100040e)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![7 kyu](https://img.shields.io/badge/7%20kyu-white?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals, Mathematics|
|`Completed On`|2024-06-28T18:06:06.166+0000|


## Description 

### A square of squares



You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!



However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a _perfect square_.



### Task



Given an integral number, determine if it's a [square number](https://en.wikipedia.org/wiki/Square_number):



> In mathematics, a __square number__ or __perfect square__ is an integer that is the square of an integer; in other words, it is the product of some integer with itself.



The tests will _always_ use some integral number, so don't worry about that in dynamic typed languages.



### Examples



```
-1  =>  false
 0  =>  true
 3  =>  false
 4  =>  true
25  =>  true
26  =>  false
```



  



## Code 

```python
def is_square(n):    
    return False if n < 0 else (n**0.5).is_integer()
```

## [47. Break camelCase](https://www.codewars.com/kata/5208f99aee097e6552000148)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![6 kyu](https://img.shields.io/badge/6%20kyu-FFFF00?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Strings, Fundamentals|
|`Completed On`|2024-06-27T13:32:52.551+0000|


## Description 

Complete the solution so that the function will break up camel casing, using a space between words.



### Example 



```
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
```

## Code 

```python
def solution(s):
    res = ""
    for i in s:
        if 65 <= ord(i) <= 90:
            res += " " + i
        else:
            res += i
    return res
```

## [48. Sum of odd numbers](https://www.codewars.com/kata/55fd2d567d94ac3bc9000064)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![7 kyu](https://img.shields.io/badge/7%20kyu-white?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Arrays, Lists, Mathematics, Fundamentals|
|`Completed On`|2024-06-27T13:02:30.586+0000|


## Description 

Given the triangle of consecutive odd numbers:



```
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
```



Calculate the sum of the numbers in the n<sup>th</sup> row of this triangle (starting at index 1) e.g.: (**Input --> Output**)



```
1 -->  1
2 --> 3 + 5 = 8
```

## Code 

```python
def row_sum_odd_numbers(n):
    return n ** 3
```

## [49. Beginner Series #1 School Paperwork](https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![8 kyu](https://img.shields.io/badge/8%20kyu-lightgrey?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals|
|`Completed On`|2024-06-27T12:47:18.665+0000|


## Description 

Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.



Your task is to calculate how many blank pages do you need. If `n < 0` or `m < 0` return `0`.



### Example:



```
n= 5, m=5: 25
n=-5, m=5:  0
```



Waiting for translations and Feedback! Thanks!

## Code 

```python
def paperwork(n, m):
    return 0 if (n < 0 or m < 0) else n * m
```

## [50. Highest and Lowest](https://www.codewars.com/kata/554b4ac871d6813a03000035)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![7 kyu](https://img.shields.io/badge/7%20kyu-white?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals, Strings|
|`Completed On`|2024-06-27T12:32:46.199+0000|


## Description 

In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.



### Examples



``` text
Input: "1 2 3 4 5"   =>  Output: "5 1"
Input: "1 2 -3 4 5"  =>  Output: "5 -3"
Input: "1 9 3 4 -5"  =>  Output: "9 -5"
```



```python
high_and_low("1 2 3 4 5") # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
```



### Notes



- All numbers are valid ```Int32```, no *need* to validate them.

- There will always be at least one number in the input string.

- Output string must be two numbers separated by a single space, and highest number is first.

## Code 

```python
def high_and_low(n):
    l = sorted(n.split(" "), key = int)
    return f"{l[-1]} {l[0]}"
```

## [51. Is he gonna survive?](https://www.codewars.com/kata/59ca8246d751df55cc00014c)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![8 kyu](https://img.shields.io/badge/8%20kyu-lightgrey?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals|
|`Completed On`|2024-06-27T10:54:00.485+0000|


## Description 

A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?



Return true if yes, false otherwise :)

## Code 

```python
def hero(bullets, dragons):
    return dragons * 2 <= bullets
```

## [52. Ones and Zeros](https://www.codewars.com/kata/578553c3a1b8d5c40300037c)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![7 kyu](https://img.shields.io/badge/7%20kyu-white?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals, Arrays|
|`Completed On`|2024-06-27T10:51:35.094+0000|


## Description 

Given an array of ones and zeroes, convert the equivalent binary value to an integer.



Eg: `[0, 0, 0, 1]` is treated as `0001` which is the binary representation of `1`.



Examples:

```
Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11
```



However, the arrays can have varying lengths, not just limited to `4`.

## Code 

```python
def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)
```

## [53. Convert number to reversed array of digits](https://www.codewars.com/kata/5583090cbe83f4fd8c000051)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![8 kyu](https://img.shields.io/badge/8%20kyu-lightgrey?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Arrays, Fundamentals|
|`Completed On`|2024-06-26T13:18:59.589+0000|


## Description 

Given a random non-negative number, you have to return the digits of this number within an array in reverse order.



### Example (Input => Output):



```
35231 => [1,3,2,5,3]
0     => [0]
```

## Code 

```python
def digitize(n):
    return [int(i) for i in str(n)[::-1]]
```

## [54. Convert boolean values to strings 'Yes' or 'No'.](https://www.codewars.com/kata/53369039d7ab3ac506000467)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![8 kyu](https://img.shields.io/badge/8%20kyu-lightgrey?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals|
|`Completed On`|2024-06-26T13:13:37.664+0000|


## Description 

Complete the method that takes a boolean value and return a `"Yes"` string for `true`, or a `"No"` string for `false`.

## Code 

```python
def bool_to_word(b):
    return 'Yes' if b else 'No' 
```

## [55. Get the Middle Character](https://www.codewars.com/kata/56747fd5cb988479af000028)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![7 kyu](https://img.shields.io/badge/7%20kyu-white?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals, Strings|
|`Completed On`|2024-06-26T13:11:36.564+0000|


## Description 

You are going to be given a **non-empty** string. Your job is to return the middle character(s) of the string.

* If the string's length is odd, return the middle character.

* If the string's length is even, return the middle 2 characters.



### Examples:





## Code 

```python
def get_middle(s):
    return s[len(s)//2 - 1:len(s)//2 + 1] if len(s)%2==0 else s[len(s)//2]
```

## [56. Two to One](https://www.codewars.com/kata/5656b6906de340bd1b0000ac)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![7 kyu](https://img.shields.io/badge/7%20kyu-white?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals|
|`Completed On`|2024-06-26T12:54:29.134+0000|


## Description 

Take 2 strings `s1` and `s2` including only letters from `a` to `z`.

Return a new **sorted** string (alphabetical ascending), the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.



#### Examples:

```
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
```

## Code 

```python
def longest(a1, a2):
    return ''.join(sorted(set(a1 + a2)))
```

## [57. Printer Errors](https://www.codewars.com/kata/56541980fa08ab47a0000040)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![7 kyu](https://img.shields.io/badge/7%20kyu-white?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals|
|`Completed On`|2024-06-26T12:48:27.394+0000|


## Description 

In a factory a printer prints labels for boxes. For one kind of boxes

the printer has to use colors which, for the sake of simplicity,

are named with letters from `a to m`. 



The colors used by the printer are

recorded in a control string. For example a "good" control string would be

`aaabbbbhaijjjm` meaning that the printer used three times color a, four times

color b, one time color h then one time color a...



Sometimes there are problems: lack of colors, technical malfunction and a "bad" 

control string is produced e.g. `aaaxbbbbyyhwawiwjjjwwm` with letters not from `a to m`.



You have to write a function `printer_error` which given a string will return

the error rate of the printer as a **string** representing a rational whose numerator 

is the number of errors and the denominator the length of the control string.

Don't reduce this fraction to a simpler expression.



The string has a length greater or equal to one and contains only letters 

from `a`to `z`.



#### Examples:



```
s="aaabbbbhaijjjm"
printer_error(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
printer_error(s) => "8/22"

```

## Code 

```python
def printer_error(s):
    return f"{sum(color > 'm' for color in s)}/{len(s)}"
```

## [58. Binary Addition](https://www.codewars.com/kata/551f37452ff852b7bd000139)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![7 kyu](https://img.shields.io/badge/7%20kyu-white?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Binary, Fundamentals|
|`Completed On`|2024-06-26T12:27:18.451+0000|


## Description 

Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.



The binary number returned should be a string.



**Examples:(Input1, Input2 --> Output (explanation)))**

```
1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
```

## Code 

```python
def add_binary(a,b):
    return f"{a+b:b}"
```

## [59. Categorize New Member](https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![7 kyu](https://img.shields.io/badge/7%20kyu-white?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals|
|`Completed On`|2024-06-26T11:58:48.208+0000|


## Description 

The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.



To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.



### Input



Input will consist of a list of pairs. Each pair contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.



### Output

Output will consist of a list of string values (in Haskell and C: `Open` or `Senior`) stating whether the respective member is to be placed in the senior or open category.



### Example



```
input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]
```

## Code 

```python
def open_or_senior(data):
    result = []
    for age, hand in data:
        if age >= 55 and hand > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result
```

## [60. Keep Hydrated!](https://www.codewars.com/kata/582cb0224e56e068d800003c)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![8 kyu](https://img.shields.io/badge/8%20kyu-lightgrey?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Algorithms, Mathematics, Fundamentals|
|`Completed On`|2024-06-26T11:47:48.497+0000|


## Description 

Nathan loves cycling. 



Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.



You get given the time in hours and you need to return the number of litres Nathan will drink, rounded _down_.



For example:

time = 3 ----> litres = 1



time = 6.7---> litres = 3



time = 11.8--> litres = 5



## Code 

```python
def litres(time):
    return (time * 5)//10
```

## [61. Beginner - Lost Without a Map](https://www.codewars.com/kata/57f781872e3d8ca2a000007e)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![8 kyu](https://img.shields.io/badge/8%20kyu-lightgrey?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals, Arrays|
|`Completed On`|2024-06-26T11:40:46.556+0000|


## Description 

Given an array of integers, return a new array with each value doubled.



For example:



`[1, 2, 3] --> [2, 4, 6]`





## Code 

```python
def maps(a):
    return [x * 2 for x in a]
```

## [62. Complementary DNA](https://www.codewars.com/kata/554e4a2f232cdd87d9000038)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![7 kyu](https://img.shields.io/badge/7%20kyu-white?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Strings, Fundamentals|
|`Completed On`|2024-06-26T11:37:35.890+0000|


## Description 

Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.



If you want to know more: http://en.wikipedia.org/wiki/DNA



In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 

Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).



More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)



Example: (**input --> output**)

"ATTGC" --> "TAACG"

"GTAT" --> "CATA"



## Code 

```python
def DNA_strand(dna):
    trans = str.maketrans('TACG','ATGC')
    return dna.translate(trans)
```

## [63. Sum Arrays](https://www.codewars.com/kata/53dc54212259ed3d4f00071c)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![8 kyu](https://img.shields.io/badge/8%20kyu-lightgrey?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Arrays, Fundamentals|
|`Completed On`|2024-06-26T11:14:24.663+0000|


## Description 

Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.



### Examples



Input: `[1, 5.2, 4, 0, -1]`  

Output: `9.2`



Input: `[]`  

Output: `0`



Input: `[-2.398]`  

Output: `-2.398`



### Assumptions



- You can assume that you are only given numbers.

- You cannot assume the size of the array.

- You can assume that you do get an array and if the array is empty, return 0.



### What We're Testing



We're testing basic loops and math operations. This is for beginners who are just learning loops and math operations.  

Advanced users may find this extremely easy and can easily write this in one line.

## Code 

```python
def sum_array(a):
    return sum(a)
```

## [64. Reverse words](https://www.codewars.com/kata/5259b20d6021e9e14c0010d4)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![7 kyu](https://img.shields.io/badge/7%20kyu-white?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Strings, Fundamentals|
|`Completed On`|2024-06-26T11:07:09.685+0000|


## Description 

Complete the function that accepts a string parameter, and reverses each word in the string. **All** spaces in the string should be retained.



## Examples

```
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
```

## Code 

```python
def reverse_words(text):
    return ' '.join([s[::-1] for s in text.split(' ')]) 
```

## [65. Area or Perimeter](https://www.codewars.com/kata/5ab6538b379d20ad880000ab)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![8 kyu](https://img.shields.io/badge/8%20kyu-lightgrey?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals, Mathematics, Geometry|
|`Completed On`|2024-06-26T10:37:46.133+0000|


## Description 

You are given the `length` and `width` of a 4-sided polygon. The polygon can either be a rectangle or a square.  

If it is a square, return its area. If it is a rectangle, return its perimeter.



**Example(Input1, Input2 --> Output):**

```
6, 10 --> 32
3, 3 --> 9
```



**Note:** for the purposes of this kata you will assume that it is a square if its `length` and `width` are equal, otherwise it is a rectangle.

## Code 

```python
def area_or_perimeter(l , w):
    if l == w:
        return l * w
    return 2 * (l + w)
```

## [66. Fake Binary](https://www.codewars.com/kata/57eae65a4321032ce000002d)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![8 kyu](https://img.shields.io/badge/8%20kyu-lightgrey?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals, Strings, Arrays|
|`Completed On`|2024-06-26T10:34:19.811+0000|


## Description 

Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.



**Note: input will never be an empty string**

## Code 

```python
def fake_bin(x):
    z = ""
    for i in x:
        if int(i) < 5:
            z += '0'
        else:
            z+= '1'
    return z
```

## [67. Remove String Spaces](https://www.codewars.com/kata/57eae20f5500ad98e50002c5)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![8 kyu](https://img.shields.io/badge/8%20kyu-lightgrey?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals, Strings|
|`Completed On`|2024-06-26T10:31:48.984+0000|


## Description 

Write a function that removes the spaces from the string, then return the resultant string.



Examples (**Input -> Output**):

```
"8 j 8   mBliB8g  imjB8B8  jl  B" -> "8j8mBliB8gimjB8B8jlB"
"8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd" -> "88Bifk8hB8BB8BBBB888chl8BhBfd"
"8aaaaa dddd r     " -> "8aaaaaddddr"
```





## Code 

```python
def no_space(x):
    z = ""
    for i in x:
        if i != ' ':
            z+=i
    return z
```

## [68. Sentence Smash](https://www.codewars.com/kata/53dc23c68a0c93699800041d)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![8 kyu](https://img.shields.io/badge/8%20kyu-lightgrey?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Strings, Arrays, Fundamentals|
|`Completed On`|2024-06-26T10:24:06.586+0000|


## Description 

# Sentence Smash



Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. **Be careful, there shouldn't be a space at the beginning or the end of the sentence!**



## Example



```
['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'
```



## Assumptions



* You can assume that you are only given words.

* You cannot assume the size of the array.

* You can assume that you do get an array.



## What We're Testing



We're testing basic loops and string manipulation. This is for beginners who are just learning loops and string manipulation.



## Disclaimer



This is for beginners so we want to test basic loops and string manipulation. Advanced users should easily be able to do this in one line.

## Code 

```python
def smash(words):
    return " ".join(words)
    
```

## [69. Return Negative](https://www.codewars.com/kata/55685cd7ad70877c23000102)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![8 kyu](https://img.shields.io/badge/8%20kyu-lightgrey?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals|
|`Completed On`|2024-06-09T08:13:54.074+0000|


## Description 

In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?



### Examples



``` text
Input:  1  =>  Output: -1
Input: -5  =>  Output: -5
Input:  0  =>  Output:  0
```



``` python
make_negative(1);  # return -1
make_negative(-5); # return -5
make_negative(0);  # return 0
```



### Notes



- The number can be negative already, in which case no change is required.

- Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.

## Code 

```python
def make_negative( number ):
    return number * -1 if number >= 0 else number
```

## [70. Counting sheep...](https://www.codewars.com/kata/54edbc7200b811e956000556)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![8 kyu](https://img.shields.io/badge/8%20kyu-lightgrey?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Arrays, Fundamentals|
|`Completed On`|2024-06-09T08:10:08.799+0000|


## Description 

Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).



For example,



```python
[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
```



The correct answer would be `17`.



Hint: Don't forget to check for bad values like `null`/`undefined`





## Code 

```python
def count_sheeps(sheep):
    return sum([1 for i in sheep if i])
```

## [71. Convert a String to a Number!](https://www.codewars.com/kata/544675c6f971f7399a000e79)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![8 kyu](https://img.shields.io/badge/8%20kyu-lightgrey?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Parsing, Strings, Fundamentals|
|`Completed On`|2024-06-09T08:05:11.766+0000|


## Description 

Note: This kata is inspired by [Convert a Number to a String!](http://www.codewars.com/kata/convert-a-number-to-a-string/). Try that one too.



## Description



We need a function that can transform a string into a number. What ways of achieving this do you know?



Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.



## Examples

```
"1234" --> 1234
"605"  --> 605
"1405" --> 1405
"-7" --> -7
```

## Code 

```python
def string_to_number(s):
    return int(s)
```

## [72. If you can't sleep, just count sheep!!](https://www.codewars.com/kata/5b077ebdaf15be5c7f000077)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![8 kyu](https://img.shields.io/badge/8%20kyu-lightgrey?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals, Strings|
|`Completed On`|2024-06-09T08:03:25.286+0000|


## Description 

If you can't sleep, just count sheeps!!



## Task:

Given a non-negative integer, `3` for example, return a string with a murmur: `"1 sheep...2 sheep...3 sheep..."`.  Input will always be valid, i.e. no negative integers.

## Code 

```python
def count_sheep(n):
    print(n)
    if n < 1:
        return ""
    else:
        return ' sheep...'.join([str(i + 1) for i in range(0, n)]) + ' sheep...'
```

## [73. Find Maximum and Minimum Values of a List](https://www.codewars.com/kata/577a98a6ae28071780000989)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![8 kyu](https://img.shields.io/badge/8%20kyu-lightgrey?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals|
|`Completed On`|2024-06-09T07:55:39.434+0000|


## Description 

Your task is to make two functions ( `max` and `min`, or `maximum` and `minimum`, etc., depending on the language ) that receive a list of integers as input, and return the largest and lowest number in that list, respectively. Each function returns one number.



### Examples (Input -> Output)



```
* [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
* [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
* [42, 54, 65, 87, 0]             -> min = 0, max = 87
* [5]                             -> min = 5, max = 5
```



### Notes



- You may consider that there will not be any empty arrays/vectors.

## Code 

```python
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)
```

## [74. Sum without highest and lowest number](https://www.codewars.com/kata/576b93db1129fcf2200001e6)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![8 kyu](https://img.shields.io/badge/8%20kyu-lightgrey?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals|
|`Completed On`|2024-06-09T07:54:56.573+0000|


## Description 

## Task



Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).



The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.



Mind the input validation.



## Example



    { 6, 2, 1, 8, 10 } => 16

    { 1, 1, 11, 2, 3 } => 6



## Input validation



If an empty value ( `null`, `None`, `Nothing`, `nil` etc. ) is given instead of an array, or the given array is an empty list or a list with only `1` element, return `0`.

## Code 

```python
def sum_array(arr):
    if (not arr) or len(arr) <= 2:
        return 0
    else:
        arry = [i for i in arr if type(i) == int]
        return sum(sorted(arry)[1:-1])
```

## [75. Opposites Attract](https://www.codewars.com/kata/555086d53eac039a2a000083)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![8 kyu](https://img.shields.io/badge/8%20kyu-lightgrey?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Fundamentals|
|`Completed On`|2024-06-09T07:17:50.347+0000|


## Description 

Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love. 



Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

## Code 

```python
def lovefunc( flower1, flower2 ):
    if (flower1 + flower2) % 2 != 0:
        return True
    else:
        return False
```

## [76. Are You Playing Banjo?](https://www.codewars.com/kata/53af2b8861023f1d88000832)

|**Attribute**|**Value**|
|---|---|
|`Difficulty`|![8 kyu](https://img.shields.io/badge/8%20kyu-lightgrey?style=for-the-banner&logo=codewars&logoColor=orange&labelColor=grey)|
|`Language`|Python|
|`Tags`|Strings, Fundamentals|
|`Completed On`|2024-06-09T07:15:12.730+0000|


## Description 

Create a function which answers the question "Are you playing banjo?".  

If your name starts with the letter "R" or lower case "r", you are playing banjo!



The function takes a name as its only argument, and returns one of the following strings:

```
name + " plays banjo" 
name + " does not play banjo"
```

Names given are always valid strings.

## Code 

```python
def are_you_playing_banjo(name):
    if name[0].lower() == 'r': 
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
```

