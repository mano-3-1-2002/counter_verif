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
CONFIG_DIR  = ../config
SCRIPT_DIR  = ../scripts
WORK_LIB    = work

#-----------------------------
# Source Files
#-----------------------------
RTL_SRC = $(RTL_DIR)/counter.sv
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

# Optional compile arguments
VLOG_ARGS ?=

#-----------------------------
# Phony Targets
#-----------------------------
.PHONY: all lib compile opt sim regress clean

all: sim

#===========================================================
# Create Questa Work Library
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
	$(VOPT) work.$(TOP) \
	-o $(OPT_DESIGN)

#===========================================================
# Run Simulation
#===========================================================
sim: opt
	$(VSIM) \
	$(OPT_DESIGN) \
	-do run.do \
	+TESTNAME=$(TESTNAME) \
	-sv_seed $(SEED) \
	-l $(LOG_DIR)/$(TESTNAME).log

#===========================================================
# Regression
#===========================================================
regress:
	$(PYTHON) $(SCRIPT_DIR)/run_regression.py

#===========================================================
# Cleanup
#===========================================================
clean:
	rm -rf work
	rm -rf $(LOG_DIR)
	rm -f transcript
	rm -f vsim.wlf
	rm -f *.wlf
