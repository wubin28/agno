# 🚀 Quick Start - DeepSeek Version

这是一个使用DeepSeek模型的Agno Demo快速启动指南。

## 🎯 推荐方式：交互式启动（无需保存密钥）

**最简单、最安全的方式！** 直接运行，程序会询问你的API密钥：

```bash
# 激活虚拟环境（如果还没有激活）
source .demoenv/bin/activate

# 直接启动 - 会提示你输入API密钥
python run.py
```

运行后会看到：
```
============================================================
AgentOS API Key Configuration
============================================================

⚠️  DEEPSEEK_API_KEY not found in environment
Please enter your DeepSeek API key:
(Get one at: https://platform.deepseek.com/)
DeepSeek API Key (hidden): ************  # 输入时显示为星号
✓ DeepSeek API key set for this session
============================================================
```

**优点：**
- ✅ API密钥不会保存到文件
- ✅ 输入时显示为星号，保护隐私
- ✅ 只在当前运行会话有效
- ✅ 最安全的方式

## 方式2：使用环境变量（持久化）

如果你想避免每次输入，可以设置环境变量：

```bash
# 设置DeepSeek API密钥
export DEEPSEEK_API_KEY="your-api-key-here"

# 启动AgentOS
python run.py
```

如果环境变量已设置，程序会自动检测并使用，不会再询问。

## 方式3：使用自动化脚本

```bash
# 运行设置脚本（会保存到 .bashrc 或 .zshrc）
./setup_deepseek.sh

# 启动AgentOS
python run.py
```

## 获取DeepSeek API密钥

1. 访问 https://platform.deepseek.com/
2. 注册并登录
3. 在API设置中创建新的API密钥
4. 复制密钥并按上述方式设置

## 访问Web界面

启动成功后，访问：
- 本地: http://localhost:7777
- 在线: https://os.agno.com/ (连接到本地AgentOS)

## 已修改的Agent

所有Agent都已从Claude模型切换到DeepSeek模型：

✅ Agno Knowledge Agent - 知识库问答
✅ Agno MCP Agent - MCP工具支持
✅ YouTube Agent - 视频内容分析
✅ Memory Manager - 记忆管理
✅ Finance Agent - 金融数据分析
✅ Finance Team - 金融团队协作
✅ Research Agent - 研究助手
✅ Competitive Brief - 竞品分析
✅ Simple Agent - 简单示例

## 常见问题

### Q: 为什么要切换到DeepSeek？
A: 在中国大陆，Claude API可能无法访问（403错误）。DeepSeek是一个很好的替代方案，提供强大的中英文支持和推理能力。

### Q: DeepSeek和Claude性能对比如何？
A: DeepSeek在中文理解和推理任务上表现出色，且价格更实惠。对于大多数Agent任务，两者性能相当。

### Q: 我可以同时使用两个模型吗？
A: 可以！你可以为不同的Agent配置不同的模型。只需在创建Agent时指定不同的model参数。

### Q: 如何切换回Claude？
A: 查看 `DEEPSEEK_SETUP.md` 文件中的"Reverting to Claude"部分。

## 技术支持

- DeepSeek文档: https://platform.deepseek.com/docs
- Agno文档: https://docs.agno.com/
- 问题反馈: GitHub Issues

## 进阶配置

### 使用DeepSeek Reasoner模型

如果你需要更强的推理能力，可以修改agent配置：

```python
from agno.models.deepseek import DeepSeek

agent = Agent(
    model=DeepSeek(id="deepseek-reasoner"),  # 使用推理模型
    # ... 其他配置
)
```

### 自定义模型参数

```python
agent = Agent(
    model=DeepSeek(
        id="deepseek-chat",
        temperature=0.7,
        max_tokens=2048,
    ),
    # ... 其他配置
)
```

## 下一步

1. 在Web界面测试各个Agent
2. 尝试"What is the AgentOS?"提示词
3. 探索finance、research等其他Agent
4. 根据需要自定义Agent配置

祝你使用愉快！🎉

