words = [
         'PUBLIC ART', 
         'AI', 
         'ARTIFICIAL INTELLIGENCE', 
         'DIGITAL', 
         'XR',
         'SCULPTURE', 
         'DIGITAL ART', 
         'STYLE', 
         'IDEA', 
         'GREEN DESIGN', 
         'HCPS', 
         'INNOVATION', 
         'CREATIVE', 
         'EMOTION', 
         'INTERACTION DESIGN', 
         'SMART', 
         'FUNCTION', 
         'FASHION DESIGN', 
         'GREEN', 
         'ORIGINALITY', 
         'DESIGN THINKING', 
         'STRATEGY', 
         ]

count = [140, 210, 220, 220, 160, 80, 180, 100, 110, 40, 80, 190, 220, 40, 80, 170, 100, 80, 90, 80, 80, 30]

text = './doc/xauat.txt'

with open(text, 'w', encoding='utf-8') as f:
    for i in range(len(words)):
        word_to_add = (words[i]+' ') * count[i] 
        f.write(word_to_add)
        
    
     