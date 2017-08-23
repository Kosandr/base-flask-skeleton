#!/usr/bin/python3

import os, sh

def run_bash(cmd, get_out=True):
   if get_out:
      return os.popen(cmd).read()
   else:
      return os.system(cmd)

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

def main():
   check_and_install_docker()


if __name__ == '__main__':
   main()

   run_bash('docker build dock', False)


def install_deps():

   def base_deps():
      cmd = '''
         sudo apt -y install sqlite3
         pip3 install Flask
      '''
      run_bash(cmd, get_out=False)

   def flask_session_deps():
      cmd = '''
         sudo apt install -y redis-server
         pip3 install redis Flask-Session
      '''
      run_bash(cmd, get_out=False)

   base_deps()
   flask_session_deps()






