import string

width = 200
height = 31
label_len = 16

characters = '0123456789'+string.ascii_lowercase+'-'
label_classes = len(characters)+1

# for batch_generator
lexicon_dic_path = 'mnt/ramdisk/max/90kDICT32px/lexicon.txt'
file_list = open('mnt/ramdisk/max/90kDICT32px/annotation_train.txt', 'r')
file_list_val = open('mnt/ramdisk/max/90kDICT32px/annotation_val.txt', 'r')
img_folder = 'mnt/ramdisk/max/90kDICT32px/'


# for CRNN_with_STN
learning_rate = 0.0001  # learning rate, 0.002 for default
cp_save_path = 'weights_best_STN.{epoch:02d}-{loss:.2f}.hdf5' \
    # save checkpoint path
base_model_path = 'weights_for_predict_STN.hdf5'  \
    # the model for predicting
tb_log_dir = 'paper_log'  # TensorBoard save path, Optional
load_model_path = ''  \
    # if you want to train a new model, please set  load_model_path = ""

