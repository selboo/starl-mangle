 "+"以完成功能 


 + 1、charisma 框架修改
 + 1.1、添加更多 icon 图标 http://www.lovelucy.info/demo/twitter-bootstrap-custom-icons/
 + 1.2、首页 Widgets 
 
 + 2、用户管理
 + 3.1、用户显示
 + 2.2、用户编辑
 + 2.3、用户删除
  + 2.3.1、删除账号 弹出确认窗口
 + 2.4、用户 COOKIES 和 SESSIOS 认证
 + 2.5、限制IP登陆
  + 2.5.1、https://pypi.python.org/pypi/IPy/
 + 2.6、实现 状态功能
 + 2.7、密码 三次 MD5加密
 + 2.8、用户头像

 + 4、设备资产
 + 4.1、资产列表
  4.1.1、资产过期时间（自动更新）
 + 4.2、资产编辑
  4.2.1、资产历史记录
  4.2.2、资产历史对比
 + 4.3、资产删除

 + 5、交换机管理
 + 5.1、交换机列表
   5.2、交换机修改
   5.2、交换机 命令 
  + 5.2.1、绑定ARP
  + 5.2.2、端口绑定
  + 5.2.3、获取防火墙 带宽 数据包 和 ping 并出图
    http://www.ichartjs.com/ 绘图工具
    备选 图标库 http://ecomfe.github.io/echarts/
    5.2.4、显示交换机 端口实时状态
    5.2.5、端口状态检查 检查某一端口 MAC地址，发送邮件

   6、服务器管理
   6.1、SSH 无密码链接 id_rsa.pub
   6.2、获取SVN 权限 添加SVN 发送邮件
 + 6.3、直接连接 SSH 模块
  + 6.3.1 Ajaxterm https://github.com/mattlaue/ajaxterm2 二次开发 
    GET方式 提交链接信息
    6.3.2 Ajaxterm 直接调用 id_rsa.pub 密钥免密码登陆
    
 + 7、邮件模块 setings 内
 + 7.1、邮件模块 mail_send('收件人', '主题', '内容')

   8、webvirtmgr KVM 整合
   8.1、https://github.com/retspen/webvirtmgr

    + 9、C/S 架构 获取数据执行命令
  + 9.1、S
   + 9.1.1、监听 TCP 54321
   + 9.1.2、守护进程 daemon
   + 9.1.3、RSA 解密认证
   + 9.1.4、命令回显 BASE64 加密传输
   + 9.1.5、l_command 模块的命令，重新加载
   + 9.1.6、TCP MTU 分包发送，用于发送大内容数据
     + 9.2、C
   9.2.1、agent
   + 9.2.2、RSA 加密认证
   + 9.2.3、命令显示 BASE64 解密
   + 9.2.3、TCP MTU 分包接受

 + 10、站点设置
 + 10.1、系统参数设置
 + 10.2、开放注册设置
 + 10.3、Session API 查询

   11、监控模块
   11.1、获取指定服务器 CPU 内存 硬盘等信息
   
   12、报警模板
   12.1、设置相应阀值，和监控数值对比进行报警
   
   13、计划任务模块
   13.1、通过 crontab 设置监控频率 [*/1,*/3,*/5,*/10,*/15,*/30,*/60] * * * * python crontab.py

 PS: 借鉴平台
 OSA开源运维监控管理平台：http://www.osapub.com/
 TriAquae批量部署管理工具：http://triaquae2.sinaapp.com/

 绘图工具：http://www.ichartjs.com/ 绘图工具
 绘图工具：http://ecomfe.github.io/echarts/

 SSH ,Ajaxterm Fabric http://www.serfish.com/console/ paramiko.SSHClient()
 
 使用 noVNC 开发 Web 虚拟机控制台 http://www.vpsee.com/2013/07/integrating-novnc-with-our-vm-control-panel/
 
 Bootstrap 模板    http://wrapbootstrap.com/
     http://wrapbootstrap.com/preview/WB0JLR295