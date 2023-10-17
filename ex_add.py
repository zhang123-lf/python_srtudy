#！/usr/bin/env python3
# -*- coding : utf-8 -*-

a = 20

match a:
    case x if x> 18:
        print('ok')
    case 17 | 16 | 15:
        print('no')
    case _:
        print('again')


