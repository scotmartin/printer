from escpos.printer import Usb
p = Usb(0x04b8,0x0e15)
p.set(align=u'left', font=u'b', text_type=u'normal', width=1, height=1, density=9, invert=False, smooth=False, flip=False)
p.text("Hello world!")
p.text('\n')
p.text('{:>12}  {:>12}  {:>12}'.format('Hello','Martin','Hello'))
p.text('\n')
p.text('{:*^64}'.format('centered'))
p.text('\n')
p.text('Sentences with number of characters are cool too')
p.text('\n')
p.set(text_type='B')
p.text('Sentences with number of characters are cool too')
p.cut()
