from django.db import models


class Puzzle(models.Model):
    """published crossword puzzle"""

    title = models.CharField(max_length=255, )
    date = models.DateField()
    byline = models.CharField(max_length=255)
    publisher = models.CharField(max_length=12)

    @property
    def get_title(self):
        if self.title == "":
            return f"Untitled - {self.publisher} {self.byline}: {self.date}"
        else:
            return self.title

    def __str__(self):
        return self.title


class Entry(models.Model):
    entry_text = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return self.entry_text


class Clue(models.Model):
    entry = models.ForeignKey(
        "Entry",
        on_delete=models.PROTECT,
    )
    puzzle = models.ForeignKey(
        "Puzzle",
        on_delete=models.PROTECT,
    )
    clue_text = models.CharField(max_length=512)
    theme = models.BooleanField(default=False)

    def __str__(self):
        return self.clue_text
