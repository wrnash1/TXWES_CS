# Makefile for TXWES_CS Packer Project

PACKER_FILE = txwes-fedora.pkr.hcl

.PHONY: all init build clean validate

all: validate build

init:
	packer init $(PACKER_FILE)

validate:
	packer validate $(PACKER_FILE)

build: init
	packer build -force $(PACKER_FILE)

clean:
	rm -rf build/
