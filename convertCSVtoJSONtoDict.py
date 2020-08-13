#!/usr/bin/env python
# coding: utf-8

# # CSV to JSON to DICT

# In[15]:



# The current csv and dictionary contains 4194 emojis 
# which are from https://unicode.org/Public/emoji/13.0/emoji-test.txt plus regional indicators letter symbols 

# note that this list also includes unqualified and minimally qualified emojis which may appear to look like a duplicate of other emojis
# but the codepoints are different. also note that there are additional emojis supported on some platforms but are 
# not supported by unicode and thus not in this list - e.g. twitter and microsoft have some family emojis with skin tone 



# attributes in dict dict attribute fields
#['rownum', 'emoji', 'group', 'subgroup', 'grp_subgrp', 'cldr short name', 'status' ,
# 'char_len', 'version',  'codepoint', 
#'desc', 'person_animal_other', 'anthro_type', 'gender', 'skin_tone', 'sent_smileys_binary',
#'shape_type', 'shape_color',
#'direction' ]



# In[16]:



## USE THIS TO CONVERT CSV TO DICT WITH VALUES FROM ONE OF THE COLUMNS AS THE KEY AND THEN SAVE TOTAL DICT AS JSON 

import csv
# load in csv and convert it to a dictionary
csv_emoji_data = []
emoji_dict = dict()
with open('emoji_all_v13_attributes_w_color_anthro_sentiment_shape_direction.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    header = []
    i = 0
    for row in csvreader:
        row_dict = dict()
        individual_emoji_data = dict()
        if i == 0:
            header = row
            print(header)
            i += 1
        elif i > 0:
            csv_emoji_data.append(row)
            col_num = 0
            for col_num in range(0,len(header)):
                #if col_num > 1: # skip the first two cols which is the unique row id, and the emoji
                row_dict[header[col_num]] = row[col_num]
            
            emoji_dict[row[1]] = row_dict # {emoji_happy_face:{'group':'smileys&people','subgroup':'happy'...}}
            
            i += 1
        else:
            break

# verifying they are the same size (based on unique values in column used for dictionary keys - e.g. emoji)            
print(len(emoji_dict), len(csv_emoji_data))     



# In[18]:


# list of all unique values for each attribute

attributes_type_list = ['rownum', 'emoji', 'cldr short name', 'codepoint',                        'status' , 'char_len', 'version',                         'group', 'subgroup', 'grp_subgrp',                         'desc', 'person_animal_other', 'anthro_type',                        'gender', 'skin_tone', 'sentiment_smileys_binary',                        'shape_type', 'shape_color', 'direction' ]


for i in range(len(attributes_type_list)):
    if i > 3:
        val_list = set([attributes[attributes_type_list[i]] for emoji, attributes in emoji_dict.items()])
        print( attributes_type_list[i], val_list)
        print()


# In[19]:


# write out dictionary as json
import json
with open('emoji_all_v13_attributes_w_color_anthro_sentiment_shape_direction.json', 'w', encoding='utf-8') as out_file:
    out_file.write("{") 
    c = 0
    max_c = len(emoji_dict)
    for emoji, emoji_values in emoji_dict.items():
        out_file.write('"'+emoji+'":')
        
        json.dump(emoji_values, out_file, ensure_ascii=False)
        if c < max_c-1:
            out_file.write(",\n")
            c+=1
        else:
            out_file.write("\n")
    out_file.write("}") 
# structure of output file is      
#{
#"😃": {"rownum": "2", "emoji": "😃", "grp_subgrp": "Smileys & Emotion_face-smiling"},
#"😄": {"rownum": "3", "emoji": "😄", "grp_subgrp": "Smileys & Emotion_face-smiling"}
#}

print('done')


# In[21]:


# load in a json of dictionaries into a new dictionary

# strucutre in file is: 
#{
#"😃": {"rownum": "2", "emoji": "😃", "grp_subgrp": "Smileys & Emotion_face-smiling"},
#"😄": {"rownum": "3", "emoji": "😄", "grp_subgrp": "Smileys & Emotion_face-smiling"}
#}
with open('emoji_all_v13_attributes_w_color_anthro_sentiment_shape_direction.json') as f:
    emoji_w_attributes_dict = json.load(f)    
    
        
        
        
print(type(emoji_w_attributes_dict), len(emoji_w_attributes_dict))   
print()

#attributes_type_list = ['rownum', 'emoji', 'cldr short name', 'codepoint',\
#                        'status' , 'char_len', 'version', \
#                        'group', 'subgroup', 'grp_subgrp',\
#                         'desc', 'person_animal_other', 'anthro_type',\
#                        'gender', 'skin_tone', 'sentiment_smileys_binary',\
#                        'shape_type', 'shape_color', 'direction' ]


i = 0
for emoji, attributes in emoji_w_attributes_dict.items():
    if i < 5:
        print(emoji, attributes['emoji'])
        i += 1
    else:
        break


# In[ ]:




