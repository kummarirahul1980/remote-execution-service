from django.shortcuts import render
import subprocess
import os
import json
from android.settings import write_log
# Create your views here.
import time


def floating_time(string):
    from datetime import datetime


    try:
        return datetime.strptime(string, "%Y-%m-%d %H:%M:%S").timestamp()
    except ValueError:
        print("Invalid format of time.")
        return ""

    except Exception as E :
        print("floating time exception:    ",E)
        return ""

# def MarkRead(message):
#     from android.settings import BASE_DIR
#     from pathlib import Path
#     with open(os.path.join(BASE_DIR,"read.rj"),"r") as rj_dev:
#         rjde

        

class NoTermuxApiException(Exception):
  def __init__(self, message = "Termux api not found."):
    self.message = message
    super().__init__(self.message)

def ExecuteCommandLine(*args):pass
def run_blocking_io(command="",*args):
  try:
    terminal = subprocess.run([command,*args],
    capture_output=True,
    text=True,
    timeout = 60,
    )
    terminal_stdout = (terminal.stdout or "")[:2500]
    terminal_stderr  = (terminal.stderr or "")[:3000]
    returnjson = {
        "stdout" : terminal_stdout,
        "stderr" : terminal_stderr
    }
    return {
        "terminal" : returnjson
    }
    
  except subprocess.TimeoutExpired:
    return { "ERROR" : "timeout expired." }
  except Exception as E:
    return { "ERROR" : "UNKNOWN",
    "message" : E}
    
  return 

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
      
      
def get_last_five_messages():

    if Termux.has_termux_api:
        terminal = subprocess.run(["termux-sms-list", "-l","5"],capture_output=True)
        stdout = terminal.stdout
        stderr = terminal.stderr
        return terminal
        
    else :
      print("Anonymous Environment detected.")
      return None


def send_return_sms(number,message):
    if number  and message:
        if len(str(number)) >= 10:
            stripped_number = str(number)[-10:]
            subprocess.run(["termux-sms-send", "-n", stripped_number, message])
            print("return sms sent.")
            write_log("Sms sent to ", stripped_number)

def ping_sms(number=""):
    write_log(f"ping request from {number}")
    send_return_sms(number=number,message="Ping recieved")
    
def CheckCLI():
    from django.contrib.auth import authenticate
    terminal = get_last_five_messages()
    terminal_stdout = terminal.stdout
    try: 
      import json
      formatted_json = json.loads(terminal_stdout.decode())
      if not isinstance(formatted_json,list):
          print("Error, not list")
          
      else :
         # print(json.dumps(formatted_json,indent=4))
          
          import time
          now = time.time()
          for i in formatted_json:
            if i.get("type") == "inbox":
              if now-(floating_time(i["received"])) < 20:


                  body = i.get("body")
                  if body == "/ping_inbox":
                      ping_sms(i.get("number"))
                      print("ping request from ", i.get("number"))
                      continue
                    
                  try : 
                      inbox_phone = i.get("number")
                      body = json.loads(body)
                      credentials = body.get("chaduvuko_first")
                      
                      execute = body.get("neekenduku_exec")
                      command = execute.get("command")
                      arguments = execute.get("args")
                      username = credentials.get("password")
                      password = credentials.get("night_changes")
                      print("Request of execution received")
                      SUPERUSER = authenticate(username = username,password= password)
                      if not SUPERUSER or not SUPERUSER.is_superuser:
                          continue
                      else :
                          print("User authenticated.")
                          if not isinstance(arguments,list):
                              pass
                          else:
                              write_log(f"Execution : {command} {arguments}")
                              print("executiom request")
                              return_json = run_blocking_io(command,*arguments) 
                              print(return_json)
                              send_return_sms(number= inbox_phone,message = json.dumps(return_json))
                  except json.JSONDecodeError:
                      #print(json.loads(body))
                      print(body)
                      my_ex = i.get("received")
                      print(my_ex, bool((now-floating_time(my_ex))<20))
                    #  print(type(body))
                      print()
                      print("Invalid format.JSONDecodeError")
                  except Exception as e:
                      #raise e
                      print("The unknown error occurred")
                      print(e)
    except json.JSONDecodeError:
        print("Invalid format.JSONDecodeError")
    except Exception as e:
        
        print("The unknown error outer occurred" )
        print(e)

        