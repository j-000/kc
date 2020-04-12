# Kaprekar's Constants

I recently watched a video on YouTube by Numberphile entitled [6174 - Numberphile](https://www.youtube.com/watch?v=d8TRcZklX_Q).
It discusses [Kaprekar's constant 6174](https://en.wikipedia.org/wiki/6174_(number)). This constant
is found with the following algorithm.

```text
1) Take a number: 1234
2) Sort it descending order: 4321
3) Subtract the first number to the sorted one: 4321 - 1234 = 3087
Repeat step 1) with result 3087

    4321 - 1234 = 3087
    8730 - 378 = 8352
    8532 - 2358 = 6174
    7641 - 1467 = 6174
    Ended with 4 loops.

This example only "loops" 4 times until it reaches 6174.
```

I found it extremely interesting and decided to write this python script to crunch some more
Kaprekar constants.

## My approach 
I am using a very slow 64-bit Acer Laptop with an Intel® Core™ i5-8250U and 8 CPU @ 1.60GHz. Sadly, 
I only managed to crunch up to 6 digits and then had to turn to a [z1d.large (~$0.186$ per Hour)](https://aws.amazon.com/ec2/instance-types/z1d/) memory optimised EC2 instance.
It did crunch 7 digits and only took 5 minutes. 

## Results (so far)
Given than the algorithm is a recursive one, I consider a "loop" to be each time the function is called
with a given number. The numbers on the right represent the total numbers in the range that loop the amount of times on the left side.

Given that in the range 111111 to 10000000 there are 9 numbers with only 1 digit (1111111, 2222222, etc), the
result shows these numbers loop 0 times are they are not valid (1111111 - 1111111 = 0). 

The rest can 
be read as "there are 8 numbers that loop 8 times until they hit the constant".
```text
7 digits - The most common digit is 8439552 at 8888768/8888889 or 100.0%.
Loop distributions is:
{
    "0": 9,
    "1": 112,
    "8": 8,
    "9": 757694,
    "10": 820280,
    "11": 826159,
    "12": 856594,
    "13": 733850,
    "14": 1548694,
    "15": 1688786,
    "16": 645429,
    "17": 581241,
    "18": 180962,
    "19": 204487,
    "20": 42876,
    "21": 1708
}
```

More results can be found on [info.txt](https://github.com/j-000/kc/blob/master/info.txt).

## Dependencies
The only depency is the tqdm library to provide a visual clue (progress bar) of the iteration.
- [tqdm](https://github.com/tqdm/tqdm) - `pip install tqdm` to install.

## Usage
```text
git clone https://github.com/tqdm/tqdm.git
python kc.py 111 1000

100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 889/889 [00:00<00:00, 112838.14it/s]
Loop distribution:
{
    "0": 9,
    "1": 49,
    "2": 137,
    "3": 130,
    "4": 244,
    "5": 196,
    "6": 124
}
The most common digit is 495 at 832/889 or 93.59%.
```

The ranges must be 111...X to 100...X. 

11 to 100

111 to 1000

1111 to 10000
etc..


## Contribute
Pull requests welcome. 

## Why?
Bored of this quarantine and as Professor Roger Bowley put it in the video 
> _Not everything has to be useful to be appealing and fun._

## Next steps?
Let's try crack the Kaprekar's constant for the range 11111111 to 100000000. 
