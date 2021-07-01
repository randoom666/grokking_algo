def crop(width: int, height: int):
    if width % height == 0:
        return height
    else:
        crop(height, width % height)


width = input('Enter width')
height = input('Enter height')
if isinstance(width, float) or isinstance(height, float):
    print('You`re an asshole')
    width = int(width)
    height = int(height)
if width < height:
    height, width = width, height
min_height = crop(width, height)
print('Minimal square has height of:', min_height)