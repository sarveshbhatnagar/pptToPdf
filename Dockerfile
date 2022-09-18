FROM public.ecr.aws/lambda/python:3

RUN yum install \
    tar \
    gzip \
    libdbusmenu.x86_64 \
    libdbusmenu-gtk2.x86_64 \
    libSM.x86_64 \
    xorg-x11-fonts-* \
    google-noto-sans-cjk-fonts.noarch \
    binutils.x86_64 \
    -y && \
    yum clean all

RUN set -xo pipefail && \
    curl "https://ftp.halifax.rwth-aachen.de/tdf/libreoffice/stable/7.4.0/rpm/x86_64/LibreOffice_7.4.0_Linux_x86-64_rpm.tar.gz" | tar -xz

RUN cd LibreOffice_7.4.0.3_Linux_x86-64_rpm/RPMS && \
    yum install *.rpm -y && \
    rm -rf /var/task/LibreOffice_7.4.0* && \
    cd /opt/libreoffice7.4/ && \
    strip ./**/* || true

RUN cd ~/
ADD main.py .

CMD ["main.lambda_handler"]