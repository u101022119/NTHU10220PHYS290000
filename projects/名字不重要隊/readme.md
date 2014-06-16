BLACKJACK (introduction)
============
This game is about blackJack. It isn't a formal game. We design it as a easier game.  Therefore, you had better see the rule clearly before starting the game. 
Besides this code, there are other files you have to download.
First, go to https://drive.google.com/folderview?id=0B443UOKCSaXkT09DZk5fUHRSa3c&usp=sharing , and download the whole floder. Please remember not to change the name of the folder. Next, put the floder in the Partition D. ( D槽)
After finishing the above steps, you can start enjoying the game.


An h2 header
------------




PART B (adding card)
The most important part of adding card is how to avoid picking repeated cards.
So, we rearrange the order of the cards in the beginning (Add function) of the game. We set 'Y' to be the key to add cards. 'i+=50' and 'length += 1 ' is used to line up the cards. There will be 50-unit distance between each added card. The program will check if the total point held at that moment is larger than 21. If it does, When 'N' is pressed, the loop is break and show the following instruction. If not, we check if there is 'ACE' inside. To optimize the player's benefit, under the premise that the points will be closer but not more than 21, there will be additional 10 points. To achieve the goal, the former method will applied to the situation when the points are smaller than 12. 
After the plauer finish adding cards, it is computer's turn. We set the standard to be 16 points. When computer's points below the point, some cards will be added until the points are bigger than 16. Otherwise, that's all. When Ace is involved, the adjusting procedure will be the same as the method mentioned before. Then, we jumped to next section--comparison.
