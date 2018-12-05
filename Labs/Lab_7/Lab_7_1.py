user_input = "35642"
desire_amount = int(user_input)

available_notes =[100, 50, 20, 10, 5, 2, 1]
note_number = [0]* len(available_notes)

for i in range(len(available_notes)):
    if desire_amount:
        if not desire_amount//available_notes[i]:
            continue
        else:
            number_of_note, desire_amount = divmod(desire_amount, available_notes[i])
            note_number[i] = number_of_note
    else:
        break

for note, number in zip(available_notes, note_number):
    if number:
        print('${:>4}: {}'.format(note, number))