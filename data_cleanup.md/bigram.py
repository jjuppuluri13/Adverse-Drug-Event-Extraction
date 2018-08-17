#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 12:55:12 2018
@author: jjuppuluri13
"""

#import data_proc

list_len = len(df.sentence)
bigram_count = []
i = 0
while i < list_len:
    k = 0
    check = 0
    word = df.drug[i]
    while k < len(word):
        if word[k] == ' ':
            bigram_count.append(1)
            check += 1
            break
        k += 1
    if check == 0:
        bigram_count.append(0)
    i += 1

#print (bigram_count)
#print (len(bigram_count))

j = 0
while j < list_len:
    drug = df.drug[j]
    if bigram_count[j] > 0:
        df.sentence[j] = df.sentence[j].replace(drug, drug.replace(" ", "_"))
    j += 1

g = 0
while g < 6821:
    if bigram_count[g] == 1:
        df.drug[g] = df.drug[g].replace(" ", "_")
    g += 1
