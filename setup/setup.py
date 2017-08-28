#!/usr/bin/python3

import os, sh

def run_bash(cmd, get_out=True):
   if get_out: #return
      return os.popen(cmd).read()
   else:
      return os.system(cmd) #prints return to screen

def install_docker():
   def add_docker_repo():
      cmd = '''
      sudo apt-get update;
      sudo apt-get install \
          apt-transport-https \
          ca-certificates \
          curl \
          software-properties-common;
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
      sudo apt-key fingerprint 0EBFCD88;

      sudo add-apt-repository \
         "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
         $(lsb_release -cs) \
         stable"
      '''
      return run_bash(cmd, get_out=False)

   def install():
      cmd = '''
         sudo apt-get update; sudo apt-get install docker-ce
      '''
      return run_bash(cmd, get_out=False)

   add_docker_repo()
   install()

   pass


def is_docker_installed():
   try:
      sh.docker()
   except Exception as e:
      return False
   return True

def check_and_install_docker():
   have_docker = is_docker_installed()
   if not have_docker:
      install_docker()

   print('have docker:', have_docker)


'''def docker_build(path):

   import pexpect
   child = pexpect.spawn()'''


def write_img_buildid(name):
   with open('latest_docker_img', 'w') as f:
      f.write(name)

def get_img_buildid():
   with open('latest_docker_img', 'r') as f:
      return f.read()
   return None


def main():
   check_and_install_docker()

   build_flags = '--no-cache'
   build_flags = ''

   cmd = 'docker build %s -f dock/Dockerfile dock' % (build_flags,)

   ret = run_bash(cmd, True)

   print(ret)

   splitted = ret.split('Successfully built ')

   if len(splitted) is not 2:
      print('failed building image:', ret)
   else:
      build_id = splitted[1]
      #build_id = 'a6072e47be06'
      write_img_name(build_id)
      print('running image: %s' % (build_id,))

      run_bash('docker run -t -i %s /bin/bash' % (build_id,), False)


def run(build_id, shared_drive_path):
   run_bash('docker run -t -i %s

if __name__ == '__main__':
   main()




def install_deps():

   def base_deps():
      cmd = '''
         sudo apt -y install sqlite3
         pip3 install Flask gunicorn
      '''
      run_bash(cmd, get_out=False)

   def flask_session_deps():
      cmd = '''
         sudo apt -y install redis-server
         pip3 install redis Flask-Session
      '''
      run_bash(cmd, get_out=False)

   base_deps()
   flask_session_deps()






