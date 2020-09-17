import config
import time
from action import login
from action import explore, search
from action import follow, article
from action import like_comment


def robot(username, password, **kwargs):
    driver = config.DRIVER
    timeout = config.TIMEOUT
    login(username, password)
    driver.implicitly_wait(timeout)
    for _ in kwargs.keys():
        search(_)
        for k, v in kwargs[_].items():
            # article(k)
            # like_comment(v)
            time.sleep(5)
            
    #driver.close()

#-----------test-----------
    
if __name__ == "__main__":
    username = 'username'
    password = 'passwd'
    
    blank_dict = {}
    for i in range(5):
        blank_dict[i+1] = ()
        
    target = ['huskiis',
              'huskies_corner',
              'huskiestail',
              'shibe_site_of_life',
              'acoshiba',
              'thedailyshibainu',
            ]
    
    tar_dict = {}
    for _ in target:
        tar_dict[_] = blank_dict
    
    robot(username, password, **tar_dict)
