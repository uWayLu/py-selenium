FROM selenium/standalone-chrome:119.0

USER root

# chrome 127 only
#RUN sed -i '/^deb/s/^/#/' /etc/apt/sources.list && \
#    sed -i '/^deb/s/^/#/' /etc/apt/sources.list.d/ubuntu.sources

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-selenium python3-pyvirtualdisplay && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY print_rfp_url.py .
COPY print_rfp_url.sh .
COPY print_to_pdf.sh .

RUN chmod +x print_rfp_url.py print_rfp_url.sh print_to_pdf.sh 

