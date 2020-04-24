# Monitoring-directory-demo
花了一小会时间写的目录监控样本/  Took a little time to write a monitoring directory demo
使用python写的一个目录监控程序
通过pyinotify实现，将被修改的文件copy到另一个文件夹储存并以时间戳区分
基于linux系统
目前只能监控的类似echo这种修改，因为是很短时间写完的。。所以没有清除vim等软件造成的临时文件的影响

need:
python3

install:
pip3 install -r requerment.txt

usage：
motify.py /xxx/ (xxx为你要监控的路径)

todo-list：
根据参数创建监控器
排除掉vim等造成的临时文件的影响
