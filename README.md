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
I only managed to crunch up to 6 digits and then had to turn to a [z1d.large](https://aws.amazon.com/ec2/instance-types/z1d/) memory optimised EC2 instance.
It did crunch 7 digits and only took 5 minutes.

## Results (so far)
The important bit is the "most common digit" between each iteration. For 4 digits, the range (1111, 10000), it is the 6174 constant. 
Also note this constant has the interesting property that if performed the algorithm it loops
back to itself: 7641 - 1467 = 6174, so it only loops once. In fact 6174 appears on 8816 out of 8889 (99.18%) of the 
iterations for the range of 4 digits (1111, 10000).

Similarly, for the range of 6 digits, the number 851742 appears on 831491 out of 888889 (93.54%)
of the iterations for the range. Sadly, it does not converge to one number like 6174 does when the algoritm 
is applied to it - but it is still cool!

```text
#1) 875421 - 124578 = 750843
#2) 875430 - 34578 = 840852
#3) 885420 - 24588 = 860832
#4) 886320 - 23688 = 862632
#5) 866322 - 223668 = 642654
#6) 665442 - 244566 = 420876
#7) 876420 - 24678 = 851742 <-- back to #1) so this is the end. 
```

More results can be found on [info.txt](https://github.com/j-000/kc/blob/master/info.txt).

## Dependencies
- [tqdm](https://github.com/tqdm/tqdm) - `pip install tqdm` to install.
- [prettytable](https://github.com/jazzband/prettytable) - `pip install prettytable` to install.

## Usage
```text
git clone https://github.com/j-000/kc.git
python kc.py 111 1000

Starting with range (111, 1000) of 889 iterations.
100%|██████████| 889/889 [00:00<00:00, 81799.23it/s]
+------------+-----------+-------+
| Loop count | Frequency |   %   |
+------------+-----------+-------+
|     0      |     9     |  1.01 |
|     1      |     49    |  5.51 |
|     2      |    137    | 15.41 |
|     3      |    130    | 14.62 |
|     4      |    244    | 27.45 |
|     5      |    196    | 22.05 |
|     6      |    124    | 13.95 |
+------------+-----------+-------+
For the range (111, 1000), out of 889 iterations, the number 495 appears 832 times or 93.59% of the time.
The most common number (495), finishes in 1 loop(s).
```

## Contribute
Pull requests welcome. [Check issues](https://github.com/j-000/kc/issues) for ideas to help out.

## Why?
Bored of this quarantine and as Professor Roger Bowley put it in the video 
> _Not everything has to be useful to be appealing and fun._

## Next steps?
Let's try crack the Kaprekar's constant for the range 11111111 to 100000000. 
