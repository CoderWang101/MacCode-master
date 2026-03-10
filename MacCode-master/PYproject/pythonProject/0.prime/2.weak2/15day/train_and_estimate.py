import torch
import matplotlib.pyplot as plt
import matplotlib as mpl
import time
import os
mpl.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False
class Trainer:  # 定义 Trainer 类
    def __init__(self, model, train_loader, test_loader, criterion, optimizer, device, num_epochs=None, early_stopping=False, patience=3, min_delta=0.0, restore_best=True, early_stop_on='loss', save_model=False, save_every_epoch=False, save_path='checkpoint.pt'):  # 构造函数，接收模型、训练/测试数据加载器、损失函数、优化器和设备参数
        """
        初始化 Trainer 类
        
        参数:
            model: 待训练的模型
            train_loader: 训练数据加载器
            test_loader: 测试数据加载器
            criterion: 损失函数
            optimizer: 优化器
            device: 训练设备 (cpu 或 cuda)
            early_stop_on: 早停指标，'loss' 或 'acc'，默认 'loss'
            save_model: 是否保存模型，默认 False
            save_every_epoch: 是否每轮都保存模型，默认 False（仅保存最佳）
            save_path: 模型保存路径，默认 'checkpoint.pt'
        """
        # 保存传入的参数
        self.model = model  # 保存模型
        self.train_loader = train_loader  # 保存训练数据加载器
        self.test_loader = test_loader  # 保存测试数据加载器
        self.criterion = criterion  # 保存损失函数
        self.optimizer = optimizer  # 保存优化器
        self.device = device  # 保存设备信息
        self.num_epochs = num_epochs
        self.early_stopping = early_stopping
        self.patience = patience
        self.min_delta = min_delta
        self.restore_best = restore_best
        self.early_stop_on = early_stop_on  # 新增：早停指标选择
        self.save_model = save_model
        self.save_every_epoch = save_every_epoch
        self.save_path = save_path
        
        # 用于记录训练过程中的数据
        self.history = {  # 初始化历史记录字典
            'train_loss': [],  # 记录训练损失
            'train_acc': [],  # 记录训练准确率
            'test_loss': [],  # 记录测试损失
            'test_acc': []  # 记录测试准确率
        }

    def train(self, num_epochs=None):  # 训练方法，接收训练轮数
        """
        训练模型
        
        参数:
            num_epochs: 训练轮数
        """
        # 将模型移动到指定设备
        self.model.to(self.device)  # 将模型加载到指定设备
        
        # 记录训练开始时间
        start_time = time.time()  # 获取当前时间作为开始时间
        
        epochs_to_run = num_epochs if num_epochs is not None else (self.num_epochs if self.num_epochs is not None else 5)
        
        # 根据早停指标初始化最佳值
        if self.early_stop_on == 'acc':
            best_metric = -float('inf')
        else:  # 默认 'loss'
            best_metric = float('inf')
        
        best_state = None
        best_epoch = -1
        no_improve = 0
        
        # 遍历每个 epoch
        for epoch in range(epochs_to_run):  # 循环训练指定轮数
            # --- 训练阶段 ---
            self.model.train()  # 设置模型为训练模式
            running_loss = 0.0  # 累计损失
            correct = 0  # 预测正确的样本数
            total = 0  # 总样本数
            
            # 遍历训练数据
            for images, labels in self.train_loader:  # 从训练数据加载器中迭代获取图像和标签
                # 将数据移动到指定设备
                images, labels = images.to(self.device), labels.to(self.device)  # 将图像和标签加载到指定设备
                
                # 前向传播：计算模型输出
                outputs = self.model(images)  # 使用模型进行前向传播，得到输出
                loss = self.criterion(outputs, labels)  # 计算损失
                
                # 反向传播和优化
                self.optimizer.zero_grad()  # 清空梯度
                loss.backward()  # 反向传播计算梯度
                self.optimizer.step()  # 更新模型参数
                
                # 统计数据
                running_loss += loss.item() * images.size(0)  # 累计损失
                _, predicted = torch.max(outputs.data, 1)  # 获取预测类别
                total += labels.size(0)  # 累计样本数
                correct += (predicted == labels).sum().item()  # 累计正确预测数
            
            # 计算当前 epoch 的平均损失和准确率
            epoch_loss = running_loss / total  # 计算平均损失
            epoch_acc = correct / total  # 计算准确率
            
            # 保存训练指标
            self.history['train_loss'].append(epoch_loss)  # 保存训练损失
            self.history['train_acc'].append(epoch_acc)  # 保存训练准确率
            
            # --- 测试阶段 ---
            test_loss, test_acc = self._evaluate()  # 调用内部评估函数获取测试损失和准确率
            self.history['test_loss'].append(test_loss)  # 保存测试损失
            self.history['test_acc'].append(test_acc)  # 保存测试准确率
            
            # 打印每个 epoch 的结果
            print(f'Epoch [{epoch+1}/{epochs_to_run}] '  # 打印当前 epoch 编号
                  f'Train Loss: {epoch_loss:.4f} Acc: {epoch_acc:.4f} | '  # 打印训练损失和准确率
                  f'Test Loss: {test_loss:.4f} Acc: {test_acc:.4f}')  # 打印测试损失和准确率
            
            # 模型保存逻辑
            if self.save_model:
                if self.save_every_epoch:
                    # 每轮都保存
                    epoch_path = self.save_path.replace('.pt', f'_epoch{epoch+1}.pt')
                    torch.save(self.model.state_dict(), epoch_path)
                    print(f'模型已保存至 {epoch_path}')
                else:
                    # 仅保存最佳模型
                    save_best = False
                    if self.early_stop_on == 'acc':
                        if test_acc > best_metric + self.min_delta:
                            save_best = True
                    else:
                        if test_loss < best_metric - self.min_delta:
                            save_best = True
                    if save_best:
                        torch.save(self.model.state_dict(), self.save_path)
                        print(f'最佳模型已保存至 {self.save_path}')
            
            if self.early_stopping:
                if self.early_stop_on == 'acc':
                    # 以准确率作为早停指标
                    if test_acc > best_metric + self.min_delta:
                        best_metric = test_acc
                        best_state = {k: v.cpu().clone() for k, v in self.model.state_dict().items()}
                        best_epoch = epoch + 1
                        no_improve = 0
                    else:
                        no_improve += 1
                        if no_improve >= self.patience:
                            print(f'早停触发：连续 {self.patience} 轮未提升，最佳在第 {best_epoch} 轮，验证准确率 {best_metric:.4f}')
                            break
                else:
                    # 以损失作为早停指标（默认）
                    if test_loss < best_metric - self.min_delta:
                        best_metric = test_loss
                        best_state = {k: v.cpu().clone() for k, v in self.model.state_dict().items()}
                        best_epoch = epoch + 1
                        no_improve = 0
                    else:
                        no_improve += 1
                        if no_improve >= self.patience:
                            print(f'早停触发：连续 {self.patience} 轮未提升，最佳在第 {best_epoch} 轮，验证损失 {best_metric:.4f}')
                            break
        
        # 计算并打印总训练时间
        total_time = time.time() - start_time  # 计算总耗时
        print(f'Training finished in {total_time:.2f} seconds')  # 打印总训练时间
        if self.early_stopping and self.restore_best and best_state is not None:
            self.model.load_state_dict(best_state)
            if self.early_stop_on == 'acc':
                print('已恢复至最佳验证准确率的模型权重')
            else:
                print('已恢复至最佳验证损失的模型权重')
        return self.history  # 返回历史记录

    def _evaluate(self):  # 内部评估函数，用于在测试集上评估模型性能
        """内部评估函数，用于在测试集上评估模型性能"""
        self.model.eval()  # 设置模型为评估模式
        running_loss = 0.0  # 累计损失
        correct = 0  # 预测正确的样本数
        total = 0  # 总样本数
        
        # 禁用梯度计算，提高评估速度
        with torch.no_grad():  # 禁用梯度计算
            # 遍历测试数据
            for images, labels in self.test_loader:  # 从测试数据加载器中迭代获取图像和标签
                # 将数据移动到指定设备
                images, labels = images.to(self.device), labels.to(self.device)  # 将图像和标签加载到指定设备
                
                # 前向传播：计算模型输出
                outputs = self.model(images)  # 使用模型进行前向传播，得到输出
                loss = self.criterion(outputs, labels)  # 计算损失
                
                # 累计损失和准确率
                running_loss += loss.item() * images.size(0)  # 累计损失
                _, predicted = torch.max(outputs.data, 1)  # 获取预测类别
                total += labels.size(0)  # 累计样本数
                correct += (predicted == labels).sum().item()  # 累计正确预测数
        
        # 返回平均损失和准确率
        return running_loss / total, correct / total  # 返回平均损失和准确率

    def plot(self):  # 绘制训练过程中的损失和准确率曲线
        """绘制训练过程中的损失和准确率曲线"""
        # 生成 epoch 列表
        epochs = range(1, len(self.history['train_loss']) + 1)  # 生成 epoch 编号列表
        
        # 创建画布
        plt.figure(figsize=(12, 5))  # 创建新画布，设置大小
        
        # 绘制损失曲线
        plt.subplot(1, 2, 1)  # 创建第一个子图
        plt.plot(epochs, self.history['train_loss'], 'b-', label='Train Loss')  # 绘制训练损失曲线
        plt.plot(epochs, self.history['test_loss'], 'r-', label='Test Loss')  # 绘制测试损失曲线
        plt.title('Training and Test Loss')  # 设置子图标题
        plt.xlabel('Epochs')  # 设置 x 轴标签
        plt.ylabel('Loss')  # 设置 y 轴标签
        plt.legend()  # 显示图例
        plt.grid(True)  # 显示网格
        
        # 绘制准确率曲线
        plt.subplot(1, 2, 2)  # 创建第二个子图
        plt.plot(epochs, self.history['train_acc'], 'b-', label='Train Acc')  # 绘制训练准确率曲线
        plt.plot(epochs, self.history['test_acc'], 'r-', label='Test Acc')  # 绘制测试准确率曲线
        plt.title('Training and Test Accuracy')  # 设置子图标题
        plt.xlabel('Epochs')  # 设置 x 轴标签
        plt.ylabel('Accuracy')  # 设置 y 轴标签
        plt.legend()  # 显示图例
        plt.grid(True)  # 显示网格
        
        # 调整子图间距并显示
        plt.tight_layout()  # 调整子图间距
        plt.show()  # 显示图像
