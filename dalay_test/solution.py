a = '''
SG-6000# show transceiver
Transceiver status information is shown as below:
================       ethernet0/4       =====================
SFP information:        JDSU / PLRXPLSCS4322N / 151123
Serial Number:                  CF48UF03T
Transmission media:             Multi-mode
Module temperature:             37.69    C
Tx supply voltage:              3.36     V
Tx bias current:                4.68    mA
Tx optical power:               -2.16   dBm
Rx optical power:               -4.01   dBm
===============================================================
================       ethernet0/5       =====================
SFP information:        JDSU / PLRXPLSCS4322N / 160526
Serial Number:                  CG22UF2UE
Transmission media:             Multi-mode
Module temperature:             38.50    C
Tx supply voltage:              3.36     V
Tx bias current:                5.36    mA
Tx optical power:               -2.18   dBm
Rx optical power:               -2.84   dBm
===============================================================
================       ethernet0/6       =====================
SFP information:        HGGENUINE / MTRS02X13G / 190622
Serial Number:                  MA19251360976
Transmission media:             Other Mode
Module temperature:             37.03    C
Tx supply voltage:              3.36     V
Tx bias current:                27.72   mA
Tx optical power:               -3.28   dBm
Rx optical power:               -2.86   dBm
===============================================================
================       ethernet0/7       =====================
SFP information:        HGGENUINE / MTRS02X13G / 190622
Serial Number:                  MA19251362053
Transmission media:             Other Mode
Module temperature:             36.93    C
Tx supply voltage:              3.37     V
Tx bias current:                27.36   mA
Tx optical power:               -3.29   dBm
Rx optical power:               -2.73   dBm
===============================================================
================       xethernet1/0       =====================
SFP+/XFP information:   JDSU / PLRXPLSCS4322N / 171112
Serial Number:                  CH46UF0WC
Transmission media:             Multi-mode
Module temperature:             33.32    C
Tx supply voltage:              3.45     V
Tx bias current:                4.91    mA
Tx optical power:               -2.17   dBm
Rx optical power:               -3.18   dBm
===============================================================
================       xethernet1/1       =====================
SFP+/XFP information:   JDSU / PLRXPLSCS4322N / 171112
Serial Number:                  CH46UF10Y
Transmission media:             Multi-mode
Module temperature:             33.18    C
Tx supply voltage:              3.46     V
Tx bias current:                5.02    mA
Tx optical power:               -2.15   dBm
Rx optical power:               -2.83   dBm
===============================================================
================       xethernet1/2       =====================
SFP+/XFP information:   JDSU / PLRXPLSCS4322N / 170120
Serial Number:                  CH04UF083
Transmission media:             Multi-mode
Module temperature:             34.16    C
Tx supply voltage:              3.45     V
Tx bias current:                6.19    mA
Tx optical power:               -2.27   dBm
Rx optical power:               -2.93   dBm
===============================================================
================       xethernet1/3       =====================
SFP+/XFP information:   JDSU / PLRXPLSCS4322N / 160330
Serial Number:                  CG14UF0GF
Transmission media:             Multi-mode
Module temperature:             38.38    C
Tx supply voltage:              3.44     V
Tx bias current:                6.08    mA
Tx optical power:               -2.24   dBm
Rx optical power:               -3.00   dBm
====================
====================
====================
===
SG-6000#
'''
import re

# re_r = '^={63}$'
# # d = re.split(re_r, a)
# # print(d)
# #
# # b = a.split('===============================================================')
# # print(b)
# #
# # for i in b:
# #     pass
    # print(i)

print(sum(range(0,101)))
