quick sorting
============
我沒有使用遞迴來寫quick sorting，我的作法是用一開始的array來進行quick sorting 的所有步驟，標記已經選過的數字，
再用另一個一樣長的array來記已經選過的數字，以免它們被重複選到。
就結果而言，多出了相當多的步驟......
 
基本變數介紹

 *original_array:
  我把要用來排序的array稱為original_array，它會記下每次改動後的結果

 *recording_array=np.copy(original_array):
 recording_array專門用來記錄選過了哪些數字，對應'被選過數字的最終位置'的那一格會是-1，這個array長度固定


 *operation_array=np.copy(original_array):
  這是代表'當前進行排列'的子序列，長度會改變，最大當然就是一開始的長度

 *start和end:
  這是代表現在正在排序的operation_array是在original_array的第幾項(起訖點)，一開始start=0，end=operation_array的長度-1

 *quick_sort_one_step:在目前考慮的operation_array中，將目前選取的數字排到它應該在的位置，因為quick  sorting的特性，這就會是它的最終位置
 
步驟介紹

 0.先產生一個數字在1到200之間的original_array，畫一開始的圖形

 1.基本的想法是，一開始先選取original_array的最後一項，此時operation_array=original_array，畫圖

 2.使用quick_sort_one_step對最後一項作排序

 3.在2.中每一次的置換完畢後，都用新的operation_array來改寫原來的original_array，並畫圖，用operation_array的每一項的位置在加上此時的start  的值就可以正確的取代

 4.結束2.後在recording_array之中，被選數字的最終相對位置上(看它最後是在第幾項)標記-1(以免被選到)，畫圖
 
 5.接著按照新的recording_array，從 左邊開始，選出新的合適的start和end

 6.在新的original_array上，由新的start和end產生新的operation_array

 7.三個array都更新完畢，重覆2.直到operation_array長度為0，畫最終圖形

 *此時的original_array即為排序完成的數列


函數介紹
------------
 0.對應步驟0，用randit(1,200,10)產生original_array
 
 1.quick_sort_one_step(original_array,operation_array,recording_array,start,end):
   這是對應步驟1.到4.的函數，還包含了畫出圖形的部分
   
   一開始當然是:
   
     array_length=len(operation_array)
          last_term=array_length-1
          first_term=0
          choosen_number=operation_array[last_term]
 
   接著是畫出圖形的部分:
   將已選過(-1)的畫成紅色，正在排(start、end在對應範圍畫成黃色)，剩下其他待排的數列畫成藍色:
   
     colors=[]
     N=np.zeros(len(original_array))
     for n in range(len(original_array)):
         N[n]=n
     for set_colors in range(len(original_array)):
         if recording_array[set_colors]==-1:
             colors.append('r')   
         elif start<=set_colors and end>=set_colors:
             colors.append('y')
         else:
             colors.append('b')
   綠色的部分要在每一個步驟中畫，所以不會放在這裡
   
   接著是步驟1.2.3.:
       for j in range(array_length):       
            if j+first_term>=last_term:
                clf()
                colors[start+last_term]='g'
                plt.bar(N,original_array,width=0.3,color=colors)
                plt.show()
                plt.pause(0.5)
                break 
            elif operation_array[j+first_term]>choosen_number:
                Constant=operation_array[j+first_term]
                operation_array[j+first_term]=operation_array[last_term-1]
                operation_array[last_term-1]=operation_array[last_term]
                operation_array[last_term]=Constant
                colors[start+last_term]='g'
                last_term=last_term-1
                first_term=first_term-1
                clf()   
                plt.bar(N,original_array,width=0.3,color=colors)
                colors[start+last_term+1]='y'
                plt.show()
                plt.pause(1)
                for p in range(array_length):
                    original_array[start+p]=operation_array[p]
   
 2.quick_sort(original_array):
   這是主函數
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
