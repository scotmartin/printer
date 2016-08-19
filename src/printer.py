from escpos.printer import Usb
p = Usb(0x04b8,0x0e15)
p.text("Hello World!")
p.cut()
