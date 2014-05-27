# -*- coding: utf-8 -*-
"""
Created on Tue May 13 18:07:43 2014

@author: larry lu
"""

class card_sprite(Sprite):  
    is_event_handler=True;  
    def __init__(self,image):  
        super(card_sprite,self).__init__(image);  
        self.is_mouse=False;  
        self.is_end=False;  
    def on_enter(self):  
        super(card_sprite,self).on_enter();  
        director.window.push_handlers(self.on_mouse_press);  
    def on_exit(self):  
        director.window.pop_handlers();  
        super(card_sprite,self).on_exit();  
  
    def on_mouse_press(self,x,y,buttons,modifiers):  
        if self.is_mouse==True:  
            if buttons== 1 and x>(self.x-self.width/2) and x<=(self.x-self.width/2+20) and y>=(self.y-self.height/2) and y<=(self.y +self.height/2):  
                print "click!!!!11";  
                return;  
        if self.is_end==True:  
            if buttons== 1 and x>(self.x-self.width/2) and x<=(self.x-self.width/2+90) and y>=(self.y-self.height/2) and y<=(self.y +self.height/2):  
                print 'is end click()';  
                return ;  