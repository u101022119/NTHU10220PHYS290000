Color Sorting Game
============

這是一個遊戲讓玩家根據程式所給的參考圖畫，去嘗試排列相近的顏色

>遊戲說明:
>先在遊戲選單裡面選擇難度
>進到遊戲畫面後，右邊會呈現遊戲希望玩家完成的答案
>玩家根據右邊的答案，用滑鼠點擊任兩個方格讓它交換
>當玩家認為完成之後點擊finish鍵後系統會計算玩家的完成程度
>給予相對應的分數，分數越低代表完成度越高

遊戲畫面分成兩個部分

  * 遊戲選單
  * 遊戲畫面

遊戲選單內包含五種難度給玩家選擇,難度的不同因方格色碼的變化量而不同
 1. easy, 以25為單位做變化
 2. normal, 以10為單位做變化
 3. hard, 以5為單位做變化
 4. crazy, 以3為單位做變化
 5. WTH, 以1為單位做變化

難度的不同以list的形式把100個方格應該擁有的顏色存在程式碼裡面的這個部分

~~~

#gamemode
easy=range(0,250,25)
normal=range(100,200,10)
hard=range(150,200,5)
crazy=range(150,180,3)
WTH=range(150,160,1)

~~~

函數定義
-----
這邊稍微介紹一下程式中所定義的函數

####1.這是產生100個方格的函數##

~~~
def BLOCKARRAYDETAIL(s,t):
    u=[]
    x=0
    y=0
    while x <10:
        while y <10:
            BLOCK=Rectangle(x,y)
            BLOCK.color(t)
            r=[BLOCK.x,BLOCK.y,BLOCK.red,BLOCK.green]
            v=[BLOCK.red,BLOCK.green]
            if v in u:
                y+=0
            else:
                u.append(v)
                s.append(r)
                y+=1
        y=0
        x+=1
    return s

~~~

####2.產生對應答案的函數###

~~~
def ANSWER(t):
    s=[]
    for i in range(10):
        for j in range(10):
            box=Block()
            box.x=900+i*40
            box.y=20+j*40
            box.color=BlockColor()
            box.color.red=t[i]
            box.color.green=t[j]
            r=[box.x,box.y,box.color.red,box.color.green]
            s.append(r)
    return s
~~~

####3.把方格畫到畫面上的函數###

~~~
def DRAWBLOCKARRAY(s):
    for i in range(10):
        for j in range(10):
            pygame.draw.rect(windowSurface,(s[i][j][2],s[i][j][3],0),(s[i][j][0],s[i][j][1],BLOCKSIZE,BLOCKSIZE)) 
~~~

####4.決定方格是否被點擊過的判斷函數##

~~~
def GenerateSelectedBoxData(val):
    SelectedBox=[]
    for i in range(10):
        SelectedBox.append([val]*10)
    return SelectedBox
~~~




for the menu, I create five buttons for the players to select.


Note that --- not considering the asterisk --- the actual text
content starts at 4-columns in.

> Block quotes are
> written like so.
>
> They can span multiple paragraphs,
> if you like.

Use 3 dashes for an em-dash. Use 2 dashes for ranges (ex. "it's all in
chapters 12--14"). Three dots ... will be converted to an ellipsis.



An h2 header
------------

Here's a numbered list:

 1. first item
 2. second item
 3. third item

Note again how the actual text starts at 4 columns in (4 characters
from the left side). Here's a code sample:

    # Let me re-iterate ...
    for i in 1 .. 10 { do-something(i) }

As you probably guessed, indented 4 spaces. By the way, instead of
indenting the block, you can use delimited blocks, if you like:

~~~
define foobar() {
    print "Welcome to flavor country!";
}
~~~

(which makes copying & pasting easier). You can optionally mark the
delimited block for Pandoc to syntax highlight it:

~~~python
import time
# Quick, count to ten!
for i in range(10):
    # (but not *too* quick)
    time.sleep(0.5)
    print i
~~~



### An h3 header ###

Now a nested list:

 1. First, get these ingredients:

      * carrots
      * celery
      * lentils

 2. Boil some water.

 3. Dump everything in the pot and follow
    this algorithm:

        find wooden spoon
        uncover pot
        stir
        cover pot
        balance wooden spoon precariously on pot handle
        wait 10 minutes
        goto first step (or shut off burner when done)

    Do not bump wooden spoon or it will fall.

Notice again how text always lines up on 4-space indents (including
that last line which continues item 3 above). Here's a link to [a
website](http://foo.bar). Here's a link to a [local
doc](local-doc.html). Here's a footnote [^1].

[^1]: Footnote text goes here.

Tables can look like this:

size  material      color
----  ------------  ------------
9     leather       brown
10    hemp canvas   natural
11    glass         transparent

Table: Shoes, their sizes, and what they're made of

(The above is the caption for the table.) Here's a definition list:

apples
  : Good for making applesauce.
oranges
  : Citrus!
tomatoes
  : There's no "e" in tomatoe.

Again, text is indented 4 spaces. (Alternately, put blank lines in
between each of the above definition list lines to spread things
out more.)

Inline math equations go in like so: $\omega = d\phi / dt$. Display
math should get its own line and be put in in double-dollarsigns:

$$I = \int \rho R^{2} dV$$

Done.
