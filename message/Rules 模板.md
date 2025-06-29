以下是为 Python 开发者 量身定制的现成 AI 协作 Rules 模板，包含可直接复用的代码示例和配置文件：

***

### 📜 Python 专用 AI 协作 Rules（Markdown 格式）

```
<MARKDOWN>
```

````
# Python_AI_Rules.md## 🛠 **通用规则**1. **代码生成前必须确认**：   - [ ] Python 版本要求（如 >=3.8）   - [ ] 第三方依赖清单（非标准库需注明）2. **代码风格**：   ```python   # 示例：AI 生成代码必须符合以下要求   def calculate_average(numbers: list[float]) -> float:  # 必须有类型注解       """计算列表平均值，空列表返回 0.0"""               # Google 风格文档字符串       if not numbers:                                  # 防御性编程           return 0.0       return sum(numbers) / len(numbers)
````

3. 禁止出现：

   * 裸 except: 语句（必须指定异常类型）

   * 超过 2 层嵌套的循环/条件

   * 未处理的 None 返回值

## 🧪 测试规范

```
<PYTHON>
```

```
# 测试用例生成规则（AI 需为每个函数生成）@pytest.mark.parametrize(    "input_data, expected",    [        ([1, 2, 3], 2.0),      # 正常用例        ([], 0.0),             # 边界用例        (["a"], TypeError),    # 异常用例    ])def test_calculate_average(input_data, expected):    # AI 应自动生成测试逻辑...
```

***

### ⚙️ 可执行配置文件（JSON 格式）

```
<JSON>
```

```
// .pythonairules.json{  "style": {    "type_hints": "required",    "docstring_format": "google",    "max_function_length": 30  },  "security": {    "check_input_type": true,    "ban_unsafe_libs": ["pickle", "eval"]  },  "ai": {    "pre_prompt": "首先生成实现思路，包含时间复杂度分析",    "post_prompt": "输出改进建议（如用 NumPy 加速）"  }}
```

***

### 🔍 常见场景 Rules 速查

#### 1. 数据分析脚本

```
<PYTHON>
```

```
# AI 生成规则：- 必须包含 Pandas 链式方法注释（例：`.query() → # 筛选条件: x>0`）- 禁止直接修改输入 DataFrame（需 .copy()）- 内存占用超过 100MB 时给出警告
```

#### 2. Web 开发（FastAPI/Django）

```
<PYTHON>
```

```
# AI 生成规则：- 路由函数必须包含 OpenAPI 文档- 数据库操作必须用 async/await 标记- 密码字段需自动过滤日志输出
```

#### 3. 深度学习（PyTorch）

```
<PYTHON>
```

```
# AI 生成规则：- 张量形状变化需用注释标注（如 # [B, C, H, W] → [B, H*W, C]）- 模型训练代码必须包含随机种子设置- 显存超 80% 时提示优化建议
```

***

### 📌 使用技巧

1. 在 Cursor 中植入规则：

   ```
   <PYTHON>
   ```

   ```
   # 在项目根目录创建 .cursor/ai_rules.pydef pre_codegen():    """强制 AI 生成前检查"""    print("❗ 请确认：是否已处理 None 输入？")def post_codegen(code: str):    """生成后自动检查"""    if "except:" in code:        raise ValueError("禁止使用裸 except!")
   ```

2. 快速检验工具指令：

   ```
   <BASH>
   ```

   ```
   # 用以下命令验证 AI 生成的代码pylint --disable=all --enable=typecheck,invalid-name $filemypy --strict $file
   ```

***

### 🎯 示例完整流程

用户提问：
"用 Python 写一个从 API 获取天气数据的脚本"

AI 响应规则：

1. 先输出设计：

   ```
   <PYTHON>
   ```

   ```
   # 1. 设计确认- 使用 requests 库（需安装）- 请求超时设置为 10s- 处理 HTTP 404/500 错误
   ```

2. 按规则生成代码：

   ```
   <PYTHON>
   ```

   ```
   def get_weather(api_url: str) -> dict:    """获取天气数据（自动重试 1 次）"""    try:        response = requests.get(api_url, timeout=10)        response.raise_for_status()        return response.json()    except requests.RequestException as e:        # 错误处理逻辑...
   ```

以下是为 Python 不同领域 定制的 AI 协作 Rules 模板，包含可直接复用的代码示例和配置文件：

***

### 🕷️ 1. 爬虫领域专用 Rules

#### 📜 核心规则（保存为 spider\_rules.md）

```
<MARKDOWN>
```

````
# Python_Spider_Rules.md## 🚦 强制性约束- **请求限制**：  ```python  # 必须包含以下参数  requests.get(      url,      headers={"User-Agent": "Mozilla/5.0"},  # 必须伪装浏览器      timeout=10,                             # 超时设置      proxies={"http": "socks5://127.0.0.1:1080"}  # 需要时代理配置  )
````

* 异常处理：

  ```
  <PYTHON>
  ```

  ```
  # 必须处理以下异常try:    response = requests.get(url)except (requests.Timeout, requests.ConnectionError) as e:    logger.error(f"Request failed: {e}")  # 必须记录日志    raise SystemExit(1)                   # 严重错误立即
  ```

## ⚠️ 反反爬策略

```
<PYTHON>
```

```
# AI 生成代码时必须声明反爬措施def anti_anti_spider():    """必须包含以下至少一项"""    - 随机延迟（2~5秒）    - 动态 Cookie 管理    - 验证码识别模块标注  # 如使用 ddddocr 需特别注明
```

***

### 🤖 2. 自动化测试专用 Rules

#### ⚙️ 配置文件（保存为 .pytestairules.json）

```
<JSON>
```

```
{  "generation_rules": {    "fixtures": {      "required": true,      "template": "@pytest.fixture(scope='module')\ndef {name}():\n    \"\"\"{docstring}\"\"\""    },    "parametrize": {      "min_cases": 3,      "require_edge_cases": true    }  },  "forbidden": [    "time.sleep()",  # 必须用 pytest-timeout 替代    "print()"        # 必须用 logging 或 capfd  ]}
```

#### 📝 示例代码规则

```
<PYTHON>
```

```
# AI 生成测试代码时必须遵守：class TestLogin:    """测试登录功能"""        # 必须包含以下测试维度    def test_success(self, auth_fixture):  # 1. 成功路径        assert response.status_code == 200            def test_wrong_password(self):         # 2. 错误路径        assert "Invalid password" in response.text            @pytest.mark.parametrize("input", [None, "", 123])  # 3. 异常输入    def test_invalid_input(self, input):        assert "Error" in response.json()
```

***

### 📊 3. 数据分析专用 Rules

#### 🧩 Jupyter Notebook 规则模板

```
<PYTHON>
```

````
# %% [markdown]# ## AI 生成 Notebook 必须包含：# 1. **数据校验单元格**：#    ```python#    assert not df.empty, "数据不能为空"#    assert df.duplicated().sum() == 0, "必须去重"#    ```# %% [code]# 2. **可视化规范**：def plot_distribution(data: pd.Series):    """必须包含的参数"""    plt.figure(figsize=(10, 6))            # 指定画布大小    plt.title("Distribution Plot")         # 必须含标题    sns.despine()                          # 美化图形
````

#### 🚫 禁止模式

```
<PYTHON>
```

```
# 以下模式会被拒绝df.drop_duplicates(inplace=True)  # 禁用 inplace 操作plt.show()                        # 必须使用返回值显示图形
```

***

### 🔧 4. 量化交易专用 Rules

#### ⚠️ 风控规则模板

```
<PYTHON>
```

```
# risk_control_rules.pyclass TradingRules:    """AI 生成策略代码必须继承此类"""        @property    def max_drawdown(self) -> float:  # 必须定义风控参数        return 0.2        def pre_execute(self):        """交易前必须检查"""        assert not self.is_holiday(), "节假日禁止交易"        assert self.current_position < 0.8, "超过仓位限制"
```

#### 📈 回测规范

```
<PYTHON>
```

```
def backtest_strategy():    """必须包含的指标"""    return {        "sharpe_ratio": ">=1.5",    # 夏普比率要求        "max_drawdown": "<25%",     # 最大回撤限制        "trade_count": ">30"        # 最小交易次数    }
```

***

### 🛠️ 5. 运维自动化专用 Rules

#### 🐧 Linux 运维脚本规则

```
<BASH>
```

```
#!/bin/bash# AI 生成运维脚本必须包含：set -euo pipefail  # 必须启用严格模式trap "echo 'ERROR at line $LINENO'" ERR  # 错误追踪# 敏感操作需确认if [[ $DELETE_FLAG == true ]]; then    read -p "确认删除？(yes/no)" confirm    [[ $confirm == "yes" ]] || exit 1fi
```

#### ☸️ K8s 运维规则

```
<YAML>
```

> ```
> # k8s_rules.yamlapiVersion: apps/v1kind: Deploymentmetadata:  annotations:    ai-generation-constraints:  # AI 必须添加的约束      - "必须定义 resource limits"      - "必须配置 readinessProbe"spec:  template:    spec:      containers:      - resources:          limits:            cpu: "2"  # 必须设置上限
> ```

***

### 🎯 快速使用方法

1. 将对应领域的规则保存为项目文件（如 .spider\_rules.md）

2. 在 Cursor 中通过指令调用：

   ```
   <PYTHON>
   ```

   ```
   # 在代码顶部添加规则声明# @rules: .spider_rules.md# @env: requests>=2.28.2
   ```
