# Makefile

# defaults
SIM ?= verilator
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/src/ultraram.v
VERILOG_SOURCES += $(PWD)/src/ultraram_fifo.sv
VERILOG_SOURCES += $(PWD)/src/bram_fifo.sv
VERILOG_SOURCES += $(PWD)/src/top_pkg.sv
VERILOG_SOURCES += $(PWD)/src/prefetcher_pkg.sv
VERILOG_SOURCES += $(PWD)/src/prefetcher_streaming_manager.sv
VERILOG_SOURCES += $(PWD)/src/prefetcher_fetch_tag.sv

# use VHDL_SOURCES for VHDL files

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = prefetcher

# MODULE is the basename of the Python test file
MODULE = agile_prefetcher_cocotb

COCOTB_LOG_LEVEL = critical

EXTRA_ARGS += --trace-fst --trace-structs \
	-Wno-fatal -CFLAGS "-std=c++14 -Wall -O3"

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim