# GithubAutoStarAllInOne
Windows run AllInOne.bat    
Linux/Unix AllInOn.sh    
Python 2.7 or higher required    
GLHF
===============================================
original fork from these repo:    
***点赞脚本（Python 2.7）***:    
https://github.com/weilaihui/GitHubStar    
***加粉脚本（Python 2.7）***:    
https://github.com/weilaihui/GitHubFollow    
***Fork脚本（Python 2.7）***:    
https://github.com/acelwiker/GitAutoFork    


### Source code
#### Step 1
1. Install Python 2.x,run```python --version```and```pip```for a test.  
1. To install pip, securely download [get-pip.py](https://bootstrap.pypa.io/get-pip.py)
1. Then run the following（If you have downloaded it,skip the step.）:
    ```
    python get-pip.py
    ```
> MAKE SURE that you have installed ```requests```.
```
pip install -r requirements.txt
```
#### Step 2
1. Clone the repo  
    ```
    git clone https://github.com/wangzhenjjcn/GithubAutoStarAllInOne.git && cd GithubAutoStarAllInOne
    ```
1. Open`settings.py`, replace variables with your own infomation.
    ```
    #############settings#############
    NAME		= "1" #GitStar username
    PASSWORD	= "1" #GitStar password
    GITNAME		= "1" #Gitee username
    GITPASSWORD	= "1" #Gitee password
    #############settings#############
    ```
#### Step 3
- Run
    ```
    python -u GitHubStar.py
    ```  
    ```
    python -u GitHubFollow.py
    ``` 
    ```
    python -u GitAutoFork.py
    ``` 
Everything is ok,hooray!