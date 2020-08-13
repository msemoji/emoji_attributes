#!/usr/bin/env python
# coding: utf-8

# In[1]:


# This code demonstates how to get attributes for emojis in a list using a reference dictonary compiled for this


# ABOUT THE EMOJI ATTRIBUTE REFERENCE FILE
# The attributes are compiled from Unicode emoji data files emoji-test.txt and also manual review
# Unicode data files: https://unicode.org/Public/emoji/13.0/
# there may be some emojis that render but are not fully supported by Unicode (e.g. family with skintone)
# and thus may not be in the master reference of emoji attributes


# values for emoji group, subgroup, name, status, version are from Unicode
# attributes for shape, color, direction, gender, skin_tone are based on Unicode name
# desc, person_animal_other, anthro_type, were assigned by the author but could be changed
# sentiment did a positive (1) or negative (-1) or neutral (0) based on smileys, this could be modified
# additonal fields could be added for other groupings
# additional resources are: https://emojipedia.org/ and https://unicode.org/emoji/charts/full-emoji-list.html


# In[2]:


import getEmojiAttributes


# In[3]:


# to see the attributes in the master attribute reference for a single emoji
#getEmojiAttributes.emoji_w_attributes_dict['😀'] # directly access the reference

emoji_of_interest = '😀'

# get a dictionary of attributes for a single emoji, 
# if it is not in the reference list and is a family with skintones it will create the attributes for it
getEmojiAttributes.getAttributesForSingleEmoji(emoji_of_interest)


# In[4]:


#this test_emoji is not in the reference because most family with skin tones are not fully supported by Unicode
# however this code analyzes the emoji and builds the attributes for the family with skin tone emojis on the fly

test_emoji = '👨🏾\u200d👩🏾\u200d👧🏾\u200d👦🏾'

getEmojiAttributes.getAttributesForSingleEmoji(test_emoji)


# In[5]:


# Get a list of the values for a specific attribute for emojis in a list with that attribute
# the input is a list of emojis and a string of the attribute name, if a list is passed it only takes the first value

attributes_in_ref_to_choose_from = ['group', 'subgroup', 'grp_subgrp',                         'desc', 'person_animal_other', 'anthro_type',                        'gender', 'skin_tone',                         'shape_type', 'shape_color', 'direction',                          'emoji', 'cldr short name','sentiment_smileys_binary',
                        'status' , 'char_len', 'version','rownum', 'codepoint']


attribute_to_get = 'group'

test_list_of_emojis = ['4️⃣', '❤️', '🇦', '🇦🇺', '🍎', '👨🏾\u200d👩🏾\u200d👧🏾\u200d👦🏾', '👩🏿\u200d💻', '👪🏿', '🗳️','🗳', '😃', '🟠']

print(attribute_to_get)
print(getEmojiAttributes.getListOfSingleAttributeValuesForEmojiList(test_list_of_emojis, attribute_to_get))


# In[6]:


# Get a list of the sorted unique values for a specific attribute for emojis in a list with that attribute
# the input is a list of emojis and a string of the attribute name, if a list is passed it only takes the first value

attributes_in_ref_to_choose_from = ['group', 'subgroup', 'grp_subgrp',                         'desc', 'person_animal_other', 'anthro_type',                        'gender', 'skin_tone',                         'shape_type', 'shape_color', 'direction',                          'emoji', 'cldr short name','sentiment_smileys_binary',
                        'status' , 'char_len', 'version','rownum', 'codepoint']


attribute_to_get = 'group'

test_list_of_emojis = ['4️⃣', '❤️', '🇦', '🇦🇺', '🍎', '👨🏾\u200d👩🏾\u200d👧🏾\u200d👦🏾', '👩🏿\u200d💻', '👪🏿', '🗳️','🗳', '😃', '🟠']

print(attribute_to_get)
print(getEmojiAttributes.getUniqueListOfSingleAttributeValuesForEmojiList(test_list_of_emojis, attribute_to_get))


# In[7]:


# get a dict of select attributes values for emojis in a list
# input is a list of emojis and a list of attributes

attributes_in_ref_to_choose_from = ['group', 'subgroup', 'grp_subgrp',                         'desc', 'person_animal_other', 'anthro_type',                        'gender', 'skin_tone',                         'shape_type', 'shape_color', 'direction',                          'emoji', 'cldr short name','sentiment_smileys_binary',
                        'status' , 'char_len', 'version','rownum', 'codepoint']


test_list_of_emojis = ['4️⃣', '❤️', '🇦', '🇦🇺', '🍎', '👨🏾\u200d👩🏾\u200d👧🏾\u200d👦🏾', '👩🏿\u200d💻', '👪🏿', '🗳️','🗳', '😃', '🟠']
attributes_to_get = ['group','shape_color']

dict_of_values_for_test_emojis = getEmojiAttributes.getDictOfValuesForEmojiAttributesOfInterest(test_list_of_emojis,attributes_to_get)
dict_of_values_for_test_emojis


# In[8]:


# get a dict of select attributes and sorted unique values for emojis in a list
# input is a list of emojis and a list of attributes

attributes_in_ref_to_choose_from = ['group', 'subgroup', 'grp_subgrp',                         'desc', 'person_animal_other', 'anthro_type',                        'gender', 'skin_tone',                         'shape_type', 'shape_color', 'direction',                          'emoji', 'cldr short name','sentiment_smileys_binary',
                        'status' , 'char_len', 'version','rownum', 'codepoint']


test_list_of_emojis = ['4️⃣', '❤️', '🇦', '🇦🇺', '🍎', '👨🏾\u200d👩🏾\u200d👧🏾\u200d👦🏾', '👩🏿\u200d💻', '👪🏿', '🗳️','🗳', '😃', '🟠']
attributes_to_get = ['shape_color','group']

dict_of_values_for_test_emojis = getEmojiAttributes.getDictOfUniqueValuesForEmojiAttributesOfInterest(test_list_of_emojis,attributes_to_get)
dict_of_values_for_test_emojis


# In[9]:


# create a dictionary of all attributes for all emojis in a list

test_list_of_emojis = ['4️⃣', '❤️', '🇦', '🇦🇺', '🍎', '👨🏾\u200d👩🏾\u200d👧🏾\u200d👦🏾', '👩🏿\u200d💻', '👪🏿', '🗳️','🗳', '😃', '🟠']

subset_emoji_attributes_dict = getEmojiAttributes.getDictOfEmojiAttributes(test_list_of_emojis)

print('number of emojis in list:', len(test_list_of_emojis))
print('number of emojis in list found in master attribute ref:', len(subset_emoji_attributes_dict))
print()
print('Show dictionary of emojis with attributes for emoji list')
subset_emoji_attributes_dict
        


# In[ ]:




