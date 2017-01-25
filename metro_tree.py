# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 15:47:18 2017

@author: stpl
"""
#pc, pc, lkm, rc = 2,3,4,5;
rc, pc, cs, lkm = {'pc' : 2, 'cs' : 3, 'lkm' : 4, 'ub' : 5}, {'cs' : 3, 'lkm' : 4, 'ub': 5}, {'lkm' : 4, 'ub': 5}, {'ub': 5};


met = {'rc' : rc,
       'pc' : pc,
       'cs' : cs,
       'lkm' : lkm};
       
s = input("source : ");
d = input("destination : "); 

dist = 0;


try:
    if (s in met and d in [ k for k,v in met[s].items()]):
        for k, v in (met[s].items()):
            print(k,v);
            dist += v;
            if k == d:
                print('terminating:',k)
                break;

except:
    print("Stations not found... Please check the Entered stations....");
    
print('\nTotal Time to reach is approx: {} min.'.format(dist));
       
