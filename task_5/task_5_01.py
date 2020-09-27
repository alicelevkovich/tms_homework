pupils = [
    {
        'firstname': 'Masha',
        'Group': 42,
        'physics': 7,
        'informatics': 6,
        'history': 8,
    },
    {
        'firstname': 'Alex',
        'Group': 45,
        'physics': 10,
        'informatics': 8,
        'history': 4,
    },
    {
        'firstname': 'Rudy',
        'Group': 44,
        'physics': 4,
        'informatics': 4,
        'history': 9,
    },
    {
        'firstname': 'Dasha',
        'Group': 43,
        'physics': 9,
        'informatics': 9,
        'history': 9,
    },
    {
        'firstname': 'Lisa',
        'Group': 45,
        'physics': 7,
        'informatics': 5,
        'history': 3,
    },
    {
        'firstname': 'Alena',
        'Group': 42,
        'physics': 6,
        'informatics': 7,
        'history': 8,
    },
    {
        'firstname': 'George',
        'Group': 44,
        'physics': 9,
        'informatics': 9,
        'history': 8,
    },
    {
        'firstname': 'Bella',
        'Group': 45,
        'physics': 10,
        'informatics': 10,
        'history': 10,
    },
    {
        'firstname': 'Boris',
        'Group': 43,
        'physics': 5,
        'informatics': 6,
        'history': 9,
    },
    {
        'firstname': 'Ned',
        'Group': 45,
        'physics': 8,
        'informatics': 8,
        'history': 8,
    },
]

sum_pupils = []
pupils_dict = {}

for pupil in pupils:
    avg = (pupil.get('physics') + pupil.get('informatics') + pupil.get('history')) / 3.0
    sum_pupils.append(avg)
    if avg > 4.0:
        pupils_dict[pupil.get('firstname')] = avg
print(sum_pupils)
print(pupils_dict)



