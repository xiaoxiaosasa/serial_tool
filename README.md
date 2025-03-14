# sensor_server_fastapi

## 【功能描述】

serial control tool  
串口控制工具 控制继电器电路开关

## 【程序类型】

- PROGRAM_TYPE= GUI developed by python3.10 pyside6

## 【使用】

- 安装依赖:

  - pip install -r requirements.txt

- 打包

  - pyinstaller --windowed --onefile --icon=app.ico main.py

- 启动
  - python main.py
  - dist 下 exe 文件

## 【设计说明】

- 采用.\venv\Lib\site-packages\PySide6\designer.exe 设计 ui 页面
- 保存 ui 为 mainwindow.ui 文件
- pyside6-uic.exe .\mainwindow.ui -o ui_mainwindow.py 将 ui 文件打成 py 文件
- 代码中加载使用按钮等元素

### 项目结构

### 环境变量

- 虚拟环境
  - python -m venv venv
