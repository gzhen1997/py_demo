# FastAPI Hello 示例项目

这是一个使用 FastAPI 搭建的简单 Hello 接口示例项目。

## 项目结构

```
py_demo/
├── main.py            # FastAPI 应用主文件
├── requirements.txt   # Python 依赖列表
└── venv/              # 虚拟环境目录
```

## 环境要求

- Python 3.8+

## 快速开始

### 1. 创建虚拟环境（如果还未创建）

```bash
python -m venv venv
```

### 2. 激活虚拟环境

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 启动服务

```bash
uvicorn main:app --reload
```

服务启动后，访问以下地址：

- API 首页: http://127.0.0.1:8000/
- Swagger 文档: http://127.0.0.1:8000/docs
- ReDoc 文档: http://127.0.0.1:8000/redoc

## 接口说明

### 1. Hello World

**GET** `/`

返回示例：
```json
{
  "message": "Hello World"
}
```

### 2. 自定义 Hello

**GET** `/hello/{name}`

路径参数：
- `name`: 你的名字

返回示例（访问 `/hello/Alice`）：
```json
{
  "message": "Hello, Alice!"
}
```
