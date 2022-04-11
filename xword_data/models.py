from django.db import models


class Puzzle(models.Model):
    """published crossword puzzle"""

    title = models.CharField(max_length=255)
    date = models.DateField()
    byline = models.CharField(max_length=255)
    publisher = models.CharField(max_length=12)

    def __str__(self):
        return self.title


class Entry(models.Model):
    entry_text = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.entry_text

    class Meta:
        verbose_name_plural = "entries"


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
