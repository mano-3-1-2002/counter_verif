#===========================================================
# Questa Simulation Makefile
#===========================================================

#-----------------------------
# Tool Commands
#-----------------------------
VLIB    = vlib
VLOG    = vlog
VOPT    = vopt
VSIM    = vsim
PYTHON  = python3

#-----------------------------
# Directories
#-----------------------------
RTL_DIR     = ../rtl
TB_DIR      = ../tb
LOG_DIR     = ../logs
WORK_LIB    = work

#-----------------------------
# Source Files
#-----------------------------
RTL_SRC = $(RTL_DIR)/counter_rtl.sv
TB_SRC  = $(TB_DIR)/counter_tb.sv

#-----------------------------
# Design Names
#-----------------------------
TOP        = counter_tb
OPT_DESIGN = counter_tb_opt

#-----------------------------
# User Variables
#-----------------------------
TESTNAME ?= test1
SEED     ?= 1

# Optional compile options
VLOG_ARGS ?=

#-----------------------------
# Phony Targets
#-----------------------------
.PHONY: all lib compile opt sim regress_sim regress clean

all: sim

#===========================================================
# Create Work Library
#===========================================================
lib:
	@mkdir -p $(LOG_DIR)
	$(VLIB) $(WORK_LIB)

#===========================================================
# Compile RTL + TB
#===========================================================
compile: lib
	$(VLOG) \
	-work $(WORK_LIB) \
	$(VLOG_ARGS) \
	$(RTL_SRC) \
	$(TB_SRC) \
	-l $(LOG_DIR)/compile.log

#===========================================================
# Optimize Design
#===========================================================
opt: compile
	$(VOPT) work.$(TOP) -o $(OPT_DESIGN)

#===========================================================
# GUI Simulation (Single Test)
#===========================================================
sim: opt
	$(VSIM) \
	$(OPT_DESIGN) \
	-do run.do \
	+TESTNAME=$(TESTNAME) \
	-sv_seed $(SEED) \
	-l $(LOG_DIR)/$(TESTNAME).log

#===========================================================
# Console Simulation (Regression)
#===========================================================
regress_sim: opt
	$(VSIM) \
	-c \
	$(OPT_DESIGN) \
	-sv_seed $(SEED) \
	+TESTNAME=$(TESTNAME) \
	-l $(LOG_DIR)/$(TESTNAME).log \
	-do "run -all; exit"

#===========================================================
# Run Regression + Generate Reports
#===========================================================
regress:
	@echo "======================================"
	@echo " Running Regression"
	@echo "======================================"
	@cd .. && \
	$(PYTHON) scripts/run_regression.py && \
	$(PYTHON) scripts/log_analyzer.py

#===========================================================
# Clean Generated Files
#===========================================================
clean:
	rm -rf work
	rm -rf $(LOG_DIR)
	rm -f transcript
	rm -f vsim.wlf
	rm -f *.wlf
