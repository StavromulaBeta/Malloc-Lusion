# Malloc-Lusion

*Malloc-Lusion™* is possibly the world's first *Orthodontic Programming Language (OPL)*. Programs are comprised of the relative positions of teeth in the programmer's mouth, as ascertained by panoramic radiograph.

![Panoramic radiograph example](input3.png)

## Language Overview

*Malloc-Lusion™* interprets data as stored in the programmer's mouth. The position of each tooth encodes an instruction. As such, the programmer writes code via conventional orthodontic manipulation of their teeth (albeit in potentially unconventional directions). Programs are input as a *grayscale* png file of a panoramic radiograph taken of the programmer. The (standardized) deviance of each tooth, read left-right, top-bottom, from the mean dental arch are then used to perform calculations.

![As seen by the program](input3_eroded.png)

## Programming

After installing the required libraries, a program can be run as follows:
```
./malloclusion input.png
```

Each instruction is encoded by the location of successive teeth in the programmer's mouth, read left-right, top-bottom on the provided panoramic radiograph. An operand is the absolute standard deviation of a tooth relative to its arch, in units of its height, multiplied by 10. The language itself comprises of manipulating 8-bit integers on a stack.

```
0: Push (multiplying by 100) teeth to the stack until 0 encountered
1: Add top 2 stack items, push result
2: Subtract top of stack from second top, push result
3: Multiply top 2 stack value, push result
4: Divide second top value by top, push result
5: Print top stack value as number
6: Print top stack value as ascii character
7: Jump instruction pointer to top of stack value
8: Print the entire stack as numbers
9: Print the entire stack as a string
10: Drop top stack item
11: Clone top stack item
12: Swap top stack items
13+: Halt
```

Most people's teeth are either infinite loops or simply push garbage to the stack. This is not our failing, but rather a failing of modern orthodontics. Do better.

# Hello world

Unfortunately we haven't yet managed to find a volunteer for our hello world program, but it might look something like this:

![Hello world program (teeth](helloworld_eroded.png)

## Interpreter

The provided interpreter for *Malloc-Lusion™* is written in Python and uses [RobertSmithers/TeethSegmentation](https://github.com/robertsmithers/teethsegmentation). A convolutional neural network to identifies the position of each tooth in the input panoramic radiograph and masks them out in turn, such that the vertical deviations can be computed using OpenCV.


## FAQ

Q: What if I want to write longer programs?

A: Get more teeth.
