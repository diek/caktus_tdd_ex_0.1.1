from urllib.parse import urlencode

from django.shortcuts import redirect, render
from django.urls import reverse

from .app_utils import generate_random
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

    if request.method == 'GET':
        user_answer = request.GET["answer"]
        post_id = request.GET["postId"]
        clue = Clue.objects.get(pk=post_id)
        correct_answer = clue.entry.entry_text
        if user_answer.upper() == correct_answer:
            base_url = reverse("answer")
            query_string = urlencode({'correct_answer': correct_answer})
            url = f"{base_url}?{query_string}"
            return redirect(url)
        else:
            return render(request, "xword_data/drill.html", {"clue": clue})
    else:
        random_clue = 1  # generate_random()
        clue = Clue.objects.get(pk=random_clue)
        return render(request, "xword_data/drill.html", {"clue": clue})


def answer(request):
    """
    - **Answer view:** when reached via a successful guess, this view congratulates the user on
      their success and offers up some additional data about the clue. If this is the only
      occurrence of the clue in the database then that is stated. If, however, the clue appears more
      than once in the database then the answer page for the clue presents a table of Entries
      associated with the clue and a count of how many times that Clue/Entry pair appear in the
      database.
    """
    correct_answer = request.GET.get('correct_answer')
    return render(request, "xword_data/answer.html", {"correct_answer": correct_answer})
