import sys
import numpy as np
from PIL import Image
import wikipedia ## to extract information
from wordcloud import WordCloud,STOPWORDS
import datetime

## we will import STOPWORD because to remove common words like "the , a , than , here , after "

a = str(input("Enter the name of which you want to make word cloud : "))
title = wikipedia.search(a)[0] ##it will search the title from wikipedia
page = wikipedia.page(title) ## it will search the page related to given topic in wikipedia
text = page.content ## to extract the  content of that topic
print(text)

bg = np.array(Image.open("abcd.jpg"))  ## download the backgroud image because we need base on which  our words will print
unwated_words = set(STOPWORDS)
wordclo = WordCloud(background_color="black",max_words= 400, mask= bg, stopwords=unwated_words)
wordclo.generate(text)

#### to get unique name using date_time
now = datetime.datetime.now()
current_time = str(now)
name = f"{current_time[:-7]}"
name = (str(name)).replace(' ','')
name = name.replace(':','-')

wordclo.to_file(f"{a}_{name}.png")  ## what name you want to save
