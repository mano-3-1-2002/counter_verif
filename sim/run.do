#===========================================================
# Questa DO File
#===========================================================

# Add all signals in the design
add wave -r sim:/*

# Run simulation until completion
run -all

# Quit simulator
quit -f
