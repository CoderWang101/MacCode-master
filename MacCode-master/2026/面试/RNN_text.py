import torch
import torch.nn as nn

class SimpleRNN(nn.Module):
    """
    一个简单的RNN模型,用于学习RNN的基本结构
    """

    def __init__(self, input_size, hidden_size, output_size, num_layers=1):
        super(SimpleRNN, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers

        # 定义RNN层
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, batch_first=True)

        # 定义输出层
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        # 初始化隐藏状态
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)

        # 前向传播RNN
        out, _ = self.rnn(x, h0)

        # 取最后一个时间步的输出
        out = self.fc(out[:, -1, :])

        return out


# 示例：创建一个简单的RNN模型
if __name__ == "__main__":
    # 参数设置
    input_size = 10  # 输入特征维度
    hidden_size = 20  # 隐藏层维度
    output_size = 1  # 输出维度
    seq_length = 5  # 序列长度
    batch_size = 3  # 批次大小

    # 创建模型
    model = SimpleRNN(input_size, hidden_size, output_size)

    # 创建随机输入数据 (batch_size, seq_length, input_size)
    inputs = torch.randn(batch_size, seq_length, input_size)

    # 前向传播
    outputs = model(inputs)

    print("模型输出形状:", outputs.shape)  # 应输出: torch.Size([3, 1])
    print("模型结构:\n", model)
