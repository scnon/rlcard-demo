# rlcard-demo

## 四川麻将游戏规则

四川麻将游戏规则已经实现。它包括以下组件：
- 牌
- 游戏
- 环境
- 回合
- 玩家
- 庄家
- 裁判
- 工具

## 训练脚本

已添加四川麻将游戏的训练脚本。您可以使用它来训练您的模型。

## 新动作

游戏现在包括以下新动作：
- 碰 (Peng)
- 杠 (Gang)
- 胡 (Hu)

有关游戏规则的更多信息，请参阅 [四川麻将](https://zh.wikipedia.org/wiki/四川麻将)。

## 训练模型

要训练模型，请运行以下命令：

```bash
python train_sichuan_mahjong.py --train
```

## 保存训练模型

训练完成后，模型将自动保存到指定路径。您可以在 `train_sichuan_mahjong.py` 中设置保存路径。

## 加载训练模型并预测

要加载训练模型并根据手牌和牌桌信息预测出牌，请运行以下命令：

```bash
python train_sichuan_mahjong.py --predict
```
