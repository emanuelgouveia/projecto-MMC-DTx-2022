# projecto-MMC-DTx-2022
Vehicle make and model classification from images, using state-of-the-art computer vision models.

## Dataset labels
The file `stanford_train.json` contains a dictionary of labels to use with a custom-defined training dataset from the Stanford Cars dataset.
* The key `labels` contains a list of classes for all training examples, in integer format
* The keys `bbox_x1`, `bbox_y1`, `bbox_x2` and `bbox_y2` contain pixel coordinates of the vehicle bounding boxes, for all training examples
* The key `label_refs` contains a list of strings, describing each of the 196 classes. The index of each string corresponds to the integer used as a class in `labels` 
