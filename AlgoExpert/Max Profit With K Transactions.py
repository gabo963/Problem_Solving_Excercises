# -*- coding: utf-8 -*-
"""
AlgoExpert
Max profit with K Transactions
"""

prices = [5, 10, 2, 10, 2, 90]
k = 3

def maxProfitWithKTransactions(prices, k):
    # Write your code here.
    
    if len(prices) == 0:
        return( 0 )
    
    possibleProfit = [[ 0 for i in range(len(prices)) ] for j in range(k) ]
    
    for trade in range( 1, k + 1):
        for i, p in enumerate(prices):
            maxVal = float("-inf")
            MaxMins = 0
            NextTrades = 0
            
            if i > 0:    
                MaxMins = max( [p - prices[c] for c in range(0,i)] )
                
                if trade > 1:
                    NextTrades = max([ possibleProfit[trade-2][ c ] + p - prices[c+1] for c in range(0,i)])
                
            maxVal = max( maxVal, MaxMins, NextTrades, possibleProfit[trade-1][ i-1 ] )
            
            possibleProfit[trade-1][ i ] = maxVal
            
    return( possibleProfit[-1][-1] )

print( maxProfitWithKTransactions(prices, k) )