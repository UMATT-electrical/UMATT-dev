###############################################
# Change these files names to match your own: #
###############################################

# name of the executable to be generated
PROG = UMATT_main
INCLUDE_DIR = include
OBJ_DIR = object
SRC_DIR = src
HDRS = $(shell find $(SRC_DIR) -name *.h -type f)
SRCS = $(shell find $(SRC_DIR) -name *.c -type f)

#######################
# Don't change these: #
#######################

# directory to store object files
# names of object files
OBJS = $(patsubst %.c, $(OBJ_DIR)/%.o, $(SRCS))

# name of the compiler
CC = gcc
# additional compiler flags to pass in
CFLAGS = -L. -I$(INCLUDE_DIR) -Wall -Wextra
# libraries for the linker
LIBS = -lwiringPi

####################
# Compiling rules: #
####################

# invoked when "make" is run
all : $(OBJ_DIR) $(PROG)

# links object files into executable
$(PROG) : $(OBJS)
	$(CC) $(CFLAGS) $(patsubst %.o, $(OBJ_DIR)/%.o, $(notdir $^)) -o $(PROG) $(LIBS)
	@echo ""
	@echo Successfully compiled to \"$(PROG)\"!

# compiles source files into object files
object/%.o : %.c $(HDRS)
	$(CC) -c $(CFLAGS) $< -o $(OBJ_DIR)/$(notdir $@) $(LIBS)

# creates directory to store object files
$(OBJ_DIR) :
	mkdir -p $@/

# cleans up object files and executable
# type "make clean" to use
# Note: you can add your own commands to remove other things (e.g. output files)
clean:
	@clear
	rm -rf object/
	rm -f $(PROG)
	@echo Finished Cleaning!
