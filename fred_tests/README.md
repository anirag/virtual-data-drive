# Silly tests

In this repo is a script for a BoNG + LR classifier (with `Agency` as target) that I threw together this morning.

## EVAL

Ran on a down-sampled dataset

```bash

              precision    recall  f1-score   support

         ACS      1.000     1.000     1.000         8
         DCA      1.000     1.000     1.000       325
        DCAS      1.000     1.000     1.000        19
         DEP      1.000     1.000     1.000      3452
        DFTA      1.000     1.000     1.000       122
         DHS      1.000     1.000     1.000       327
         DOB      1.000     1.000     1.000      2411
         DOE      1.000     1.000     1.000        36
         DOF      1.000     1.000     1.000       829
       DOHMH      1.000     1.000     1.000      1167
       DOITT      1.000     1.000     1.000        11
         DOT      1.000     1.000     1.000      5160
         DPR      0.999     1.000     1.000      1980
        DSNY      1.000     1.000     1.000      6470
         DVS      1.000     1.000     1.000         3
         EDC      1.000     1.000     1.000        25
        FDNY      1.000     1.000     1.000         1
         HPD      1.000     1.000     1.000      9600
         HRA      1.000     1.000     1.000       167
       NYCEM      1.000     1.000     1.000         7
        NYPD      1.000     1.000     1.000     13923
         TAT      1.000     1.000     1.000         1
         TAX      1.000     1.000     1.000         1
         TLC      1.000     1.000     1.000       542

    accuracy                          1.000     46587
   macro avg      1.000     1.000     1.000     46587
weighted avg      1.000     1.000     1.000     46587
```
