# Candidate Verification System
from pyscript import display, document


def student_club(e):
    document.getElementById('output').innerHTML = '' # No multiple outputs
    student_fname = document.getElementById('student_firstname').value
    student_lname = document.getElementById('student_lastname').value
    chiikawa_members = ['Chiikawa Dela Cruz', 'Usagi Santos', 'Hachiware Bautista', 'Momonga Garcia', 'Rakko Ramos', 'Kurimanju Fernandez', 'Shisa Castillo']
    full_name = student_fname + ' ' + student_lname
    member_checker = full_name in chiikawa_members

    display_message = (f'Sorry, your name is not on the list.', f'Congratulations {full_name}! You are now part of the Chiikawa club.')

    display(display_message[member_checker], target='output')