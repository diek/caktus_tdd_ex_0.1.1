from urllib.parse import urlencode

from django.shortcuts import redirect, render
from django.urls import reverse

from .app_utils import generate_random
from .forms import ClueForm
from .models import Clue, Entry, Puzzle


def drill(request):
    """
    1. presents a random clue with information about the entry (length and puzzle
      where it appeared) to the user,

    2. includes an input field where the user can provide a guess at the answer.

    3. i. Input of an incorrect guess should re-display the same clue with a note the
      answer is not correct.
    or
      ii. Input of a correct answer should redirect to the answer view for that
      clue.

    The drill view's rendered page should offer the user an "escape hatch" to see the answer
      even if they cannot correctly guess it.
    """

    form = ClueForm(request.GET or None)
    if form.is_valid():
        guess = form.cleaned_data["answer"]
        clue_id = request.GET["clue_id"]
        clue = Clue.objects.get(pk=clue_id)
        correct_answer = clue.entry.entry_text
        if guess.upper() == correct_answer:
            # answer_link_url = reverse("xword-answer", kwargs={"clue_id": int(clue_id)})
            answer_link_url = reverse('xword-answer', args=(clue_id,))
            return redirect(answer_link_url)
        else:
            incorrect_answer = True
            return render(
                request,
                "xword_data/drill.html",
                {"clue": clue, "incorrect_answer": incorrect_answer},
            )
    else:
        incorrect_answer = None
        random_clue = generate_random()
        clue = Clue.objects.get(pk=random_clue)
        return render(request, "xword_data/drill.html", {"clue": clue, "form": form})


def answer(request, clue_id):
    """
    - **Answer view:** when reached via a successful guess, this view congratulates the user on
      their success and offers up some additional data about the clue.

      - If this is the only occurrence of the clue in the database then that is stated.

      - If, however, the clue appears more than once in the database then the answer page for the
        clue present
         1. a table of Entries associated with the clue, and
         2. a count of how many times that Clue/Entry pair appear in the
      database.
    """

    clue = Clue.objects.get(pk=clue_id)
    puzzle_detail = Puzzle.objects.get(pk=clue.puzzle_id)
    return render(
        request,
        "xword_data/answer.html",
        {"correct_answer": clue.entry.entry_text, "puzzle_detail": puzzle_detail},
    )
