from django.contrib import admin

from .models import Clue, Entry, Puzzle


class PuzzleAdmin(admin.ModelAdmin):
    fields = ["title", "publication_date", "byline", "publisher"]


class EntryAdmin(admin.ModelAdmin):
    fields = ["entry_text"]


class ClueAdmin(admin.ModelAdmin):
    fields = ["entry", "puzzle", "clue_text"]


admin.site.register(Clue, ClueAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Puzzle, PuzzleAdmin)
