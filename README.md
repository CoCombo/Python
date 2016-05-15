# Pygame
Learn pygame just for fun.

#Linux
sudo get-apt install python-pygame.

#Python
list.extend([...])#一次添加多个元素到列表  
字符串，元组不支持原处修改。元组没有append(),sort(),pop()方法  
~按位翻转x -> -(x+1)  
查看包的更多使用方法：help(modulename)，查看文档：print modulename.__doc__  

#python2和python3切换  
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 100  
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 150  
切换回python2  
sudo update-alternatives --config python  

#yield  
简单地讲，yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。)  
