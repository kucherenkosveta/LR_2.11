#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def max_min(type='max'):
    def helper(collection):
        if type == 'max':
            return max(collection)
        else:
            return min(collection)
    return helper


if __name__ == '__main__':
    print(max_min(input("Введите max или min: "))
          (map(int, input("Введите список: ").split(' '))))
    
