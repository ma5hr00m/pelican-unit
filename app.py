import func.winEvents
import tkinter


root = tkinter.Tk()               # 创建窗口
root.resizable( False, False )      # 横纵不允许缩放
root.geometry( "400x400-0-0" )   # 窗口的长宽、定位设置
root.configure( bg = "#333333" )      # 设置窗口背景色

testBtn = tkinter.Button( text="Close",command= lambda: root.destroy() )
testBtn.pack()

root.mainloop()