# Ringbar

RingBar is a Python package that helps you visualize progresses of any codes based on log timestamps.

## Install

WIP

## Usage

### input

```py
import ringbar
process_rb = ringbar.RingBar("2016/06/17 00:00:00", "2016/06/17 06:00:00")
process_rb.add("process1", start="2016/06/17 01:00:00", end="2016/06/17 02:34:56")
process_rb.add("process2", start="2016/06/17 03:21:09", error="2016/06/17 04:32:10")
process_rb.show()
```

### output

```
         2016/06/17
         0   1   2   3   4   5    
process1|....======>.............|
process2|.............=====x.....|
```

You can handle width of time chart by changing bins.

```
process_rb = ringbar.RingBar("2016/06/17 00:00:00", "2016/06/17 06:00:00", bin_width=10)
process_rb.add("process1", start="2016/06/17 01:00:00", end="2016/06/17 02:34:56")
process_rb.add("process2", start="2016/06/17 03:21:09", error="2016/06/17 04:32:10")
process_rb.show()
```

```
          2016/06/17
          0     1     2     3     4     5      
 process1|......=========>....................|
 process2|....................=======x........|
```


## Author

yag_ays ([@yag_ays](https://twitter.com/yag_ays))
