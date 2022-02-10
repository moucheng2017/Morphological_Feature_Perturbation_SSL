import torch
# import sys
# sys.path.append("..")
# from Train import trainModels
from Train_Stream_FixMatch import trainModels
# torch.manual_seed(0)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False


if __name__ == '__main__':

    for i in range(10):

        slice = 100

        fold_current = 'dense_' + str(i) + '_r176_s' + str(slice)

        trainModels(data_directory='/home/moucheng/projects_data/Pulmonary_data/',
                    dataset_name='CARVE2014',
                    dataset_tag=fold_current,
                    cross_validation=True,
                    input_dim=1,
                    class_no=2,
                    repeat=1,
                    train_batchsize=1,
                    augmentation=True,
                    num_epochs=50,
                    learning_rate=2e-5,
                    alpha=0.002,
                    width=24,
                    log_tag='miccai',
                    consistency_loss='mse',
                    main_loss='dice',
                    self_addition=True,
                    save_all_segmentation=False,
                    annealing_mode='down',
                    annealing_threshold=0,
                    annealing_factor=0.5,
                    )