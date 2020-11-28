## UI自动化测试框架
###### 项目框架
selenium + pytest + allure
###### 环境依赖
   - selenium              3.141.0 
   - PyYAML                5.1.2
   - pytest                5.2.2
   - allure-pytest         2.8.6
###### 支持浏览器
Chrome  FireFox  Edge  Ie  ChromeOptions
###### 浏览器驱动下载
[下载地址](https://www.cnblogs.com/XhyTechnologyShare/p/13830293.html)
###### 项目运行
执行main目录下的main.py文件;
运行原理：通过调用pytest命令运行,pytest将会自动检索该项目的测试用例文件并执行,所以编写测试用例文件时一定要按照规则编写。
###### 测试用例文件编写规则
- 模块命名必须以test开头
- 类命名必须以Test开头 
###### 项目结构
````
├─case  测试用例层
│      conftest.py              pytest默认扫描文件        
│      test_RegisterCase.py     
│      __init__.py
│      
├─config
│      config_box.py            核心基类文件
│      CsvOperation.py          操作Csv文件
│      IniOperation.py          操作Ini文件
│      LogOperation.py          操作日志
│      UtilsOperation.py        工具类文件
│      YamlOperation.py         操作yaml文件
│      __init__.py
│      
├─main
│      main.py                  程序入口,启动文件
│      __init__.py
│      
├─page  页面元素层
│      RegisterPage.py          
│      __init__.py
│      
├─resources 资源文件夹
│  ├─conf   存放配置文件
│  │      config.ini
│  │      
│  └─elementSource  存放页面定位元素文件
│          register.yaml
│          
├─result    结果文件夹
│  ├─log    存放日志文件
│  │      log.log
│  │      
│  ├─report 存放测试报告文件
│  │      1653913e-6816-42af-b9dd-c92c88160cfd-container.json
│  │      333b0432-a625-4412-b5ab-bfa5bd4787c1-container.json
│  │      3b37aa23-7212-47e7-9df7-f34f5efd5947-attachment.png
│  │      44d82816-fe1b-437e-af88-24604df4653d-attachment.txt
│  │      68ca2441-d427-489b-98d4-d15d009ca6aa-attachment.txt
│  │      9928720f-46b9-4b7f-848a-348f2fa1e262-result.json
│  │      ee73af15-58be-411b-917e-078664606749-container.json
│  │      fc515436-3388-4e17-92df-e67d601fd3b1-container.json
│  │      
│  └─screenshot 存放截图文件
│          2020-11-28-15-20-43.png
│          
└─service   业务流程层
        RegisterService.py
        __init__.py  
`````
###### demo说明
项目中带的demo为本地项目,无法在外网执行
###### 版本说明
当前版本：v1.0
###### 后续版本
后续会更新一些demo上来,不会更新版本;框架结构变动时才会更新版本