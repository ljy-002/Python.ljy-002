import wandb


# 1) 开始WB运行
wandb.init(config=tf.flags.FLAGS, sync_tensorboard=True)

# 2) 保存模型输入和超参数
config = wandb.config
config.learning_rate = 0.01

# 3) 随时间记录指标以可视化性能
wandb.log({"loss": loss})

