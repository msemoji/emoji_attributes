# emoji_attributes
Code to get emoji attributes for emojis in a list.

For example, with this code you can identify the Unicode group, subgroup, shape, color, description, and much more for the emojis in a list.
The attributes are compiled from Unicode group, subgroup, name and also manual review.

See the demo code for more details.

This code enables description and comparison of which emojis are used.

For example, for this list of emojis:
test_list_of_emojis = ['4️⃣', '❤️', '🇦', '🇦🇺', '🍎', '👨🏾\u200d👩🏾\u200d👧🏾\u200d👦🏾', '👩🏿\u200d💻', '👪🏿', '🗳️','🗳', '😃', '🟠’] 

The values of each for the Unicode group (from the Emoji Unicode charts: https://unicode.org/emoji/charts/full-emoji-list.html) are:
'group': ['Symbols', 'Smileys & Emotion', 'Symbols', 'Flags', 'Food & Drink', 'People & Body', 'People & Body', 'People & Body', 'Objects', 'Objects', 'Smileys & Emotion', 'Symbols']

