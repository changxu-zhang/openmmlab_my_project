# TODO: in config file, add queue_length as arg

# TODO: modify mmdet3d/datasets/nuscenes_dataset.py in the way that bevformer does
class CustomNuScenesDataset(NuScenesDataset):
    '''
    introduce arg queue_length
    '''

    pass

# TODO: modify bevfusion.py

def obtain_history_bev(self, imgs_queue, pc_queue img_metas_list):
    '''
    just like in forward, difference is the input now is all except latest element, i.e. the last one in seq
    1. extract features from img and pts branches
    2. 
    
    '''
    pass