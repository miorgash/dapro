import pandas as pd
from pathlib import Path
from tqdm import tqdm

class BaseLoader:
    def __init__(self):
        raise NotImplementedError
    def load(self):
        raise NotImplementedError

class LivedoorLoader(BaseLoader):
    def __init__(self, text_dir_path):
        self.text_dir_path = text_dir_path

    def load(self):

        records = []
        medium = [m for m in self.text_dir_path.glob('*') 
                  if m.name not in ('README.txt', 'CHANGES.txt')]
        
        for media in tqdm(medium):
        
            for contents in media.glob('*'):
        
                with contents.open('r') as f:
                    it = iter(f.read().splitlines())
        
                record  = []
                record.append(next(it))    # url
                record.append(next(it))    # date
                record.append(next(it))    # title
                record.append(''.join(it)) # text
                record.append(media.name)  # label
        
                records.append(record)
        
        columns = ['url', 'date', 'title', 'text', 'label']
        df = pd.DataFrame(records, columns=columns)

        return df
