# diffenshtein

An implementation version of Levenshtein distance which will show the alignment output between 2 sentences. The example output is shown below:  

```
Seq 1: s i t t i n g
Seq 2: k i t t e n ***
Sys:   S C C C S C D
Min error: 3
===========================
Seq 1: k i t t y ***
Seq 2: k i t t e n
Sys:   C C C C S I
Min error: 2
===========================
Seq 1: s i t t i n g
Seq 2: f i t t i n g
Sys:   S C C C C C C
Min error: 1
===========================
```
