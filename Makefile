.PHONY: run pdf clean install all

# Default target
all: run pdf

# Install dependencies
install:
	pip install -r requirements.txt

# Run the main script
run:
	cd src && python3 hello.py

# Compile Typst reports to PDF
pdf:
	typst compile output/persons_rapor.typ output/persons_rapor.pdf
	typst compile output/rapor.typ output/rapor.pdf

# Clean generated files
clean:
	rm -f output/*.svg output/*.pdf
	rm -rf __pycache__ src/__pycache__

# Help
help:
	@echo "Available targets:"
	@echo "  make install  - Install Python dependencies"
	@echo "  make run      - Run hello.py script"
	@echo "  make pdf      - Compile Typst files to PDF"
	@echo "  make clean    - Remove generated files"
	@echo "  make all      - Run script and compile PDFs"
