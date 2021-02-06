FROM python:3.8.7-slim-buster
RUN apt-get update
RUN apt-get install vim -y
RUN apt-get install git -y
RUN git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime
RUN sh ~/.vim_runtime/install_awesome_vimrc.sh
RUN apt-get install wget unzip
RUN apt-get install -y libappindicator1 fonts-liberation
RUN apt-get install libasound2 libatk-bridge2.0-0 libatspi2.0-0 libdrm2 libgbm1 libgtk-3-0 libnspr4 libnss3 libxkbcommon0 xdg-utils -y
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome*.deb && rm /google-chrome-stable_current_amd64.deb
RUN wget https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip && mv chromedriver /bin && rm /chromedriver_linux64.zip
# RUN chromedriver -version
# RUN google-chrome-stable -version
# RUN ls
RUN python -m pip install selenium

