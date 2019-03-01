import sys

args = sys.argv
input_file = open(args[1], 'r')
output_file = open(args[2], 'w')

lines = int(input_file.readline())

horizontal_slides = {}
vertical_slides = {}
verticals = {}
transitions_slides = {}
transitions = {}
tags = []

for i in range(lines):
    photo_data = input_file.readline().rstrip()
    photo_data_list = photo_data.split(' ')

    # separate horizontals
    if photo_data_list[0] == 'H':
        for j in range(int(photo_data_list[1])):
            tags.append(photo_data_list[j + 2])
        horizontal_slides.update({(i,): tags})

    # separate verticals
    if photo_data_list[0] == 'V':
        for j in range(int(photo_data_list[1])):
            tags.append(photo_data_list[j + 2])
        verticals[i] = tags
    tags = []


# create slides out of verticals
v_len = len(verticals)

if v_len == 2:
    v_ids = tuple(list(verticals.keys()))
    v_tags = list(set(verticals[1] + verticals[2]))
    vertical_slides.update({v_ids: v_tags})
elif v_len > 2:
    verticals1 = list(verticals.items())[:v_len//2]
    verticals2 = list(verticals.items())[v_len//2:]
    for i, j in zip(verticals1, verticals2):
        v_ids = (i[0], j[0])
        v_tags = list(set(i[1] + j[1]))
        vertical_slides.update({v_ids: v_tags})

horizontal_transitions = sorted(horizontal_slides.items(), key=lambda kv: kv[1])
vertical_transitions = sorted(vertical_slides.items(), key=lambda kv: kv[1])

len_hor = len(horizontal_slides)
len_ver = len(vertical_slides)
if len_hor > 0 and len_ver > 0:
    transitions_slides = {**horizontal_slides, **vertical_slides}
elif len_hor == 0:
    transitions_slides = {**vertical_slides}
else:
    transitions_slides = {**horizontal_slides}
transitions = sorted(transitions_slides.items(), key=lambda kv: kv[1])

# data for output
S = len(transitions) # no. of slides
output_file.write("{}\n".format(S))

for i in transitions:
    if len(i[0]) == 2:
        output_file.write("{} {}\n".format(i[0][0], i[0][1]))
    else:
        output_file.write("{}\n".format(i[0][0]))

output_file.close()
input_file.close()
