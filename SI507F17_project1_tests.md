## Write in plain english, what will you do to test everything mentioned in the description

- Deck Shuffle
    - Before shuffle, create a list of strings for self.cards
        - cards_strings = [str(c) for c in self.cards]
    - After shuffle, do this again
        - cards_strings_shuffled
    - compare them for equality
- Show Song
    - s = show_song()
    - self.assertIsInstance(s, Song)
    - self.assertTrue(isinstance(s, Song))

    - s2 = show_song('Bowie')
    - print(s2)
    - self.assertTrue('Bowie' in str(s2))
