task_num = int(input("enter task number:(1-9) "))

import functions


if task_num < 1 or task_num > 9:
    print("not_proper range")
elif task_num == 1:
    functions.draw_circle()
elif task_num == 2:
    functions.draw_rectangle()
elif task_num == 3:
    functions.draw_square()
elif task_num == 4:
    functions.rhombus()
elif task_num == 5:
    functions.hello()
elif task_num == 6:
    functions.python()
elif task_num == 7:
    functions.eight_angle()
elif task_num == 8:
    functions.ten_angle()
elif task_num == 9:
    functions.tree()

functions.screen_off()