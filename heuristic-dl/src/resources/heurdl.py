import sys
import yaml
from learning import sequential
​
with open('../settings.yml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    sequential(data['epochs'], data['batch_size'], data['resources'], data['classifications'], data['training_data'])
