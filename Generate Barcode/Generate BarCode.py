import barcode
data="1109200019121998"
k=barcode.get_barcode_class('Code128')
r=k(data)
c=r.save('barcode')