from django.shortcuts import render


def drill(request):
    """
    - **Drill view:** presents a random clue with information about the entry (length and puzzle
      where it appeared) to the user, and includes an input field where the user can provide a guess
      at the answer. Input of an incorrect guess should re-display the same clue with a note the
      answer is not correct. Input of a correct answer should redirect to the answer view for that
      clue. The drill view's rendered page should offer the user an "escape hatch" to see the answer
      even if they cannot correctly guess it.
    """
    return render(request, "xword_data/drill.html")


def answer(request):
    """
    - **Answer view:** when reached via a successful guess, this view congratulates the user on
      their success and offers up some additional data about the clue. If this is the only
      occurrence of the clue in the database then that is stated. If, however, the clue appears more
      than once in the database then the answer page for the clue presents a table of Entries
      associated with the clue and a count of how many times that Clue/Entry pair appear in the
      database.
    """
    return render(request, "xword_data/answer.html")
