#!/usr/bin/env python
import random
import sys
import requests
from BeautifulSoup import BeautifulSoup

''' a small assistant for Valerie Aurora's TCP/IP Drinking game (http://valerieaurora.org/tcpip.html) '''

print 'fetching questions...'
r = requests.get('http://valerieaurora.org/tcpip.html')
soup = BeautifulSoup(r.text)

questions = []
for q in soup.findAll('ul'):
    question = {'Q': q.contents[1].text,
                'A': q.contents[2].text,
                'Credit': q.contents[3].text}
    questions.append(question)
print 'done.\n'

# actually start the game
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\
welcome to the TCP/IP drinking game.\n\
You can play the TCP/IP drinking game just about any way you want,\n\
as long as you remember that the point is to have fun laughing at the bizarre questions\n\
which no human being actually knows the answers to. Here\'s a suggestion:\n\
Pass some token around in a circle. The person in possession of the token asks a question of the person next in line.\n\
If you get the wrong answer, drink to punish yourself. If you get the right answer, everyone drinks. \n\
If your answer is particularly amusing or clever, everyone (including you) drinks two shots. Remember, nobody wins a drinking game.\n\
I will ask you one question at a time. If you want to know the answer, press enter.\n\
To get to the next question, press enter again.\n\
Cheers!\n\
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'


while(questions):
    # choose random question and remove it so it won't be asked again
    question = questions[random.randint(0,len(questions)-1)]
    raw_input(question['Q'])
    print question['A']       
    print question['Credit'],'\n..................................................................................................................................'
    questions.remove(question)

print('Done! Whoever\'s not puking yet is truly a TCP/IP hero[ine]')
