# -*- coding: UTF-8 -*-
from escpos.printer import Usb
import datetime
# setup
p = Usb(0x04b8,0x0e15)
p.set(align=u'left', font=u'a', text_type=u'normal', width=1, height=1, density=9, invert=False, smooth=False, flip=False)
	
# p.text('{:*^64}'.format('centered'))
# p.text('Sentences with number of characters are cool too\n')
# p.set(font='a', text_type='b')
# p.text('ISIN\n')
p.set(font='b', text_type='normal')
# ISIN is max 13 long
# p.text('{:<13} {:>7} {:>10}\n'.format('DE0002635299', '163.413', '2.514,93 €'))
# p.text('{:<13} {:>7} {:>10}\n'.format('------------', '-------', '=========='))

p.text('_{:_^14}|{:_^15}|{:_^15}|{:_^15}_\n'.format(' ISIN ',' QTY ',' PRICE ',' VALUE '))
isin = 'DE0002635299'
quantity = 2.739
price = 164.450
value = quantity * price
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
p.text('|{:^14}|{:^15}|{:^15}|{:^15}|\n'.format(isin,quantity,price,value))
p.text('|{:^14}|{:^15}|{:^15}|{:^15}|\n'.format(isin,quantity,price,value))
p.text('|{:^14}|{:^15}|{:^15}|{:^15}|\n'.format(isin,quantity,price,value))
p.text('|{:^14}|{:^15}|{:^15}|{:^15}|\n'.format(isin,quantity,price,value))
p.text('|{:^14}|{:^15}|{:^15}|{:^15}|\n'.format(isin,quantity,price,value))
p.text('|{:^14}|{:^15}|{:^15}|{:^15}|\n'.format(isin,quantity,price,value))
p.text('|{:^14}|{:^15}|{:^15}|{:^15}|\n'.format(isin,quantity,price,value))
p.text('|{:^14}|{:^15}|{:^15}|{:^15}|\n'.format(isin,quantity,price,value))
p.text('|{:^14}|{:^15}|{:^15}|{:^15}|\n'.format(isin,quantity,price,value))
p.text('|{:^14}|{:^15}|{:^15}|{:^15}|\n'.format(isin,quantity,price,value))
p.text('|{:-^62}|\n'.format(''))
p.text('|{:^15}{:^16}{:>15}:{:^15}|\n'.format('','','SUM',value))
p.text('= {:=<62}'.format(date + ' ='))

p.cut()
