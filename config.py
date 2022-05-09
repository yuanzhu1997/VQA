# paths
qa_path = '../image_dataset_abs/vqa'  # directory containing the question and annotation jsons
train_path = '../image_dataset_abs/train2015'  # directory of training images
val_path = '../image_dataset_abs/val2015'  # directory of validation images
test_path = '../image_dataset_abs/test2015'  # directory of test images
preprocessed_path = '../image_dataset_abs/featuremaps/resnet-14x14-2-large.h5'  # path where preprocessed features are saved to and loaded from
vocabulary_path = '../image_dataset_abs/featuremaps/vocab.json'  # path where the used vocabularies for question and answers are saved to

task = 'OpenEnded'
dataset = 'abstract_v002'

# preprocess config
preprocess_batch_size = 32
image_size = 448  # scale shorter end of image to this size and centre crop
output_size = image_size // 32  # size of the feature maps after processing through a network
output_features = 512 #2048  # number of feature maps thereof
padding_size = 168 # 0 padding along the height
central_fraction = 1 # 0.875  # only take this much of the centre when scaling and centre cropping
#max_image = 10000
max_image_train = 20000 # 10000
max_image_val   = 10000 # 2000

# training config
epochs = 20
batch_size = 64
initial_lr = 1e-3  # 1e-3 # default Adam lr
lr_halflife = 50000  # 50000 #in iterations
data_workers = 2
max_answers = 3000
