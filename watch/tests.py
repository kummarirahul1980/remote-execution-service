from django.test import TestCase

# Create your tests here.
#from .watch.views import Termux
class NoTermuxApiException(Exception):
  def __init__(self, message = "Termux api not found."):
    self.message = message
    super().__init__(self.message)

class Termux:
    def check_termux():
        import shutil
        WHICH_PYTHON = shutil.which('python')
        import re
        pattern = re.compile(re.escape("com.termux/files/usr/bin"))
        
        
        # HOME_DIR = os.environ.get("PREFIX")
        # import re
        # print(HOME_DIR)
        # pattern = "com.termux/files/usr/bin"
        return pattern.search(WHICH_PYTHON)
    def check_termux_api():
        version = os.environ.get("TERMUX_API_VERSION")
        try: 
          termux_api_is_true = subprocess.run(["termux-sms-list","-h"])
          
        except FileNotFoundException:
          raise NoTermuxApiException("Termux api env not found. Please install termux api and then permit all permissions required.")
          
          
        except Exception as e:
          print("An unknown error occurred.")
          print(e)
        if version and termux_api_is_true:
          return True 
          
        else :
          raise NoTermuxApiException
          
      
    @property
    def is_termux(self=None):
      return bool(Termux.check_termux())
        
    @property 
    def has_termux_api(self):
        try :
          self.check_termux_api()
          return True
          
        except NoTermuxApiException:
            return False
            
        except Exception as e:
            print("During the handling of class, error : " ,e)
      
      
def get_last_messages():
    import subprocess
    if Termux.has_termux_api:
        terminal = subprocess.run(["termux-sms-list"],capture_output=True)
        stdout = terminal.stdout
        stderr = terminal.stderr
        return terminal
        
    else :
      print("Anonymous Environment detected.")
LIST = []
def Work ():
    terminal = get_last_messages()
    stdout = terminal.stdout.decode()
    import json
    try :
      
      stdout=json.loads(stdout)
      if isinstance(stdout,list):
        for i in stdout:
          threadid = i.get("threadid")
          if threadid in LIST:
            print (f"threadid : {threadid} repeated")
            print()
            print(json.dumps(i,indent=4))
            
          else :
            LIST.append(threadid)
      else : print("Not list -- passing")
      
      
    except Exception as e:
      print("Unknown error :")
      print(e)
      
    
    
if __name__ == "__main__":
  Work()