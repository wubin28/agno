# 🧪 Testing Instructions

## 测试新的交互式API Key输入功能

### 准备工作

1. **确保虚拟环境已激活**
   ```bash
   source .demoenv/bin/activate
   ```

2. **清除任何现有的环境变量（用于测试）**
   ```bash
   unset DEEPSEEK_API_KEY
   unset OPENAI_API_KEY
   ```

### 测试步骤

#### 测试 1: 基本交互式输入

```bash
python run.py
```

**预期行为：**
1. 程序启动
2. 显示配置提示：
   ```
   ============================================================
   AgentOS API Key Configuration
   ============================================================
   
   ⚠️  DEEPSEEK_API_KEY not found in environment
   Please enter your DeepSeek API key:
   (Get one at: https://platform.deepseek.com/)
   DeepSeek API Key (hidden): 
   ```
3. 输入你的DeepSeek API key（**输入时会显示为不可见或星号**）
4. 按Enter后看到：`✓ DeepSeek API key set for this session`
5. 询问OpenAI API key（可选），输入 `n` 跳过
6. AgentOS正常启动

#### 测试 2: 使用环境变量（跳过提示）

```bash
export DEEPSEEK_API_KEY="your-key-here"
python run.py
```

**预期行为：**
1. 程序启动
2. 显示：`✓ DEEPSEEK_API_KEY found`
3. 直接启动，不会询问API key

#### 测试 3: 空输入处理

```bash
unset DEEPSEEK_API_KEY
python run.py
# 当提示输入时，直接按Enter（不输入任何内容）
```

**预期行为：**
1. 显示错误：`❌ Error: API key cannot be empty`
2. 程序退出（exit code 1）

#### 测试 4: Ctrl+C 取消

```bash
unset DEEPSEEK_API_KEY
python run.py
# 当提示输入时，按 Ctrl+C
```

**预期行为：**
1. 显示：`❌ Setup cancelled by user`
2. 程序优雅退出

### 功能验证

启动成功后：

1. **访问Web界面**
   - 打开浏览器访问 http://localhost:7777
   - 或访问 https://os.agno.com/ 并连接到本地AgentOS

2. **测试 Agno Knowledge Agent**
   - 在界面中选择 "Agno Knowledge Agent"
   - 发送消息：`What is the AgentOS?`
   - **验证：** 
     - ✅ 应该收到正常响应（关于AgentOS的解释）
     - ❌ 不应该出现 403 错误
     - ❌ 不应该出现 "DEEPSEEK_API_KEY not set" 错误

3. **测试其他Agent**
   - Finance Agent: `Analyze AAPL stock`
   - Research Agent: `Research latest AI trends`
   - YouTube Agent: 提供一个YouTube URL

### 安全性验证

✅ **API Key 输入时的保密性**
- 使用 `getpass.getpass()` 函数
- 输入时不会在终端显示（或显示为 `*****`）
- API key只存储在当前进程的环境变量中
- 程序关闭后API key不会保留

✅ **不保存到文件**
- API key不会写入任何配置文件
- 不会写入 .env 文件
- 不会写入 shell 配置文件（除非用户使用 setup_deepseek.sh 脚本）

### 常见问题排查

#### 问题 1: 输入的API key仍然可见

**原因：** 某些终端或IDE可能不支持 `getpass` 的隐藏输入

**解决方案：**
- 在真实的终端中运行（不要在某些IDE的集成终端中）
- 或者使用环境变量方式：`export DEEPSEEK_API_KEY="your-key"`

#### 问题 2: 仍然报错 "DEEPSEEK_API_KEY not set"

**排查步骤：**
1. 确认你在提示时输入了API key
2. 确认按了Enter确认
3. 查看是否有 `✓ DeepSeek API key set for this session` 的确认信息
4. 验证API key是否有效（登录 https://platform.deepseek.com/ 检查）

#### 问题 3: OpenAI API key 警告

**说明：** Knowledge base 使用 OpenAI embeddings

**选项：**
- 输入 `y` 并提供 OpenAI API key（推荐，用于完整功能）
- 输入 `n` 跳过（某些知识库功能可能不可用）

### 性能验证

1. **响应时间**
   - DeepSeek API 应该在合理时间内响应（通常 1-3 秒）
   - 如果超时，检查网络连接

2. **流式输出**
   - 响应应该是流式的（逐字显示）
   - 不应该等待全部内容生成后才显示

### 成功标准

✅ 所有测试通过
✅ API key 输入时不可见
✅ Agent 正常响应，无 403 错误
✅ 程序关闭后 API key 不保留
✅ Web 界面正常工作

### 如果测试失败

1. 检查 DeepSeek API key 是否有效
2. 检查网络连接（确保可以访问 api.deepseek.com）
3. 查看终端完整错误信息
4. 参考 `QUICKSTART_DEEPSEEK.md` 和 `DEEPSEEK_SETUP.md`

## 下一步

测试成功后，你可以：
1. 尝试不同的 Agent
2. 测试 Team 和 Workflow
3. 根据需要自定义 Agent 配置
4. 探索 AgentOS 的更多功能

---

**测试完成时间：** ___________

**测试结果：** ⬜ 通过  ⬜ 失败

**备注：** ___________________________________

