#ifndef UMATT_DEFINITIONS_H_
#define UMATT_DEFINITIONS_H_

//Just in case they're not defined yet
#ifndef	TRUE
#  define	TRUE	(1==1)
#  define	FALSE	(!TRUE)
#endif

#define LOW         0
#define HIGH        1

//FIXME: Currently redefining the I/O from wiringPi.h incorrectly..
#ifndef OUTPUT
#	define OUTPUT		0 		//Verify this is right
#	define INPUT		1
#endif
							//Header pin assignments
#define MOSI 		12		//10
#define MISO 		13     	//11
#define CLK  		14     	//12
#define ADC_CS 		21     	//15
#define GPIO2_CS	22     	//16
#define GPIO3_CS	23     	//17
#define POT_CS		24     	//18
#define GPIO1_CS	27     	//23
#define GPIO4_CS	26     	//25

#endif
