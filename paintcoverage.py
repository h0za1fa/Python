wall_hieght=int(input('Enter hieght: '))
wall_width=int(input('Enter width: '))
coverage=5

def paint_needed(hieght,width,coverage) -> int:
    area=hieght*width
    paint_req=round(area/coverage , 1)
    paint_req_int=int(paint_req)
    if paint_req > int(paint_req):
        paint_req_int+=1
    return paint_req_int

print(f'Paint required is {paint_needed(wall_hieght,wall_width,coverage)}')