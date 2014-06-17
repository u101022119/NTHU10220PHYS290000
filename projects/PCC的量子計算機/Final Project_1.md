題目：觀察方程式的行為
-----------------
製作：楊尚融、林奕廷、梁洛威、王立民
-----------------
說明：
本程式可以讓使用者改變初始條件與方程式參數來觀察方程式的行為

●定義函數
把原先的二階ODE拆成兩個一階ODE
deriv_1 = x的一次微分
deriv_2 = X的二次微分
[ deriv_1 , deriv_2 ]
x = [ , ]
x[0]為x的值，x[1]為x的一次微分值

def deriv(x,t):
    deriv_1 = x[1]
    deriv_2 = epsilon*(1 - x[0]**2)*x[1] - x[0]
    return np.array([ deriv_1 , deriv_2 ])
	
●解ODE
t = np.linspace(0.0,50.0,10000) 
xinit = np.array([1.0,0.0])
x = odeint(deriv,xinit,t)

●畫出來
ax1 = plt.subplot2grid((90,160), (0,0), colspan=160 , rowspan=20)
plt.subplots_adjust(bottom=0.1)
l, = plt.plot(t,x[:,0])
plt.axis([0, 50, -5, 5])
plt.title('van der Pol oscillator')
plt.xlabel('t')
plt.ylabel('x')

●設定滑桿
axcolor = 'lightgoldenrodyellow'

axxinit  = plt.axes([0.2, 0.40, 0.20, 0.02], axisbg=axcolor)
axdx_dtinit  = plt.axes([0.2, 0.35, 0.20, 0.02], axisbg=axcolor)
axepsilon = plt.axes([0.2, 0.30, 0.20, 0.02], axisbg=axcolor)

sxinit = Slider(axxinit, 'x init', 0.1, 5.0, valinit=xinit[0])
sdx_dtinit = Slider(axdx_dtinit, 'dx_dt init', 0.1, 5.0, valinit=xinit[1])
sepsilon = Slider(axepsilon, 'epsilon', 0.1, 3.0, valinit=epsilon)

●重算數值的函數
def update(val):
    global epsilon,xinit 
    
    epsilon = sepsilon.val
    xinit[0] = sxinit.val
    xinit[1] = sdx_dtinit.val
    x = odeint(deriv,xinit,t)
    m.set_xdata(x[:,0])
    m.set_ydata(x[:,1])
    l.set_ydata(x[:,0])
    plt.draw()
	
●讓程式更新圖形的指令(去執行update函數)
sxinit.on_changed(update)
sdx_dtinit.on_changed(update)
sepsilon.on_changed(update)

●畫相圖
ax2 = plt.subplot2grid((90,160), (30,80), rowspan = 80,colspan = 80)
m, = plt.plot(x[:,0],x[:,1])
plt.axis([-6, 6, -6, 6])
plt.xlabel('x')
plt.ylabel('dx/dt')