desire_amount = int(input("Desired amount:"))
face_value = [1, 2, 5, 10, 20, 50, 100]
face_value.reverse()
number_of_note = [0] * len(face_value)

for i in range(len(face_value)):
    if desire_amount//face_value[i]:
        number_of_note[i] = desire_amount//face_value[i]
    desire_amount = desire_amount % face_value[i]

for i in range(len(face_value)):
    if number_of_note[i]:
        print("${} : {}".format(face_value[i], number_of_note[i]))

