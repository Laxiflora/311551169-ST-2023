# Equivalent class
COR_4 :
(m4 != 0 ^ (m100 == 0 && m400 != 0))
(m4 != 0 | (m100 == 0 && m400 != 0))
`year%100 -> year%4==0`

AOIS_51:
25 : numDays = day2 + (daysIn[month1] - day1++);

got error but no failure

AOIS_71:
27 : numDays = daysIn[i] + numDays++;
`後綴++的優先度高於assign，所以在numDays後面補上++只會在運算途中有短暫的error，但不會造成failure`

AOIS_11:
numDays = day2++ - day1;
`後續不會再用到days2，故雖然有error但不會有failure`

AOIU_5:
int m100 = -year % 100;
`m100只用於檢測是否==0，正負號不影響結果`

AOIS_39:
if (m4 != 0 || m100 == 0 && m400++ != 0)
`m400後續不會用到`



AOIU_4:
17 :  int m4 = -year % 4;
`若year%4==0, 則-year%4==0`

ROR_4:
    if (month2 <= month1) 
    `程式有擋month1>=month2`